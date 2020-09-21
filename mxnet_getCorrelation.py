from __future__ import print_function

import argparse
import array
import copy
import getpass
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot
import mxnet
import numpy
import os
import pprint
import scipy
import scipy.interpolate
import scipy.special
import tabulate
import time

import Common
import mxnet_train_info

import ROOT


import tdrstyle
tdrstyle.setTDRStyle()


ROOT.gStyle.SetOptStat(0)
#ROOT.gStyle.SetOptStat(111111111)


matplotlib.pyplot.rc("text", usetex = True)
matplotlib.rcParams["text.latex.preamble"] = [
    r"\usepackage{amsmath}",
    r"\usepackage{slashed}",
]


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


parser.add_argument(
    "--training",
    help = "Name of the training to be used",
    type = str,
    required = True,
)

parser.add_argument(
    "--trainingDirName",
    help = "Training directory name",
    type = str,
    required = True,
)

parser.add_argument(
    "--epoch",
    help = "Result afer which epoch to be used",
    type = int,
    required = True,
)

parser.add_argument(
    "--nEventMax",
    help = "Number of signal and background (each) events to be used",
    type = int,
    required = False,
    default = 500000,
)

parser.add_argument(
    "--splitEvery",
    help = "Load how many images per (multiprocessing) process",
    type = int,
    required = False,
    default = 20000,
)

parser.add_argument(
    "--sigFiles",
    help = "Signal files: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--bkgFiles",
    help = "Background files: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--corrVarName",
    help = "Correlation of the CNN classifier w.r.t. this variable",
    type = str,
    required = True,
)

parser.add_argument(
    "--corrVarRange",
    help = "Range of the variable. Syntax: --corrVarRange [lower] [upper]",
    nargs = 2,
    type = float,
    required = True,
)

parser.add_argument(
    "--corrVarNbin",
    help = "No. of bins for the varibale",
    type = int,
    required = True,
)

parser.add_argument(
    "--corrVarLatex",
    help = "Name of the variable in (ROOT) latex",
    type = str,
    required = True,
)

parser.add_argument(
    "--extraCutSig",
    help = "Extra selection on signal",
    type = str,
    required = False,
    default = "1"
)

parser.add_argument(
    "--extraCutBkg",
    help = "Extra selection on background",
    type = str,
    required = False,
    default = "1"
)

parser.add_argument(
    "--titleSig",
    help = "Plot title for signal",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--titleBkg",
    help = "Plot title for background",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--printCorrPos",
    help = "Position where the correlation value is to be printed. Syntax: --printCorrPos [x] [y]",
    nargs = 2,
    type = float,
    required = True,
)

parser.add_argument(
    "--logZ",
    help = "Z-axis in log scale",
    default = False,
    action = "store_true",
)


parser.add_argument(
    "--outFileSuffix",
    help = "Output filename suffix (include the leading underscore if needed)",
    type = str,
    required = False,
    default = "",
)


# Parse arguments
args = parser.parse_args()
d_args = vars(args)


context = mxnet.cpu()
username = getpass.getuser()

if (username == "sobhatta") :
    
    print("*********************")
    print("***** Using GPU *****")
    print("*********************")
    print("\n")
    
    context = mxnet.gpu()
    
    #ROOT.ROOT.EnableImplicitMT(30)


l_inFileName_sig = mxnet_train_info.d_ntupleFile[args.sigFiles]
l_inFileName_bkg = mxnet_train_info.d_ntupleFile[args.bkgFiles]

tree_sig = ROOT.TChain("tree")
tree_bkg = ROOT.TChain("tree")

for iFile in range(0, len(l_inFileName_sig)) :
    
    tree_sig.Add(l_inFileName_sig[iFile])

for iFile in range(0, len(l_inFileName_bkg)) :
    
    tree_bkg.Add(l_inFileName_bkg[iFile])

nEvent_tree_sig = tree_sig.GetEntries()
nEvent_tree_bkg = tree_bkg.GetEntries()

l_varStr = mxnet_train_info.d_info[args.training]["layerNames"]
l_cutVar = mxnet_train_info.d_info[args.training]["varNames"]

nVar = len(l_varStr)

cutStr_sig = "(%s) and %s" %(mxnet_train_info.d_info[args.training]["cutStr_sig"], args.extraCutSig)
cutStr_bkg = "(%s) and %s" %(mxnet_train_info.d_info[args.training]["cutStr_bkg"], args.extraCutBkg)


d_imageInfo = Common.getVarInfoFromTree(
    l_varStr = l_varStr,
    tree_sig = tree_sig,
    tree_bkg = tree_bkg,
    l_cutVar = l_cutVar,
    cutStr_sig = cutStr_sig,
    cutStr_bkg = cutStr_bkg,
    nEventTotal_sig = args.nEventMax,
    nEventTotal_bkg = args.nEventMax,
    splitEvery = args.splitEvery,
    #nCPUfraction = args.nCPUfraction,
)


a_var_sig = Common.getArrayFromTBranch(
    tree = tree_sig,
    varName = args.corrVarName,
    l_cutVar = l_cutVar,
    cutStr = cutStr_sig,
    nSel_max = args.nEventMax,
)

a_var_bkg = Common.getArrayFromTBranch(
    tree = tree_bkg,
    varName = args.corrVarName,
    l_cutVar = l_cutVar,
    cutStr = cutStr_bkg,
    nSel_max = args.nEventMax,
)


sigFiles_suffix = str(args.sigFiles)
sigFiles_suffix = sigFiles_suffix.replace("l_ntupleFile_", "")

bkgFiles_suffix = str(args.bkgFiles)
bkgFiles_suffix = bkgFiles_suffix.replace("l_ntupleFile_", "")


networkSymbolFile = "mxnetNetworkInfo/%s/network-symbol.json" %(args.trainingDirName)
networkParamFile = "mxnetNetworkInfo/%s/network-%04d.params" %(args.trainingDirName, args.epoch)
outFileName_corr_sig = "plots/mxnet/%s/corr_CNN-epoch%03d_vs_%s_%s%s.pdf" %(args.trainingDirName, args.epoch, args.corrVarName, sigFiles_suffix, args.outFileSuffix)
outFileName_corr_bkg = "plots/mxnet/%s/corr_CNN-epoch%03d_vs_%s_%s%s.pdf" %(args.trainingDirName, args.epoch, args.corrVarName, bkgFiles_suffix, args.outFileSuffix)
outFileName_config = "plots/mxnet/%s/corr_CNN-epoch%03d_vs_%s%s_config.txt" %(args.trainingDirName, args.epoch, args.corrVarName, args.outFileSuffix)


# Save the configuration
print("Saving the configuration to: %s" %(outFileName_config))

with open(outFileName_config, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")


neuralNetwork = mxnet.gluon.nn.SymbolBlock.imports(
    symbol_file = networkSymbolFile,
    param_file  = networkParamFile,
    input_names = ["data"],
    ctx = context,
)


l_data_sig = []
l_data_bkg = []

l_data = []

nRow = d_imageInfo[l_varStr[0]].a_sig[0].shape[0]
nCol = d_imageInfo[l_varStr[0]].a_sig[0].shape[1]

a_data_sig = numpy.zeros((d_imageInfo[l_varStr[0]].a_sig.shape[0], nVar, nRow, nCol))
a_data_bkg = numpy.zeros((d_imageInfo[l_varStr[0]].a_bkg.shape[0], nVar, nRow, nCol))


for iVar in range(0, nVar) :
    
    varStr = l_varStr[iVar]
    
    varInfo = d_imageInfo[varStr]
    
    a_data_sig[:, iVar, :, :] = varInfo.a_sig
    print(varInfo.a_sig.shape)
    
    # Free memory
    varInfo.a_sig = None
    
    a_data_bkg[:, iVar, :, :] = varInfo.a_bkg
    print(varInfo.a_bkg.shape)
    
    # Free memory
    varInfo.a_bkg = None

print(a_data_sig.shape)
print(a_data_bkg.shape)


pred_sig = []
pred_bkg = []

batchDataSet_sig = mxnet.gluon.data.DataLoader(
    a_data_sig, batch_size = 100, shuffle = False, num_workers = 4
)

batchDataSet_bkg = mxnet.gluon.data.DataLoader(
    a_data_bkg, batch_size = 100, shuffle = False, num_workers = 4
)


# Get sig prediction
for iBatch, data in enumerate(batchDataSet_sig):
    
    data = data.as_in_context(context).astype("float32")
    
    pred = neuralNetwork(data).asnumpy().flatten()
    
    pred_sig.extend(pred)


# Get bkg prediction
for iBatch, data in enumerate(batchDataSet_bkg):
    
    data = data.as_in_context(context).astype("float32")
    
    pred = neuralNetwork(data).asnumpy().flatten()
    
    pred_bkg.extend(pred)


pred_sig = numpy.array(pred_sig)
pred_bkg = numpy.array(pred_bkg)


#print(pred_sig.shape)
#print(pred_bkg.shape)
#print(a_var_sig.shape)
#print(a_var_bkg.shape)


##### Signal #####
ROOT.gStyle.cd()
h2_corr_sig = ROOT.TH2F("h2_corr_sig", "h2_corr_sig", args.corrVarNbin, args.corrVarRange[0], args.corrVarRange[1], 200, 0.0, 1.0)

h2_corr_sig.SetTitle(args.titleSig)

for iEle in range(0, pred_sig.shape[0]) :
    
    h2_corr_sig.Fill(
        a_var_sig[iEle],
        pred_sig[iEle],
    )

# Normalize
h2_corr_sig.Scale(1.0/h2_corr_sig.Integral())


histDetail_sig = Common.HistogramDetails()
histDetail_sig.hist = h2_corr_sig.Clone()
histDetail_sig.drawOption = "colz"
histDetail_sig.histTitle = args.titleSig
histDetail_sig.titleSizeScale = 0.9
#histDetail_sig.titleOffsetScale = 1.3
histDetail_sig.xTitle = args.corrVarLatex
histDetail_sig.yTitle = "CNN classifier"
histDetail_sig.zTitle = "a.u."
#histDetail_sig.xTitleSizeScale = 1.7
#histDetail_sig.yTitleSizeScale = 1.65
#histDetail_sig.zTitleSizeScale = 1.65
histDetail_sig.xTitleOffsetScale = 1.25
histDetail_sig.yTitleOffsetScale = 0.95
histDetail_sig.zTitleOffsetScale = 1.25
#histDetail_sig.xLabelSizeScale = 1.4
#histDetail_sig.yLabelSizeScale = 1.4
#histDetail_sig.zLabelSizeScale = 1.4
histDetail_sig.logZ = args.logZ
histDetail_sig.outFileName = outFileName_corr_sig

corr_sig = h2_corr_sig.GetCorrelationFactor()
corrStr_sig = "Correlation #[]{#frac{Cov(x, y)}{#sigma(x)#sigma(y)}#times100} = %0.1f%%" %(corr_sig*100)

print("Correlation factor: %0.4e" %(corr_sig))

Common.plot2D(
    histDetail_sig,
    l_extraText = [
        [args.printCorrPos[0], args.printCorrPos[1], corrStr_sig],
    ]
)


##### Background #####
ROOT.gStyle.cd()
h2_corr_bkg = ROOT.TH2F("h2_corr_bkg", "h2_corr_bkg", args.corrVarNbin, args.corrVarRange[0], args.corrVarRange[1], 200, 0.0, 1.0)

h2_corr_bkg.SetTitle(args.titleBkg)

for iEle in range(0, pred_bkg.shape[0]) :
    
    h2_corr_bkg.Fill(
        a_var_bkg[iEle],
        pred_bkg[iEle],
    )

# Normalize
h2_corr_bkg.Scale(1.0/h2_corr_bkg.Integral())


histDetail_bkg = Common.HistogramDetails()
histDetail_bkg.hist = h2_corr_bkg.Clone()
histDetail_bkg.drawOption = "colz"
histDetail_bkg.histTitle = args.titleBkg
histDetail_bkg.titleSizeScale = 0.9
#histDetail_bkg.titleOffsetScale = 1.3
histDetail_bkg.xTitle = args.corrVarLatex
histDetail_bkg.yTitle = "CNN classifier"
histDetail_bkg.zTitle = "a.u."
#histDetail_bkg.xTitleSizeScale = 1.7
#histDetail_bkg.yTitleSizeScale = 1.65
#histDetail_bkg.zTitleSizeScale = 1.65
histDetail_bkg.xTitleOffsetScale = 1.25
histDetail_bkg.yTitleOffsetScale = 0.95
histDetail_bkg.zTitleOffsetScale = 1.25
#histDetail_bkg.xLabelSizeScale = 1.4
#histDetail_bkg.yLabelSizeScale = 1.4
#histDetail_bkg.zLabelSizeScale = 1.4
histDetail_bkg.logZ = args.logZ
histDetail_bkg.outFileName = outFileName_corr_bkg

corr_bkg = h2_corr_bkg.GetCorrelationFactor()
corrStr_bkg = "Correlation #[]{#frac{Cov(x, y)}{#sigma(x)#sigma(y)}#times100} = %0.1f%%" %(corr_bkg*100)

print("Correlation factor: %0.4e" %(corr_bkg))

Common.plot2D(
    histDetail_bkg,
    l_extraText = [
        [args.printCorrPos[0], args.printCorrPos[1], corrStr_bkg],
    ]
)

