#from __future__ import print_function

import argparse
import array
import copy
import getpass
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot
import mxnet
import numpy
import os
import pprint
import scipy
import scipy.interpolate
import scipy.special
import subprocess
import tabulate
import time

#import Common
import mxnet_train_info

import multiprocessing
import ROOT


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(
    formatter_class = argparse.RawTextHelpFormatter,
    #formatter_class = argparse.ArgumentDefaultsHelpFormatter,
)


parser.add_argument(
    "--training",
    help = "Name of the training to be used: \n%s" %("\n".join(sorted(mxnet_train_info.d_info.keys()))),
    type = str,
    choices = mxnet_train_info.d_info.keys(),
    required = True,
    metavar = "TRAINING",
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
    help = "Total number of events to be stored (-ve implies all) \nDefault: %(default)d",
    type = int,
    required = False,
    default = -1,
)

parser.add_argument(
    "--inFileList",
    help = "Input files (supports multiple space-separated entries): \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    nargs = "*",
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
    metavar = "INFILELIST",
)

parser.add_argument(
    "--CNNbranchName",
    help = "Name of the output CNN branch \nDefault: %(default)s",
    type = str,
    default = "hepTop_CNN_reco",
    required = False,
)

parser.add_argument(
    "--nCPUfraction",
    help = "Fraction of the available CPUs to use \nDefault: %(default)g",
    type = float,
    required = False,
    default = 0.95,
)

parser.add_argument(
    "--replaceOld",
    help = "Replace existing files of the same name (otherwise will rename the existing output directory)",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--test",
    help = "Test run: will not create output directories or files",
    default = False,
    action = "store_true",
)

#parser.add_argument(
#    "--outFileSuffix",
#    help = "Output filename suffix (include the leading underscore if needed)",
#    type = str,
#    required = False,
#    default = "",
#)


# Parse arguments
args = parser.parse_args()
d_args = vars(args)


context = mxnet.cpu()
username = getpass.getuser()


ROOT.gSystem.Load("HeaderFiles/CustomRootDict_cc.so")

# NOTE: This is faster on the CPU as it evaluates each event one after another.
# So there's a large overhead and IO (CPU <--> GPU) bottleneck when running on the GPU
#if (username == "sobhatta") :
#    
#    print("*********************")
#    print("***** Using GPU *****")
#    print("*********************")
#    print("\n")
#    
#    context = mxnet.gpu()
#    
#    #ROOT.ROOT.EnableImplicitMT(30)


#outDir_suffix = str(args.inFiles)
#outDir_suffix = outDir_suffix.replace("l_ntupleFile_", "")

networkSymbolFile = "mxnetNetworkInfo/%s/network-symbol.json" %(args.trainingDirName)
networkParamFile = "mxnetNetworkInfo/%s/network-%04d.params" %(args.trainingDirName, args.epoch)
#outFileName_config = "plots/mxnet/%s/corr_CNN-epoch%03d_vs_%s%s_config.txt" %(args.trainingDirName, args.epoch, args.corrVarName, args.outFileSuffix)
#
#
## Save the configuration
#print("Saving the configuration to: %s" %(outFileName_config))
#
#with open(outFileName_config, "w") as configOutFile :
#    
#    configOutFile.write(pprint.pformat(d_args, width = 1))
#    configOutFile.write("\n")
#
#print("\n")


l_inFileName = []

for iEle, ele in enumerate(args.inFileList) :
    
    l_inFileName.extend(mxnet_train_info.d_ntupleFile[ele])


l_varStr = mxnet_train_info.d_info[args.training]["layerNames"]
#l_cutVar = mxnet_train_info.d_info[args.training]["varNames"]

nVar = len(l_varStr)


def createAndFillTree(
    inFileName,
    outFileName,
    CNNbranchName,
    nEventMax = -1,
    printProgress = False,
    test = False,
    ) :
    
    neuralNetwork = mxnet.gluon.nn.SymbolBlock.imports(
        symbol_file = networkSymbolFile,
        param_file  = networkParamFile,
        input_names = ["data"],
        ctx = context,
    )
    
    inTree = ROOT.TChain("tree")
    inTree.Add(inFileName)
    
    if (not test) :
        
        outFile = ROOT.TFile.Open(outFileName, "RECREATE")
    
    outTree = ROOT.TTree("tree", "tree")
    
    v_CNN = ROOT.std.vector("double")()
    outTree.Branch(CNNbranchName, v_CNN)
    
    inTree.SetBranchStatus("*", 0)
    
    for iVar in range(0, nVar) :
        
        varName = l_varStr[iVar]
        
        inTree.SetBranchStatus(varName, 1)
    
    
    if (nEventMax < 0) :
        
        nEventMax = inTree.GetEntries()
    
    else :
        
        nEventMax = min(nEventMax, inTree.GetEntries())
    
    
    #inTree.Print()
    
    for iEvent in range(0, nEventMax) :
        
        inTree.GetEntry(iEvent)
        
        a_data = None
        
        v_CNN.clear()
        
        nRow = -1
        nCol = -1
        
        for iVar in range(0, nVar) :
            
            varName = l_varStr[iVar]
            
            a_hist = getattr(inTree, varName)
            
            nHist = len(a_hist)
            
            for iHist in range(0, nHist) :
                
                hist = a_hist[iHist]
                
                nBinX = hist.GetNbinsX()
                nBinY = hist.GetNbinsY()
                
                if (a_data is None) :
                    
                    nRow = nBinY
                    nCol = nBinX
                    
                    a_data = mxnet.ndarray.zeros(shape = (nHist, nVar, nRow, nCol), dtype = "float32", ctx = context)
                
                a_data_hist = numpy.array(hist)
                a_data_hist.shape = (nBinY+2, nBinX+2)
                
                a_data[iHist, iVar, :, :] = a_data_hist[1: -1, 1: -1]
                
                #for iBinX in range(0, nBinX) :
                #    
                #    for iBinY in range(0, nBinY) :
                #        
                #        binContent = hist.GetBinContent(iBinX+1, iBinY+1)
                #        
                #        a_data[iHist, iVar, iBinY, iBinX] = binContent
        
        # Get CNN classifier
        a_CNNclass = numpy.empty(0)
        
        if (a_data is not None) :
            
            a_CNNclass = neuralNetwork(a_data).asnumpy().flatten()
        
        for CNNclass in a_CNNclass :
            
            v_CNN.push_back(CNNclass)
        
        
        #print(a_CNNclass)
        
        outTree.Fill()
        
        
        if (printProgress) :
            
            print("\rProcessed %d/%d events." %(iEvent+1, nEventMax), end = "")
    
    
    if (not test) :
        
        #print("Starting to write output file.")
        outFile.cd()
        outTree.Write()
        outFile.Close()
        #print("Finished writing output file.")
    
    #inTree.Delete()
    
    return 0


nCPU = min(int(args.nCPUfraction*multiprocessing.cpu_count()), len(l_inFileName))
#nCPU = min(multiprocessing.cpu_count(), 14)

pool = multiprocessing.Pool(processes = nCPU)
#pool = multiprocessing.Pool(processes = 1, maxtasksperchild = 1)
l_job = []


l_renamedDir = []

#l_inFileName = [l_inFileName[0]]


for iFile, inFileName in enumerate(l_inFileName) :
    
    #if (iFile > 0) :
    #    
    #    break
    
    outDir = inFileName[0: inFileName.rfind("/")]
    outDir = "%s_%s" %(outDir, args.trainingDirName)
    
    outFileName = inFileName[inFileName.rfind("/")+1:]
    outFileName = "%s/%s" %(outDir, outFileName)
    
    print("\n")
    print("*"*50)
    print("Job %d/%d." %(iFile+1, len(l_inFileName)))
    print("Input file:  %s" %(inFileName))
    print("Output file: %s" %(outFileName))
    print("*"*50)
    
    if (not args.test and not args.replaceOld) :
        
        if (os.path.isdir(outDir) and outDir not in l_renamedDir) :
            
            outDir_old = subprocess.check_output(["date", "+%Y-%m-%d_%H-%M-%S", "-r", outDir]).strip()
            outDir_old = outDir_old.decode("UTF-8") # Convert from bytes to string
            outDir_old = "%s_%s" %(outDir, outDir_old)
            
            cmdStr = "mv %s %s" %(outDir, outDir_old)
            
            print("Output directory exists. Renaming it:")
            print(cmdStr)
            print("")
            
            cmdReturn = os.system(cmdStr)
            
            l_renamedDir.append(outDir)
        
        elif (not os.path.isdir(outDir)) :
            
            l_renamedDir.append(outDir)
        
        os.system("mkdir -p %s" %(outDir))
    
    
    CNNbranchName = args.CNNbranchName
    #CNNbranchName = "%s_epoch%d" %(args.CNNbranchName, args.epoch)
    
    job = pool.apply_async(
        createAndFillTree,
        (),
        dict(
            inFileName = inFileName,
            outFileName = outFileName,
            CNNbranchName = CNNbranchName,
            nEventMax = args.nEventMax,
            printProgress = (iFile == len(l_inFileName)-1 or (iFile+1)%nCPU == 0),
            test = args.test,
        ),
    )
    
    l_job.append(job)


pool.close()
pool.join()


for iJob, job in enumerate(l_job) :
    
    job.get()
