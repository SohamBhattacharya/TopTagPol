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

ROOT.gROOT.SetBatch(1)


ROOT.gSystem.Load("HeaderFiles/CustomRootDict_cc.so")


matplotlib.pyplot.rc("text", usetex = True)
matplotlib.rcParams["text.latex.preamble"] = [
    r"\usepackage{amsmath}",
    r"\usepackage{slashed}",
]


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


parser.add_argument(
    "--nEventMax",
    help = "Number of signal and background (each) events to be used",
    type = int,
    required = False,
    default = 500000,
)

parser.add_argument(
    "--process",
    help = "process: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--plotStr",
    help = "Plot variable",
    type = str,
    required = True,
)

parser.add_argument(
    "--cutStr",
    help = "Cut",
    type = str,
    required = True,
)

parser.add_argument(
    "--xTitle",
    help = "X-axis title",
    type = str,
    required = False,
    default = "X",
)

parser.add_argument(
    "--yTitle",
    help = "Y-axis title",
    type = str,
    required = False,
    default = "Y",
)

parser.add_argument(
    "--zTitle",
    help = "Z-axis title",
    type = str,
    required = False,
    default = "Z",
)

parser.add_argument(
    "--xMin",
    help = "X-axis minumum",
    type = float,
    required = True,
)

parser.add_argument(
    "--xMax",
    help = "X-axis maximum",
    type = float,
    required = True,
)

#parser.add_argument(
#    "--nBinX",
#    help = "Number of X-axis bins",
#    type = int,
#    required = True,
#)

parser.add_argument(
    "--logX",
    help = "X-axis in log scale",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--yMin",
    help = "Y-axis minumum",
    type = float,
    required = True,
)

parser.add_argument(
    "--yMax",
    help = "Y-axis maximum",
    type = float,
    required = True,
)

#parser.add_argument(
#    "--nBinY",
#    help = "Number of Y-axis bins",
#    type = int,
#    required = True,
#)

parser.add_argument(
    "--logY",
    help = "Y-axis in log scale",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--zMin",
    help = "Z-axis minumum",
    type = float,
    required = False,
    default = 1e-5,
)

parser.add_argument(
    "--zMax",
    help = "Z-axis maximum",
    type = float,
    required = False,
    default = 1,
)

parser.add_argument(
    "--axisMaxDigits",
    help = "Maximum digits above whoch to use exponent notation",
    type = int,
    required = False,
    default = 3,
)

parser.add_argument(
    "--logZ",
    help = "Z-axis in log scale",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--divX",
    help = "X-axis divisions (list of 3 numbers)",
    type = int,
    nargs = 3,
    required = False,
    default = [5, 2, 5],
)

parser.add_argument(
    "--divY",
    help = "Y-axis divisions (list of 3 numbers)",
    type = int,
    nargs = 3,
    required = False,
    default = [5, 2, 5],
)

parser.add_argument(
    "--norm",
    help = "Normalize to this value",
    type = float,
    required = False,
    default = 1.0,
)

parser.add_argument(
    "--title",
    help = "Plot title",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--outFileName",
    help = "Output file name",
    type = str,
    required = True,
)


# Parse arguments
args = parser.parse_args()
d_args = vars(args)


# Load tree
l_inFileName = mxnet_train_info.d_ntupleFile[args.process]

tree = ROOT.TChain("tree")

for iFile in range(0, len(l_inFileName)) :
    
    tree.Add(l_inFileName[iFile])


# Create output directory
outFileName = "plots/jetImage/%s.pdf" %(args.outFileName)
outFileName_config = "plots/jetImage/%s_config.txt" %(args.outFileName)

os.system("mkdir -p %s" %(outFileName[:outFileName.rfind("/")]))


# Save the configuration
print("Saving the configuration to: %s" %(outFileName_config))

with open(outFileName_config, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")


def getImageHist(
    tree,
    varName,
    l_cutVar = [],
    cutStr = "1",
    nEvent_max = -1,
    ) :
    
    nEventSel = tree.GetEntries()
    
    l_var = []
    
    hist_sum = None
    
    eventCount = 0
    
    #nVal = int(tree.Draw(cutStr, "1", "goff"))
    #
    #a_isSelected = tree.GetV1()
    #
    #if (hasattr(a_isSelected, "SetSize")) :
    #    
    #    a_isSelected.SetSize(nVal)
    #
    #elif (hasattr(a_isSelected, "reshape")) :
    #    
    #    a_isSelected.reshape((nVal,))
    #
    #else :
    #    
    #    print("Error: cannot read entries with GetVN()")
    #    exit(1)
    
    count = -1
    
    for iEvent in range(0, nEventSel) :
        
        #eventNumber = eventList_temp.GetEntry(iEvent)
        eventNumber = iEvent
        
        #print("Event %d: \n" %(iEvent))
        
        tree.GetEntry(eventNumber)
        
        a_hist = getattr(tree, varName)
        
        nHist = len(a_hist)
        
        if (not nHist) :
            continue
        
        nVal = int(tree.Draw(cutStr, "1", "goff", 1, iEvent))
        
        if (nHist != nVal) :
            
            print("Variable: %s" %(varName))
            print("Selection: %s" %(cutStr))
            print("Size mismatch in getImageHist(...): No. of histograms (%d) not same as no. elements in selection (%d), in event %d. " %(nHist, nVal, iEvent))
            exit(1)
        
        a_isSelected = tree.GetV1()
        
        if (hasattr(a_isSelected, "SetSize")) :
            
            a_isSelected.SetSize(nVal)
        
        elif (hasattr(a_isSelected, "reshape")) :
            
            a_isSelected.reshape((nVal,))
        
        else :
            
            print("Error: cannot read entries with GetVN()")
            exit(1)
        
        for iHist in range(0, nHist) :
            
            count += 1
            
            #cutStr_eval = cutStr
            #
            #for iCutVar in range(0, len(l_cutVar)) :
            #    
            #    if (l_cutVar[iCutVar] in cutStr_eval) :
            #        
            #        cutVarVal = getattr(tree, l_cutVar[iCutVar])[iHist]
            #        
            #        cutStr_eval = cutStr_eval.replace(l_cutVar[iCutVar], str(cutVarVal))
            #
            ##print(iEvent, iHist, cutStr_eval)
            #
            #if (not eval(cutStr_eval)) :
            #    
            #    continue
            #
            ##varValue = getattr(tree, varInfo.varName)
            ##
            ##if (varInfo.varIndex >= 0) :
            ##    
            ##    varValue = varValue[varInfo.varIndex]
            ##
            ##print varValue
            ##
            ##l_var.append(varValue)
            
            #if (not a_isSelected[count]) :
            #    
            #    continue
            
            if (not a_isSelected[iHist]) :
                
                continue
            
            hist = a_hist[iHist]
            
            if (hist_sum is None) :
                
                hist_sum = hist.Clone()
                hist_sum.SetName(varName)
                hist_sum.SetTitle(varName)
            
            else :
                
                hist_sum.Add(hist)
            
            #print("\t", arr.sum())
            
            eventCount += 1
            
            print("\rGot image %d/%d." %(eventCount, nEvent_max), end = "")
            
            if (eventCount == nEvent_max) :
                
                break
        
        if (eventCount == nEvent_max) :
                
                break
    
    print("")
    print("# images: %d \n" %(eventCount))
    
    hist_sum.Scale(1.0 / eventCount)
    
    return hist_sum


# Plot
#h2_image = ROOT.TH2F("h2_image", "h2_image", args.nBinX, args.xMin, args.xMax, args.nBinY, args.yMin, args.yMax)
#
#plotStr = "%s >> %s" %(args.plotStr, args.cutStr)
#
#tree.Draw(plotStr, args.cutStr)

#h2_image.Scale(args.norm / h2_image.GetEntries())


h2_image = getImageHist(
    tree = tree,
    varName = args.plotStr,
    l_cutVar = mxnet_train_info.l_varName_common,
    cutStr = args.cutStr,
    nEvent_max = args.nEventMax,
)


histDetail = Common.HistogramDetails()
histDetail.hist = h2_image.Clone()
histDetail.drawOption = "colz"
histDetail.histTitle = args.title
#histDetail.titleSizeScale = 0.9
#histDetail.titleOffsetScale = 1.3
histDetail.xTitle = args.xTitle
histDetail.yTitle = args.yTitle
histDetail.zTitle = args.zTitle
#histDetail.xTitleSizeScale = 1.7
#histDetail.yTitleSizeScale = 1.65
#histDetail.zTitleSizeScale = 1.65
histDetail.xTitleOffsetScale = 1.25
histDetail.yTitleOffsetScale = 0.95
histDetail.zTitleOffsetScale = 1.25
#histDetail.xLabelSizeScale = 1.4
#histDetail.yLabelSizeScale = 1.4
#histDetail.zLabelSizeScale = 1.4
histDetail.xMin = args.xMin
histDetail.xMax = args.xMax
histDetail.yMin = args.yMin
histDetail.yMax = args.yMax
histDetail.zMin = args.zMin
histDetail.zMax = args.zMax
histDetail.logZ = args.logZ
histDetail.outFileName = outFileName


Common.plot2D(
    histDetail,
    palette = ROOT.kVisibleSpectrum,
    nContour = 50,
    axisLabelMaxDigits = args.axisMaxDigits,
)


outRootFileName = outFileName.replace(".pdf", ".root")
outRootFile = ROOT.TFile.Open(outRootFileName, "RECREATE")
outRootFile.cd()

h2_image.Write()

outRootFile.Close()
