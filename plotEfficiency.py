from __future__ import print_function

import argparse
import array
import copy
import getpass
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot
#import mxnet
import multiprocessing
import numexpr
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


#matplotlib.pyplot.rc("text", usetex = True)
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{amsmath}"]
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{slashed}"]


#context = mxnet.cpu()

#username = getpass.getuser()


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


#parser.add_argument(
#    "--nEventMax",
#    help = "Number of signal and background (each) events to be used",
#    type = int,
#    required = False,
#    default = 500000,
#)

parser.add_argument(
    "--processList",
    help = "List of process names: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    nargs = "*",
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
    metavar = "PROCESSSIG",
)

parser.add_argument(
    "--extraDirSuffixList",
    help = "List of extra directory suffixes (to be added as friend trees)",
    type = str,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--plotNumList",
    help = "List of numerator plot string",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--plotDenList",
    help = "List of denominator plot string",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--cutNumList",
    help = "List of cut to be applied to the numerators",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--cutDenList",
    help = "List of cuts to be applied to the denominators",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--labelList",
    help = "List of plot labels",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--lineColorList",
    help = "List of line colors",
    type = int,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--lineStyleList",
    help = "List of line styles",
    type = int,
    nargs = "*",
    required = False,
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
    "--logX",
    help = "X-axis in log scale",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--logY",
    help = "Y-axis in log scale",
    default = False,
    action = "store_true",
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

parser.add_argument(
    "--nBinX",
    help = "Number of X-axis bins",
    type = int,
    required = True,
)

parser.add_argument(
    "--xMinDraw",
    help = "X-axis minumum for the canvas",
    type = float,
    required = True,
)

parser.add_argument(
    "--xMaxDraw",
    help = "X-axis maximum for the canvas",
    type = float,
    required = True,
)

parser.add_argument(
    "--yMin",
    help = "Y-axis minumum",
    type = float,
    required = False,
    default = 1e-5,
)

parser.add_argument(
    "--yMax",
    help = "Y-axis maximum",
    type = float,
    required = False,
    default = 1.0,
)

parser.add_argument(
    "--axisMaxDigits",
    help = "Maximum digits above whoch to use exponent notation",
    type = int,
    required = False,
    default = 3,
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
    "--title",
    help = "Plot title",
    type = str,
    required = False,
    default = " ",
)

parser.add_argument(
    "--legendPos",
    help = "Legend position",
    type = str,
    choices = ["UR", "LR", "LL", "UL"],
    required = False,
    default = "LR",
)

parser.add_argument(
    "--legendTextSize",
    help = "Legend text size",
    type = float,
    required = False,
    default = 0.04,
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


outFileName = "plots/efficiencies/%s" %(args.outFileName)

os.system("mkdir -p %s" %(outFileName[:outFileName.rfind("/")]))


l_histDetail = []


for iPlot in range(0, len(args.processList)) :
    
    process = args.processList[iPlot]
    
    plotNum = args.plotNumList[iPlot]
    plotDen = args.plotDenList[iPlot]
    
    cutNum = args.cutNumList[iPlot]
    cutDen = args.cutDenList[iPlot]
    
    
    # Read sig tree
    l_inFileName = mxnet_train_info.d_ntupleFile[process]
    
    tree = ROOT.TChain("tree")
    
    for iFile in range(0, len(l_inFileName)) :
        
        #print("Adding file: %s" %(l_inFileName[iFile]))
        tree.Add(l_inFileName[iFile])
    
    l_extraTree = []
    
    if (args.extraDirSuffixList is not None) :
        
        extraDirSuffixList = [args.extraDirSuffixList[iPlot]]
        
        for iExtra, extraDirSuffix in enumerate(extraDirSuffixList) :
            
            tree_extra = ROOT.TChain("tree")
            
            for iFile, iFileName in enumerate(l_inFileName) :
                
                iFileName_extra = "%s_%s%s" %(
                    iFileName[0: iFileName.rfind("/")],
                    extraDirSuffix,
                    iFileName[iFileName.rfind("/"):],
                )
                
                #l_inFileName_extra.extend([iFileName_extra])
                
                #print("Adding file: %s" %(iFileName_extra))
                tree_extra.Add(iFileName_extra)
            
            l_extraTree.append(tree_extra)
            
            tree.AddFriend(tree_extra)
    
    
    # Plot sig
    idx_str = "_%d"%(iPlot+1)
    
    h1_num = ROOT.TH1F("h1_num" + idx_str, "h1_num" + idx_str, args.nBinX, args.xMin, args.xMax)
    h1_den = ROOT.TH1F("h1_den" + idx_str, "h1_den" + idx_str, args.nBinX, args.xMin, args.xMax)
    
    #h1_num.SetDirectory(0)
    #h1_den.SetDirectory(0)
    
    h1_num.Sumw2()
    h1_den.Sumw2()
    
    plotStr_num = "%s >> %s" %(plotNum, h1_num.GetName())
    plotStr_den = "%s >> %s" %(plotDen, h1_den.GetName())
    
    tree.Draw(plotStr_num, cutNum)
    tree.Draw(plotStr_den, cutDen)
    
    #print(h1_num.Integral())
    #print(h1_den.Integral())
    
    h1_num.Divide(h1_den)
    
    #print(h1_num.Integral())
    
    histDetail_temp = Common.HistogramDetails()
    histDetail_temp.hist = h1_num.Clone()
    histDetail_temp.drawOption = "hist E1"
    histDetail_temp.lineColor = args.lineColorList[iPlot]
    histDetail_temp.lineWidth = 3
    histDetail_temp.lineStyle = args.lineStyleList[iPlot]
    histDetail_temp.markerSize = 0
    histDetail_temp.fillStyle = 0
    histDetail_temp.histLabel = args.labelList[iPlot]
    
    l_histDetail.append(histDetail_temp)



outFileName = "plots/efficiencies/%s" %(args.outFileName)


os.system("mkdir -p %s" %(outFileName[:outFileName.rfind("/")]))


#detailStr = "#splitline{%s}{%s}" %(args.detailSig, args.detailBkg)
#detailStr = "#splitline{%s}{%s}" %(AUC_str, detailStr)
#detailStr = "#splitline{#scale[1.75]{%s}}{%s}" %(args.detailROC, detailStr)



Common.plot1D(
    list_histDetails = l_histDetail,
    stackDrawOption = "nostack",
    title = args.title,
    titleSizeScale = 0.9,
    xTitle = args.xTitle, yTitle = args.yTitle,
    xMin = args.xMinDraw, xMax = args.xMaxDraw,
    yMin = args.yMin, yMax = args.yMax,
    logX = args.logX, logY = args.logY,
    gridX = True, gridY = True,
    nDivisionsX = args.divX,
    xTitleSizeScale = 0.85,
    yTitleSizeScale = 0.85,
    #xTitleOffset = 1.05,
    #yTitleOffset = 1.05,
    xTitleOffsetScale = 1.3,
    yTitleOffsetScale = 1.25,
    #xLabelSizeScale = 0.8,
    #yLabelSizeScale = 0.8,
    axisLabelMaxDigits = args.axisMaxDigits,
    drawLegend = True,
    #legendDrawOption = "",
    #legendNcol = 1,
    legendWidthScale = 1.0,
    legendHeightScale = 0.7,
    transparentLegend = True,
    legendTextSize = args.legendTextSize,
    legendBorderSize = 0,
    legendPos = args.legendPos,
    legendTitle = "",
    #l_extraText = [[args.detailPos[0], args.detailPos[1], detailStr]], #[[x, y, text], ...]
    outFileName = outFileName.replace(".pdf", ""),
    outFileName_suffix = "",
)

