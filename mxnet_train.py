#from __future__ import print_function

import argparse
import array
import copy
import gc
import getpass
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot
import matplotlib.ticker
import mxnet
import numpy
import scipy
import objgraph
import os
import pickle
import pprint
import psutil
import tabulate
import time
import weakref

from mxnet.contrib import amp
amp.init()

import Common
#import Common_backup as Common
import mxnet_networks
import mxnet_train_info

import ROOT


#ROOT.gStyle.SetOptStat(11111111)

#process = psutil.Process(os.getpid())

#matplotlib.pyplot.rc("text", usetex = True)
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{amsmath}"]
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{slashed}"]


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

#parser.add_argument(
#    "--loadNetwork",
#    help = "Load saved network.",
#    default = False,
#    action = "store_true",
#)

parser.add_argument(
    "--training",
    help = "Training to run: \n%s" %("\n".join(sorted(mxnet_train_info.d_info.keys()))),
    type = str,
    choices = mxnet_train_info.d_info.keys(),
    required = True,
    metavar = "TRAINING",
)

parser.add_argument(
    "--network",
    help = "Network to use: \n%s" %("\n".join(sorted(mxnet_networks.d_network.keys()))),
    type = str,
    choices = mxnet_networks.d_network.keys(),
    required = True,
    metavar = "NETWORK",
)

parser.add_argument(
    "--reweightVars",
    help = "Variables to use for reweighting (maximum of 2 variables; will use the first two otherwise)",
    type = str,
    nargs = "*",
    required = False,
    default = [],
)

parser.add_argument(
    "--reweightVarBins",
    help = "List of the number of bins for the reweighting variables",
    type = int,
    nargs = "*",
    required = False,
    default = [200, 200],
)

parser.add_argument(
    "--nEpoch",
    help = "Number of epochs to run \nDefault: %(default)d",
    type = int,
    required = False,
    default = 200,
)

parser.add_argument(
    "--batchSize",
    help = "Batch size \nDefault: %(default)d",
    type = int,
    required = False,
    default = 100,
)

parser.add_argument(
    "--nWorker",
    help = "Number of dataloader workers \nDefault: %(default)d",
    type = int,
    required = False,
    default = 10,
)

parser.add_argument(
    "--learningRate",
    help = "learningRate size \nDefault: %(default)g",
    type = float,
    required = False,
    default = 0.001,
)

l_precision = [
    #"float16",
    "float32",
    "float64"
]

parser.add_argument(
    "--precision",
    help = "Precision: \n%s \nDefault: %%(default)s" %("\n".join(l_precision)),
    type = str,
    choices = l_precision,
    required = False,
    default = "float32",
    metavar = "PRECISION",
)

parser.add_argument(
    "--nEventTotalSig",
    help = "Total number of signal events to use \nDefault: %(default)d",
    type = int,
    required = False,
    default = int(1.35e6),
)

parser.add_argument(
    "--nEventTotalBkg",
    help = "Total number of background events to use \nDefault: %(default)d",
    type = int,
    required = False,
    default = int(1.35e6),
)

parser.add_argument(
    "--trainToTstSizeRatio",
    help = "Training to testing sample size ratio \nDefault: %(default)d",
    type = int,
    required = False,
    default = 9,
)

parser.add_argument(
    "--saveEvery",
    help = "Save the network after every how many epochs \nDefault: %(default)d",
    type = int,
    required = False,
    default = 2,
)

parser.add_argument(
    "--splitEvery",
    help = "Load how many images per (multiprocessing) process \nDefault: %(default)d",
    type = int,
    required = False,
    default = 20000,
)

parser.add_argument(
    "--nCPUfraction",
    help = "Fraction of the available CPUs to use for loading images \nDefault: %(default)g",
    type = float,
    required = False,
    default = 0.9,
)

parser.add_argument(
    "--suffix",
    help = "Suffix to be added to the output directory name \nDefault: %(default)s",
    type = str,
    required = False,
    default = "",
)


# Parse arguments
args = parser.parse_args()

if (len(args.reweightVars) > 2) :
    
    args.reweightVars = args.reweightVars[0: 2]

d_args = vars(args)

d_info_training = mxnet_train_info.d_info[args.training]


# Have to import it here
# Otherwise the help options are not being shown
import root_numpy


# Set the context
context = None

username = getpass.getuser()


if (username == "sobhatta") :
    
    print("*********************")
    print("***** Using GPU *****")
    print("*********************")
    print("\n")
    
    context = mxnet.gpu()

else :
    
    context = mxnet.cpu()


#if (args.loadNetwork) :
#    
#    networkSymbolFile = "mxnetNetworkInfo/temp/network-symbol.json"
#    networkParamFile = "mxnetNetworkInfo/temp/network-0000.params"
#    
#    print("Loading saved network.")
#    
#    neuralNetwork = mxnet.gluon.nn.SymbolBlock.imports(
#        symbol_file = networkSymbolFile,
#        param_file  = networkParamFile,
#        input_names = ["data"],
#        ctx = context,
#    )

# Get the network, initialize, hybridize
neuralNetwork = mxnet_networks.d_network[args.network]
neuralNetwork.initialize(init = mxnet.init.Xavier(), ctx = context)
neuralNetwork.hybridize()


suffix = "_%s" %(args.suffix)
suffix = suffix * (len(args.suffix) > 0)
networkDirName = "network_%s_%s%s" %(args.training, args.network, suffix)


# network directory
networkDir = "mxnetNetworkInfo/%s" %(networkDirName)
print("Network directory: %s" %(networkDir))
Common.renameAndBackupDir(networkDir)
print("")
os.system("mkdir -p %s" %(networkDir))


# Plot directory
plotDir = "plots/mxnet/%s" %(networkDirName)
print("Plot directory: %s" %(plotDir))
Common.renameAndBackupDir(plotDir)
print("")
os.system("mkdir -p %s" %(plotDir))


# Save the configuration
configOutFileName = "%s/config.txt" %(networkDir)
print("Saving the configuration to: %s" %(configOutFileName))

with open(configOutFileName, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")


nEpoch = args.nEpoch

nWorker = args.nWorker
batchSize = args.batchSize
learningRate = args.learningRate

# Save every "saveEvery" epoch
saveEvery = args.saveEvery

nDigit = max(3, len(str(int(nEpoch))))

trainToTstSize_ratio = args.trainToTstSizeRatio

nEventTrn_sig = -1
nEventTst_sig = int(float(nEventTrn_sig) / trainToTstSize_ratio)

nEventTrn_bkg = -1
nEventTst_bkg = int(float(nEventTrn_bkg) / trainToTstSize_ratio)

nEventTotal_sig = args.nEventTotalSig
nEventTotal_bkg = args.nEventTotalBkg

splitEvery = args.splitEvery


if (nEventTrn_sig > 0) :
    
    nEventTotal_sig = nEventTrn_sig + nEventTst_sig

if (nEventTrn_bkg > 0) :
    
    nEventTotal_bkg = nEventTrn_bkg + nEventTst_bkg


l_inFileName_sig = d_info_training["inputFiles_sig"]
l_inFileName_bkg = d_info_training["inputFiles_bkg"]


print("")
print("Input sig file(s): %s" %("\n "+ "\n\t".join(l_inFileName_sig)))
print("Input bkg file(s): %s" %("\n "+ "\n\t".join(l_inFileName_bkg)))
print("")

l_varStr = d_info_training["layerNames"]
l_cutVar = d_info_training["varNames"]

nVar = len(l_varStr)


cutStr_sig = d_info_training["cutStr_sig"]
cutStr_bkg = d_info_training["cutStr_bkg"]


print("")
print("Sig cut: %s" %(cutStr_sig))
print("Bkg cut: %s" %(cutStr_bkg))
print("")


# Load the custom ROOT dictionaries
ROOT.gSystem.Load("HeaderFiles/CustomRootDict_cc.so")

print("Loading sig and bkg data. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))

tree_sig = ROOT.TChain("tree")
tree_bkg = ROOT.TChain("tree")

for iFile in range(0, len(l_inFileName_sig)) :
    
    tree_sig.Add(l_inFileName_sig[iFile])

for iFile in range(0, len(l_inFileName_bkg)) :
    
    tree_bkg.Add(l_inFileName_bkg[iFile])


d_varInfo = Common.getVarInfoFromTree(
    l_varStr = l_varStr,
    tree_sig = tree_sig,
    tree_bkg = tree_bkg,
    l_cutVar = l_cutVar,
    l_spectator = args.reweightVars,
    cutStr_sig = cutStr_sig,
    cutStr_bkg = cutStr_bkg,
    nEventTotal_sig = nEventTotal_sig,
    nEventTotal_bkg = nEventTotal_bkg,
    splitEvery = splitEvery,
    nCPUfraction = args.nCPUfraction,
)


print("Loaded sig and bkg data. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))

#print(d_varInfo[l_varStr[0]].a_spec_sig.shape)
#print(d_varInfo[l_varStr[0]].a_spec_bkg.shape)
#matplotlib.pyplot.hist(d_varInfo[l_varStr[0]].a_spec_sig[:, 0], bins = 100, weights = [1.0/len(d_varInfo[l_varStr[0]].a_sig)]*len(d_varInfo[l_varStr[0]].a_sig), histtype = "step", color = "r")
#matplotlib.pyplot.hist(d_varInfo[l_varStr[0]].a_spec_bkg[:, 0], bins = 100, weights = [1.0/len(d_varInfo[l_varStr[0]].a_sig)]*len(d_varInfo[l_varStr[0]].a_sig), histtype = "step", color = "b")
#matplotlib.pyplot.show()
#time.sleep(100000)

#tree_sig.Delete()
#tree_bkg.Delete()

tree_sig = None
tree_bkg = None

print("Closed input ROOT files. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))


if (nEventTrn_sig < 0) :
    
    nEventTrn_sig = int(trainToTstSize_ratio/(1.0+trainToTstSize_ratio) * len(d_varInfo[l_varStr[0]].a_sig))
    nEventTst_sig = len(d_varInfo[l_varStr[0]].a_sig) - nEventTrn_sig
    
    nEventTotal_sig = nEventTrn_sig + nEventTst_sig

if (nEventTrn_bkg < 0) :
    
    nEventTrn_bkg = int(trainToTstSize_ratio/(1.0+trainToTstSize_ratio) * len(d_varInfo[l_varStr[0]].a_bkg))
    nEventTst_bkg = len(d_varInfo[l_varStr[0]].a_bkg) - nEventTrn_bkg
    
    nEventTotal_bkg = nEventTrn_bkg + nEventTst_bkg


print("*"*50)

print("Total training events: %d" %(nEventTrn_sig + nEventTrn_bkg))
print("\t Sig. training events: %d" %(nEventTrn_sig))
print("\t Bkg. training events: %d" %(nEventTrn_bkg))

print("Total testing events: %d" %(nEventTst_sig + nEventTst_bkg))
print("\t Sig. testing events: %d" %(nEventTst_sig))
print("\t Bkg. testing events: %d" %(nEventTst_bkg))

print("*"*50, "\n")

a_labelTrn_sig = numpy.ones(nEventTrn_sig)
a_labelTst_sig = numpy.ones(nEventTst_sig)

a_labelTrn_bkg = numpy.zeros(nEventTrn_bkg)
a_labelTst_bkg = numpy.zeros(nEventTst_bkg)


l_dataTrn_sig = []
l_dataTst_sig = []

l_dataTrn_bkg = []
l_dataTst_bkg = []

l_data = []


nRow = d_varInfo[l_varStr[0]].a_sig[0].shape[0]
nCol = d_varInfo[l_varStr[0]].a_sig[0].shape[1]

a_dataTrn = numpy.empty((nEventTrn_sig+nEventTrn_bkg, nVar, nRow, nCol), dtype = "float32")
a_dataTst = numpy.empty((nEventTst_sig+nEventTst_bkg, nVar, nRow, nCol), dtype = "float32")

print("Creating training and testing data (sig and bkg). Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))

# Load data into shape [nVar, nEvent]
for iVar in range(0, nVar) :
    
    varStr = l_varStr[iVar]
    
    varInfo = d_varInfo[varStr]
    
    #a_sig_weakref = weakref.ref(varInfo.a_sig)
    a_dataTrn[0: nEventTrn_sig, iVar, :, :] = varInfo.a_sig[0: nEventTrn_sig]
    a_dataTst[0: nEventTst_sig, iVar, :, :] = varInfo.a_sig[nEventTrn_sig: nEventTotal_sig]
    
    # Free memory
    #pprint.pprint(gc.get_referrers(varInfo.a_sig))
    #print(a_sig_weakref)
    varInfo.a_sig = None
    gc.collect()
    #print(a_sig_weakref)
    
    
    #a_bkg_weakref = weakref.ref(varInfo.a_bkg)
    a_dataTrn[nEventTrn_sig: , iVar, :, :] = varInfo.a_bkg[0: nEventTrn_bkg]
    a_dataTst[nEventTst_sig: , iVar, :, :] = varInfo.a_bkg[nEventTrn_bkg: nEventTotal_bkg]
    
    # Free memory
    #pprint.pprint(gc.get_referrers(varInfo.a_bkg))
    #print(a_bkg_weakref)
    varInfo.a_bkg = None
    gc.collect()
    #print(a_bkg_weakref)


print("Created training and testing data (sig and bkg). Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))


#pprint.pprint(globals())


# sig+bkg train labels
a_labelTrn = numpy.append(a_labelTrn_sig, a_labelTrn_bkg)

# Free memory
a_labelTrn_sig = None
a_labelTrn_bkg = None


# sig+bkg test labels
a_labelTst = numpy.append(a_labelTst_sig, a_labelTst_bkg)

# Free memory
a_labelTst_sig = None
a_labelTst_bkg = None


print("Created combined (sig+bkg) training and testing labels. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))


batchSize_trn = batchSize
batchSize_tst = batchSize

if (batchSize_trn <= 0) :
    
    batchSize_trn = a_dataTrn.shape[0]

if (batchSize_tst <= 0) :
    
    batchSize_tst = a_dataTst.shape[0]

print("Batch size (train) : %d" %(batchSize_trn))
print("Batch size (test) : %d" %(batchSize_tst))


# Reweight events
print("Creating weights. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))

a_weight_trn = numpy.ones(nEventTrn_sig + nEventTrn_bkg)
a_weight_tst = numpy.ones(nEventTst_sig + nEventTst_bkg)

h2_reweight_sig = None
h2_reweight_bkg = None

reweightHist_xMin = 0
reweightHist_xMax = 1

reweightHist_yMin = 0
reweightHist_yMax = 1

a_reweightVarX_sig = numpy.zeros(nEventTotal_sig)
a_reweightVarX_bkg = numpy.zeros(nEventTotal_bkg)

a_reweightVarY_sig = numpy.zeros(nEventTotal_sig)
a_reweightVarY_bkg = numpy.zeros(nEventTotal_bkg)

if (len(args.reweightVars)) :
    
    a_reweightVarX_sig = d_varInfo[l_varStr[0]].a_spec_sig[:, 0]
    a_reweightVarX_bkg = d_varInfo[l_varStr[0]].a_spec_bkg[:, 0]
    
    reweightHist_xMin = min(a_reweightVarX_sig)
    reweightHist_xMin = min(reweightHist_xMin, min(a_reweightVarX_bkg))
    
    reweightHist_xMax = max(a_reweightVarX_sig)
    reweightHist_xMax = max(reweightHist_xMax, min(a_reweightVarX_bkg))
    reweightHist_xMax += reweightHist_xMax/100.0 # For the values exactly at the maximum

if (len(args.reweightVars) == 2) :
    
    a_reweightVarY_sig = d_varInfo[l_varStr[0]].a_spec_sig[:, 1]
    a_reweightVarY_bkg = d_varInfo[l_varStr[0]].a_spec_bkg[:, 1]
    
    reweightHist_yMin = min(a_reweightVarY_sig)
    reweightHist_yMin = min(reweightHist_yMin, min(a_reweightVarY_bkg))
    
    reweightHist_yMax = max(a_reweightVarY_sig)
    reweightHist_yMax = max(reweightHist_yMax, min(a_reweightVarY_bkg))
    reweightHist_yMax += reweightHist_yMax/100.0 # For the values exactly at the maximum

print(reweightHist_xMin, reweightHist_xMax, args.reweightVarBins[0])
print(reweightHist_yMin, reweightHist_yMax, args.reweightVarBins[1])

h2_reweight_sig = ROOT.TH2F("h2_reweight_sig", "h2_reweight_sig", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax, args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h2_reweight_bkg = ROOT.TH2F("h2_reweight_bkg", "h2_reweight_bkg", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax, args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)

h2_reweight_sig.SetDirectory(0)
h2_reweight_bkg.SetDirectory(0)

h2_reweight_sig.Sumw2()
h2_reweight_bkg.Sumw2()

#h2_reweight_sig.FillN(len(a_reweightVarX_sig), a_reweightVarX_sig, a_reweightVarY_sig, numpy.ones(len(a_reweightVarX_sig)))
#h2_reweight_bkg.FillN(len(a_reweightVarX_bkg), a_reweightVarX_bkg, a_reweightVarY_bkg, numpy.ones(len(a_reweightVarX_bkg)))

root_numpy.fill_hist(hist = h2_reweight_sig, array = list(zip(a_reweightVarX_sig, a_reweightVarY_sig)))
root_numpy.fill_hist(hist = h2_reweight_bkg, array = list(zip(a_reweightVarX_bkg, a_reweightVarY_bkg)))

#h2_reweight_sig.Draw("colz")

#print(a_reweightVarX_sig)
#print(a_reweightVarY_sig)
print(h2_reweight_sig.Integral())
print(h2_reweight_bkg.Integral())
print(h2_reweight_sig.GetEntries())
print(h2_reweight_bkg.GetEntries())

h2_reweight_sig.Scale(1.0 / h2_reweight_sig.Integral())
h2_reweight_bkg.Scale(1.0 / h2_reweight_bkg.Integral())


for iEle in range(0, nEventTotal_sig) :
    
    xVal = a_reweightVarX_sig[iEle]
    yVal = a_reweightVarY_sig[iEle]
    
    binX = h2_reweight_sig.GetXaxis().FindBin(xVal)
    binY = h2_reweight_sig.GetYaxis().FindBin(yVal)
    
    binContent_sig = h2_reweight_sig.GetBinContent(binX, binY)
    binContent_bkg = h2_reweight_bkg.GetBinContent(binX, binY)
    
    weight = 1.0
    
    if (binContent_sig != 0) :
        
        weight = min(binContent_sig, binContent_bkg) / binContent_sig
        
        #weight = 1.0/(h2_reweight_sig.GetNbinsX()*h2_reweight_sig.GetNbinsY()) / binContent_sig
    
    
    if (iEle < nEventTrn_sig) :
        
        idx = iEle
        offset = 0
        
        a_weight_trn[offset+idx] = weight
    
    else :
        
        idx = iEle-nEventTrn_sig
        offset = 0
        
        a_weight_tst[offset+idx] = weight


for iEle in range(0, nEventTotal_bkg) :
    
    xVal = a_reweightVarX_bkg[iEle]
    yVal = a_reweightVarY_bkg[iEle]
    
    binX = h2_reweight_bkg.GetXaxis().FindBin(xVal)
    binY = h2_reweight_bkg.GetYaxis().FindBin(yVal)
    
    binContent_sig = h2_reweight_sig.GetBinContent(binX, binY)
    binContent_bkg = h2_reweight_bkg.GetBinContent(binX, binY)
    
    weight = 1.0
    
    if (binContent_bkg != 0) :
        
        weight = min(binContent_sig, binContent_bkg) / binContent_bkg
        
        #weight = 1.0/(h2_reweight_bkg.GetNbinsX()*h2_reweight_bkg.GetNbinsY()) / binContent_bkg
    
    
    if (iEle < nEventTrn_bkg) :
        
        idx = iEle
        offset = nEventTrn_sig
        
        a_weight_trn[offset+idx] = weight
    
    else :
        
        idx = iEle-nEventTrn_bkg
        offset = nEventTst_sig
        
        a_weight_tst[offset+idx] = weight


# Normalize weights
a_weight_trn[0: nEventTrn_sig] = a_weight_trn[0: nEventTrn_sig] / sum(a_weight_trn[0: nEventTrn_sig])
a_weight_trn[nEventTrn_sig:  ] = a_weight_trn[nEventTrn_sig:  ] / sum(a_weight_trn[nEventTrn_sig:  ])

a_weight_tst[0: nEventTst_sig] = a_weight_tst[0: nEventTst_sig] / sum(a_weight_tst[0: nEventTst_sig])
a_weight_tst[nEventTst_sig:  ] = a_weight_tst[nEventTst_sig:  ] / sum(a_weight_tst[nEventTst_sig:  ])


print(sum(a_weight_trn[0: nEventTrn_sig]))
print(sum(a_weight_trn[nEventTrn_sig:  ]))
print(sum(a_weight_tst[0: nEventTst_sig]))
print(sum(a_weight_tst[nEventTst_sig:  ]))


# Reweighting x-variable (before reweighting)
h1_x_sig_trn = ROOT.TH1F("h1_x_sig_trn", "h1_x_sig_trn", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)
h1_x_bkg_trn = ROOT.TH1F("h1_x_bkg_trn", "h1_x_bkg_trn", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)
h1_x_sig_tst = ROOT.TH1F("h1_x_sig_tst", "h1_x_sig_tst", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)
h1_x_bkg_tst = ROOT.TH1F("h1_x_bkg_tst", "h1_x_bkg_tst", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)

root_numpy.fill_hist(hist = h1_x_sig_trn, array = a_reweightVarX_sig[0: nEventTrn_sig], weights = numpy.ones(nEventTrn_sig)/float(nEventTrn_sig))
root_numpy.fill_hist(hist = h1_x_bkg_trn, array = a_reweightVarX_bkg[0: nEventTrn_bkg], weights = numpy.ones(nEventTrn_bkg)/float(nEventTrn_bkg))

root_numpy.fill_hist(hist = h1_x_sig_tst, array = a_reweightVarX_sig[nEventTrn_sig: nEventTotal_sig], weights = numpy.ones(nEventTst_sig)/float(nEventTst_sig))
root_numpy.fill_hist(hist = h1_x_bkg_tst, array = a_reweightVarX_bkg[nEventTrn_bkg: nEventTotal_bkg], weights = numpy.ones(nEventTst_bkg)/float(nEventTst_bkg))

h1_x_sig_trn.SetLineWidth(2)
h1_x_bkg_trn.SetLineWidth(2)
h1_x_sig_tst.SetLineWidth(2)
h1_x_bkg_tst.SetLineWidth(2)

h1_x_sig_trn.SetLineColor(2)
h1_x_bkg_trn.SetLineColor(4)
h1_x_sig_tst.SetLineColor(2)
h1_x_bkg_tst.SetLineColor(4)

h1_x_sig_tst.SetLineStyle(2)
h1_x_bkg_tst.SetLineStyle(2)


# Reweighting x-variable (after reweighting)
h1_x_sig_trn_reweighted = ROOT.TH1F("h1_x_sig_trn_reweighted", "h1_x_sig_trn_reweighted", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)
h1_x_bkg_trn_reweighted = ROOT.TH1F("h1_x_bkg_trn_reweighted", "h1_x_bkg_trn_reweighted", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)
h1_x_sig_tst_reweighted = ROOT.TH1F("h1_x_sig_tst_reweighted", "h1_x_sig_tst_reweighted", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)
h1_x_bkg_tst_reweighted = ROOT.TH1F("h1_x_bkg_tst_reweighted", "h1_x_bkg_tst_reweighted", args.reweightVarBins[0], reweightHist_xMin, reweightHist_xMax)

root_numpy.fill_hist(hist = h1_x_sig_trn_reweighted, array = a_reweightVarX_sig[0: nEventTrn_sig], weights = a_weight_trn[0: nEventTrn_sig])
root_numpy.fill_hist(hist = h1_x_bkg_trn_reweighted, array = a_reweightVarX_bkg[0: nEventTrn_bkg], weights = a_weight_trn[nEventTrn_sig:  ])

root_numpy.fill_hist(hist = h1_x_sig_tst_reweighted, array = a_reweightVarX_sig[nEventTrn_sig: nEventTotal_sig], weights = a_weight_tst[0: nEventTst_sig])
root_numpy.fill_hist(hist = h1_x_bkg_tst_reweighted, array = a_reweightVarX_bkg[nEventTrn_bkg: nEventTotal_bkg], weights = a_weight_tst[nEventTst_sig:  ])

h1_x_sig_trn_reweighted.SetLineWidth(2)
h1_x_bkg_trn_reweighted.SetLineWidth(2)
h1_x_sig_tst_reweighted.SetLineWidth(2)
h1_x_bkg_tst_reweighted.SetLineWidth(2)

h1_x_sig_trn_reweighted.SetLineColor(2)
h1_x_bkg_trn_reweighted.SetLineColor(4)
h1_x_sig_tst_reweighted.SetLineColor(2)
h1_x_bkg_tst_reweighted.SetLineColor(4)

h1_x_sig_tst_reweighted.SetLineStyle(2)
h1_x_bkg_tst_reweighted.SetLineStyle(2)


# Reweighting y-variable (before reweighting)
h1_y_sig_trn = ROOT.TH1F("h1_y_sig_trn", "h1_y_sig_trn", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h1_y_bkg_trn = ROOT.TH1F("h1_y_bkg_trn", "h1_y_bkg_trn", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h1_y_sig_tst = ROOT.TH1F("h1_y_sig_tst", "h1_y_sig_tst", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h1_y_bkg_tst = ROOT.TH1F("h1_y_bkg_tst", "h1_y_bkg_tst", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)

root_numpy.fill_hist(hist = h1_y_sig_trn, array = a_reweightVarY_sig[0: nEventTrn_sig], weights = numpy.ones(nEventTrn_sig)/float(nEventTrn_sig))
root_numpy.fill_hist(hist = h1_y_bkg_trn, array = a_reweightVarY_bkg[0: nEventTrn_bkg], weights = numpy.ones(nEventTrn_bkg)/float(nEventTrn_bkg))

root_numpy.fill_hist(hist = h1_y_sig_tst, array = a_reweightVarY_sig[nEventTrn_sig: nEventTotal_sig], weights = numpy.ones(nEventTst_sig)/float(nEventTst_sig))
root_numpy.fill_hist(hist = h1_y_bkg_tst, array = a_reweightVarY_bkg[nEventTrn_bkg: nEventTotal_bkg], weights = numpy.ones(nEventTst_bkg)/float(nEventTst_bkg))

h1_y_sig_trn.SetLineWidth(2)
h1_y_bkg_trn.SetLineWidth(2)
h1_y_sig_tst.SetLineWidth(2)
h1_y_bkg_tst.SetLineWidth(2)

h1_y_sig_trn.SetLineColor(2)
h1_y_bkg_trn.SetLineColor(4)
h1_y_sig_tst.SetLineColor(2)
h1_y_bkg_tst.SetLineColor(4)

h1_y_sig_tst.SetLineStyle(2)
h1_y_bkg_tst.SetLineStyle(2)


# Reweighting y-variable (after reweighting)
h1_y_sig_trn_reweighted = ROOT.TH1F("h1_y_sig_trn_reweighted", "h1_y_sig_trn_reweighted", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h1_y_bkg_trn_reweighted = ROOT.TH1F("h1_y_bkg_trn_reweighted", "h1_y_bkg_trn_reweighted", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h1_y_sig_tst_reweighted = ROOT.TH1F("h1_y_sig_tst_reweighted", "h1_y_sig_tst_reweighted", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)
h1_y_bkg_tst_reweighted = ROOT.TH1F("h1_y_bkg_tst_reweighted", "h1_y_bkg_tst_reweighted", args.reweightVarBins[1], reweightHist_yMin, reweightHist_yMax)

root_numpy.fill_hist(hist = h1_y_sig_trn_reweighted, array = a_reweightVarY_sig[0: nEventTrn_sig], weights = a_weight_trn[0: nEventTrn_sig])
root_numpy.fill_hist(hist = h1_y_bkg_trn_reweighted, array = a_reweightVarY_bkg[0: nEventTrn_bkg], weights = a_weight_trn[nEventTrn_sig:  ])

root_numpy.fill_hist(hist = h1_y_sig_tst_reweighted, array = a_reweightVarY_sig[nEventTrn_sig: nEventTotal_sig], weights = a_weight_tst[0: nEventTst_sig])
root_numpy.fill_hist(hist = h1_y_bkg_tst_reweighted, array = a_reweightVarY_bkg[nEventTrn_bkg: nEventTotal_bkg], weights = a_weight_tst[nEventTst_sig:  ])

h1_y_sig_trn_reweighted.SetLineWidth(2)
h1_y_bkg_trn_reweighted.SetLineWidth(2)
h1_y_sig_tst_reweighted.SetLineWidth(2)
h1_y_bkg_tst_reweighted.SetLineWidth(2)

h1_y_sig_trn_reweighted.SetLineColor(2)
h1_y_bkg_trn_reweighted.SetLineColor(4)
h1_y_sig_tst_reweighted.SetLineColor(2)
h1_y_bkg_tst_reweighted.SetLineColor(4)

h1_y_sig_tst_reweighted.SetLineStyle(2)
h1_y_bkg_tst_reweighted.SetLineStyle(2)

#h1_x_sig_trn_reweighted.Draw("hist")
#h1_x_bkg_trn_reweighted.Draw("hist sames")
#h1_x_sig_tst_reweighted.Draw("hist sames")
#h1_x_bkg_tst_reweighted.Draw("hist sames")


#time.sleep(100000)
#exit()

#input()


print("Created weights. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))


reweightVarROOTfileName = "%s/reweightVar.root" %(plotDir)
reweightVarROOTfile = ROOT.TFile(reweightVarROOTfileName, "RECREATE")
reweightVarROOTfile.cd()

h2_reweight_sig.Write()
h2_reweight_bkg.Write()

h1_x_sig_trn.Write()
h1_x_bkg_trn.Write()
h1_x_sig_tst.Write()
h1_x_bkg_tst.Write()

h1_y_sig_trn.Write()
h1_y_bkg_trn.Write()
h1_y_sig_tst.Write()
h1_y_bkg_tst.Write()

h1_x_sig_trn_reweighted.Write()
h1_x_bkg_trn_reweighted.Write()
h1_x_sig_tst_reweighted.Write()
h1_x_bkg_tst_reweighted.Write()

h1_y_sig_trn_reweighted.Write()
h1_y_bkg_trn_reweighted.Write()
h1_y_sig_tst_reweighted.Write()
h1_y_bkg_tst_reweighted.Write()

reweightVarROOTfile.Close()

print("Stored reweighting variables in: %s" %(reweightVarROOTfileName))


##### Create labelled train dataset #####
dataSet_trn = mxnet.gluon.data.dataset.ArrayDataset(a_dataTrn, a_labelTrn, a_weight_trn)

# Free memory
a_dataTrn = None
a_labelTrn = None

# Divide labelled train dataset into batches
batchDataSet_trn = mxnet.gluon.data.DataLoader(
    dataSet_trn, batch_size = batchSize_trn, shuffle = True, num_workers = nWorker
)

# Free memory
dataSet_trn = None

print("Created batch data for training. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))


##### Create labelled test dataset #####
dataSet_tst = mxnet.gluon.data.dataset.ArrayDataset(a_dataTst, a_labelTst, a_weight_tst)

# Free memory
a_dataTst = None
a_labelTst = None

# Divide labelled test dataset into batches
batchDataSet_tst = mxnet.gluon.data.DataLoader(
    dataSet_tst, batch_size = batchSize_tst, shuffle = True, num_workers = nWorker
)

# Free memory
dataSet_tst = None

print("Created batch data for testing. Memory usage: %0.4f GB (%0.4f GB)" %(Common.getMemoryMB()/1024.0, Common.getMaxMemoryMB()/1024.0))


# Define the loss function
#lossFunction = mxnet.gluon.loss.SoftmaxCrossEntropyLoss()
lossFunction = mxnet.gluon.loss.L2Loss()


# Define the trainer
trainer = mxnet.gluon.Trainer(
    params = neuralNetwork.collect_params(),
    optimizer = "adam",
    #optimizer = "sgd",
    optimizer_params = {"learning_rate": learningRate},
)

amp.init_trainer(trainer)


def getAccuracy(output, label, weight = None) :
    
    pred = output.max(axis = 1)
    #print(pred)
    
    #pred = output
    #print(pred.asnumpy())
    
    pred = [ele > 0.5 for ele in pred.asnumpy()]
    #print(pred)
    
    acc = numpy.array([pred[iEle] == label.asnumpy()[iEle] for iEle in range(0, len(pred))])
    #print(acc)
    
    #acc = numpy.average(acc)
    acc = numpy.average(acc, weights = weight.asnumpy())
    
    return acc


#mxnet.viz.plot_network(neuralNetwork(mxnet.sym.var("data")))
#time.sleep(10000)

l_lossTrn = []
l_lossTst = []

l_accuTrn = []
l_accuTst = []


l_output_trn_sig = []
l_output_tst_sig = []

l_output_trn_bkg = []
l_output_tst_bkg = []


#exit(1)


for iEpoch in range(0, nEpoch) :
    
    saveNetwork = (iEpoch+1) % saveEvery == 0 or (iEpoch+1) % 5 == 0 or iEpoch+1 == nEpoch or (iEpoch+1) == 1
    
    l_output_trn_sig = []
    l_output_tst_sig = []
    
    l_output_trn_bkg = []
    l_output_tst_bkg = []
    
    lossTrn = 0.0
    lossTst = 0.0
    
    accuTrn = 0.0
    accuTst = 0.0
    
    tic = time.time()
    
    #accuTrn = mxnet.metric.Accuracy()
    
    a_sig_epoch = []
    a_bkg_epoch = []
    
    # Train
    for iBatch, (data, label, weight) in enumerate(batchDataSet_trn) :
        
        data = data.as_in_context(context).astype("float32")
        label = label.as_in_context(context).astype("float32")
        weight = weight.as_in_context(context).astype("float32")
        
        # forward + backward
        with mxnet.autograd.record() :
            
            #print mxnet.autograd.is_training()
            
            output = neuralNetwork(data)
            loss = lossFunction(output, label, weight)
            
            with amp.scale_loss(loss, trainer) as scaled_loss:
                
                mxnet.autograd.backward(scaled_loss)
        
        #loss.backward()
        
        # update parameters
        trainer.step(batchSize)
    
    
    # Compute some stuff
    for iBatch, (data, label, weight) in enumerate(batchDataSet_trn) :
        
        data = data.as_in_context(context).astype("float32")
        label = label.as_in_context(context).astype("float32")
        weight = weight.as_in_context(context).astype("float32")
        
        output = neuralNetwork(data)
        loss = lossFunction(output, label, weight)
        
        lossTrn_inst = loss.sum().asscalar()
        accuTrn_inst = getAccuracy(output, label, weight)
        
        lossTrn += lossTrn_inst
        accuTrn += accuTrn_inst
        
        if (saveNetwork) :
            
            if (1 in label.asnumpy()) :
                
                l_output_batchTrn_sig = output.asnumpy().flatten()[numpy.where(label.asnumpy().flatten())]
                l_output_trn_sig.extend(l_output_batchTrn_sig)
            
            if (0 in label.asnumpy()) :
                
                l_output_batchTrn_bkg = output.asnumpy().flatten()[numpy.where(1.0 - label.asnumpy().flatten())]
                l_output_trn_bkg.extend(l_output_batchTrn_bkg)
    
    #matplotlib.pyplot.hist(a_sig_epoch, bins = 100, histtype = "step", color = "r")
    #matplotlib.pyplot.hist(a_bkg_epoch, bins = 100, histtype = "step", color = "b")
    #matplotlib.pyplot.show()
    
    
    # Test
    for iBatch, (data, label, weight) in enumerate(batchDataSet_tst) :
        
        data = data.as_in_context(context).astype("float32")
        label = label.as_in_context(context).astype("float32")
        weight = weight.as_in_context(context).astype("float32")
        
        output = neuralNetwork(data)
        loss = lossFunction(output, label, weight)
        
        lossTst_inst = loss.sum().asscalar()
        accuTst_inst = getAccuracy(output, label, weight)
        
        lossTst += lossTst_inst
        accuTst += accuTst_inst
        
        
        if (saveNetwork) :
            
            if (1 in label.asnumpy()) :
                
                l_output_batchTst_sig = output.asnumpy().flatten()[numpy.where(label.asnumpy().flatten())]
                l_output_tst_sig.extend(l_output_batchTst_sig)
            
            if (0 in label.asnumpy()) :
                
                l_output_batchTst_bkg = output.asnumpy().flatten()[numpy.where(1.0 - label.asnumpy().flatten())]
                l_output_tst_bkg.extend(l_output_batchTst_bkg)
    
    
    lossTrn = numpy.sqrt(lossTrn)
    lossTst = numpy.sqrt(lossTst)
    
    accuTrn /= len(batchDataSet_trn)
    accuTst /= len(batchDataSet_tst),
    
    
    l_lossTrn.append(lossTrn)
    l_lossTst.append(lossTst)
    
    l_accuTrn.append(accuTrn)
    l_accuTst.append(accuTst)
    
    
    print(
        "Epoch %d/%d: "
        "train (test) loss %0.4e (%0.4e), "
        "train (test) acc %0.4f (%0.4f), "
        "in %0.1f sec " 
        "\n" %(
        
        iEpoch+1, nEpoch,
        lossTrn, lossTst,
        accuTrn, accuTst,
        time.time()-tic
    ))
    
    
    #################### Save loss and accuracy ####################
    lossAccFileName = "%s/loss_accuracy.txt" %(networkDir)
    
    with open(lossAccFileName, "a+") as tempFile :
        
        if (not iEpoch) :
            
            line_str = (
                "#epoch,"
                "loss_train,loss_test,"
                "acc_train,acc_test,"
                "\n"
            )
            
            tempFile.write(line_str)
        
        
        line_str = (
            "%03d,"
            "%0.4e,%0.4e,"
            "%0.4e,%0.4e,"
            "\n"
        )%(
            iEpoch+1,
            lossTrn, lossTst,
            accuTrn, accuTst,
        )
        
        tempFile.write(line_str)
    
    
    # Save the network
    if (saveNetwork) :
        
        #neuralNetwork.export("%s/network_epoch%0*d" %(networkDir, nDigit, iEpoch+1))
        neuralNetwork.export("%s/network" %(networkDir), epoch = iEpoch+1)
        
        print("%s Network saved %s \n" %("*"*20, "*"*20))
        
        
        #################### Save discriminator histograms ####################
        l_weight_trn_sig = numpy.ones(nEventTrn_sig) / float(nEventTrn_sig)
        l_weight_tst_sig = numpy.ones(nEventTst_sig) / float(nEventTst_sig)
        
        l_weight_trn_bkg = numpy.ones(nEventTrn_bkg) / float(nEventTrn_bkg)
        l_weight_tst_bkg = numpy.ones(nEventTst_bkg) / float(nEventTst_bkg)
        
        
        outROOTfileName = "%s/discriminator_epoch%0*d.root" %(plotDir, nDigit, iEpoch+1)
        
        h1_discr_trn_sig = ROOT.TH1F("h1_discr_trn_sig", "h1_discr_trn_sig", 100, 0.0, 1.0)
        h1_discr_trn_bkg = ROOT.TH1F("h1_discr_trn_bkg", "h1_discr_trn_bkg", 100, 0.0, 1.0)
        
        h1_discr_tst_sig = ROOT.TH1F("h1_discr_tst_sig", "h1_discr_tst_sig", 100, 0.0, 1.0)
        h1_discr_tst_bkg = ROOT.TH1F("h1_discr_tst_bkg", "h1_discr_tst_bkg", 100, 0.0, 1.0)
        
        
        a_weight_temp = array.array("f", [1]*len(l_output_trn_sig))
        
        #print(len(l_output_trn_sig), len(l_weight_trn_sig))
        #print(len(l_output_trn_bkg), len(l_weight_trn_bkg))
        #print(len(l_output_tst_sig), len(l_weight_tst_sig))
        #print(len(l_output_tst_bkg), len(l_weight_tst_bkg))
        
        root_numpy.fill_hist(hist = h1_discr_trn_sig, array = l_output_trn_sig, weights = l_weight_trn_sig)
        root_numpy.fill_hist(hist = h1_discr_trn_bkg, array = l_output_trn_bkg, weights = l_weight_trn_bkg)
        root_numpy.fill_hist(hist = h1_discr_tst_sig, array = l_output_tst_sig, weights = l_weight_tst_sig)
        root_numpy.fill_hist(hist = h1_discr_tst_bkg, array = l_output_tst_bkg, weights = l_weight_tst_bkg)
        
        #root_numpy.fill_hist(h1_discr_trn_sig, numpy.array(l_output_trn_sig, dtype = "f"))
        #root_numpy.fill_hist(h1_discr_trn_bkg, numpy.array(l_output_trn_bkg, dtype = "f"))
        #root_numpy.fill_hist(h1_discr_tst_sig, numpy.array(l_output_tst_sig, dtype = "f"))
        #root_numpy.fill_hist(h1_discr_tst_bkg, numpy.array(l_output_tst_bkg, dtype = "f"))
        
        
        #h1_discr_trn_sig.Fill(len(l_output_trn_sig), array.array("f", l_output_trn_sig), a_weight_temp)
        #h1_discr_trn_bkg.Fill(len(l_output_trn_bkg), array.array("f", l_output_trn_bkg), a_weight_temp)
        #
        #h1_discr_tst_sig.Fill(len(l_output_tst_sig), array.array("f", l_output_tst_sig), a_weight_temp)
        #h1_discr_tst_bkg.Fill(len(l_output_tst_bkg), array.array("f", l_output_tst_bkg), a_weight_temp)
        
        
        h1_discr_trn_sig.SetLineColor(2)
        h1_discr_trn_sig.SetLineStyle(1)
        h1_discr_trn_sig.SetLineWidth(2)
        
        h1_discr_trn_bkg.SetLineColor(4)
        h1_discr_trn_bkg.SetLineStyle(1)
        h1_discr_trn_bkg.SetLineWidth(2)
        
        h1_discr_tst_sig.SetLineColor(2)
        h1_discr_tst_sig.SetLineStyle(7)
        h1_discr_tst_sig.SetLineWidth(2)
        
        h1_discr_tst_bkg.SetLineColor(4)
        h1_discr_tst_bkg.SetLineStyle(7)
        h1_discr_tst_bkg.SetLineWidth(2)
        
        
        outROOTfile = ROOT.TFile(outROOTfileName, "RECREATE")
        outROOTfile.cd()
        
        h1_discr_trn_sig.Write()
        h1_discr_trn_bkg.Write()
        
        h1_discr_tst_sig.Write()
        h1_discr_tst_bkg.Write()
        
        
        outROOTfile.Close()
        
        
        #################### Plot discriminator ####################
        
        fig = matplotlib.pyplot.figure(figsize = [9, 7])
        axis = fig.add_subplot(1, 1, 1)
        
        axis.set_xlabel("MVA discriminator")
        axis.set_ylabel("a.u.")
        
        xMin = 0.00001
        xMax = 1.00001
        tickInterval_major = 0.1
        tickInterval_minor = tickInterval_major / 5.0
        
        l_tick_major = numpy.arange(xMin, xMax+tickInterval_major, tickInterval_major)
        l_tick_minor = numpy.arange(xMin, xMax+tickInterval_minor, tickInterval_minor)
        
        axis.set_xticks(l_tick_major)
        axis.set_xticks(l_tick_minor, minor = True)
        
        
        yMin = 1e9
        
        l_binContent, temp, temp = axis.hist(l_output_trn_sig, bins = 100, range = (0, 1), weights = l_weight_trn_sig, histtype = "step", color = "b", linewidth = 2, label = "Sig. training sample")
        yMin = min(yMin, min(numpy.extract(l_binContent > 0, l_binContent)))
        #print(yMin, l_binContent.shape)
        
        l_binContent, temp, temp = axis.hist(l_output_tst_sig, bins = 100, range = (0, 1), weights = l_weight_tst_sig, histtype = "step", color = "b", linewidth = 2, label = "Sig. testing sample", linestyle = "--")
        yMin = min(yMin, min(numpy.extract(l_binContent > 0, l_binContent)))
        #print(yMin, l_binContent.shape)
        
        l_binContent, temp, temp = axis.hist(l_output_trn_bkg, bins = 100, range = (0, 1), weights = l_weight_trn_bkg, histtype = "step", color = "r", linewidth = 2, label = "Bkg. training sample")
        yMin = min(yMin, min(numpy.extract(l_binContent > 0, l_binContent)))
        #print(yMin, l_binContent.shape)
        
        l_binContent, temp, temp = axis.hist(l_output_tst_bkg, bins = 100, range = (0, 1), weights = l_weight_tst_bkg, histtype = "step", color = "r", linewidth = 2, label = "Bkg. testing sample", linestyle = "--")
        yMin = min(yMin, min(numpy.extract(l_binContent > 0, l_binContent)))
        #print(yMin, l_binContent.shape)
        
        
        # Change the legend entry to a line (box by default for step histograms)
        l_handle, l_label = axis.get_legend_handles_labels()
        
        l_handle_mod = [
            matplotlib.lines.Line2D(
                [], [],
                color = h.get_edgecolor(),
                linewidth = h.get_linewidth(),
                linestyle = h.get_linestyle(),
            )
        for h in l_handle]
        
        
        legend = axis.legend(
            handles = l_handle_mod,
            labels = l_label,
            loc = "upper center",
            shadow = False,
            handlelength = matplotlib.rcParams["legend.handlelength"] * 1.5,
        )
        
        legend.get_frame().set_linewidth(2)
        
        axis.grid(which = "major")
        
        axis.set_xlim([0.0, 1.00001])
        
        
        # Linear scale
        axis.set_yticks(numpy.arange(0.0, 1.0+0.1, 0.1))
        axis.set_yticks(numpy.arange(0.0, 1.0+0.1/10, 0.1/10), minor = True)
        axis.set_ylim([0.0, 1.00001])
        
        outFileName = "%s/discriminator_epoch%0*d" %(plotDir, nDigit, iEpoch+1)
        
        fig.tight_layout()
        fig.savefig("%s.pdf" %(outFileName))
        
        pickle.dump(
            fig,
            open("%s.pickle" %(outFileName), "wb")
        )
        
        
        # Log scale
        axis.set_yscale("log")
        
        #axis.set_ylim([pow(10, -power), 1])
        axis.set_ylim([yMin/2.0, 1])
        
        outFileName = "%s/discriminator_epoch%0*d_logY" %(plotDir, nDigit, iEpoch+1)
        
        fig.tight_layout()
        fig.savefig("%s.pdf" %(outFileName))
        
        pickle.dump(
            fig,
            open("%s.pickle" %(outFileName), "wb")
        )
        
        
        matplotlib.pyplot.close()
        #matplotlib.pyplot.show()
    
    
    
    #################### Plot accuracy/loss ####################
    
    l_epochNumber = range(1, iEpoch+2)
    
    #print(l_epochNumber)
    #print(l_lossTrn)
    
    fig = matplotlib.pyplot.figure(figsize = [9, 7])
    axis1 = fig.add_subplot(1, 1, 1)
    
    colorAxis1 = "r"
    axis1.set_xlabel("Epoch")
    axis1.set_ylabel("Loss", color = colorAxis1)
    axis1.tick_params(axis = "y", labelcolor = colorAxis1)
    axis1.set_yticks(numpy.arange(0.0, 1.0+0.1, 0.1))
    axis1.set_yticks(numpy.arange(0.0, 1.0+0.1/10, 0.1/10), minor = True)
    axis1.set_xlim([l_epochNumber[0], l_epochNumber[-1]])
    axis1.set_ylim([0.0, 1.0])
    
    # Instantiate a second axes that shares the same x-axis
    axis2 = axis1.twinx()
    
    colorAxis2 = "b"
    axis2.set_ylabel("Accuracy", color = colorAxis2)
    axis2.tick_params(axis = "y", labelcolor = colorAxis2)
    axis2.set_yticks(numpy.arange(0.0, 1+0.1, 0.1))
    axis2.set_yticks(numpy.arange(0.0, 1+0.1/10, 0.1/10), minor = True)
    axis2.set_ylim([0.0, 1.0])
    
    
    axis1.plot(
        l_epochNumber, l_lossTrn,
        color = colorAxis1,
        linestyle = "-",
        linewidth = 2,
        markersize = 0
    )
    
    axis1.plot(
        l_epochNumber, l_lossTst,
        color = colorAxis1,
        linestyle = "--",
        linewidth = 2,
        markersize = 0
    )
    
    
    axis2.plot(
        l_epochNumber, l_accuTrn,
        color = colorAxis2,
        linestyle = "-",
        linewidth = 2,
        markersize = 0
    )
    
    axis2.plot(
        l_epochNumber, l_accuTst,
        color = colorAxis2,
        linestyle = "--",
        linewidth = 2,
        markersize = 0
    )
    
    
    outFileName = "%s/accuracy-loss" %(plotDir)
    
    fig.tight_layout()
    fig.savefig("%s.pdf" %(outFileName))
    
    pickle.dump(
        fig,
        open("%s.pickle" %(outFileName), "wb")
    )
    
    matplotlib.pyplot.close()

