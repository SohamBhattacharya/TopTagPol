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


parser.add_argument(
    "--nEventMax",
    help = "Number of signal and background (each) events to be used",
    type = int,
    required = False,
    default = 500000,
)

parser.add_argument(
    "--fileList",
    help = "List of files: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    nargs = "*",
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--extraDirSuffixList",
    help = "List (space separated) of extra directory suffixes (to be added as friend trees)",
    type = str,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--plotList",
    help = "List of variables to be plotted",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--cutList",
    help = "List of cuts",
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
    "--legendPos",
    help = "Legend position",
    type = str,
    choices = ["UR", "LR", "LL", "UL"],
    required = False,
    default = "LR",
)

parser.add_argument(
    "--detailStr",
    help = "Extra details to be shown on the plot",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--detailPos",
    help = "Position of the detail (LL coordinate)",
    type = float,
    nargs = 2,
    required = False,
    default = [0.0, 0.0],
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


if (args.lineStyleList is None) :
    
    args.lineStyleList = [1] * len(args.fileList)

if (args.lineColorList is None) :
    
    args.lineColorList = list(range(1, len(args.fileList)+1))


l_len = [
    len(args.fileList),
    len(args.plotList),
    len(args.cutList),
    len(args.labelList),
    len(args.lineStyleList),
    len(args.lineColorList),
]


if (len(numpy.where(numpy.array(l_len) != l_len[0])[0])) :
    
    print("Error: Unequal number of entries.")
    exit(1)


l_cutVar = [
    "hepTop_pT_reco",
    "hepTop_genHadTop_deltaR_reco",
    "hepTop_isMayBeTop_reco",
]


nPlot = l_len[0]


#l_tree = []
#l_a_var = []


l_histDetail = []


for iPlot in range(0, nPlot) :
    
    l_inFileName = mxnet_train_info.d_ntupleFile[args.fileList[iPlot]]
    
    tree = ROOT.TChain("tree")
    
    for iFile in range(0, len(l_inFileName)) :
        
        tree.Add(l_inFileName[iFile])
    
    
    l_extraTree = []
    
    
    if (args.extraDirSuffixList is not None) :
        
        for iExtra, extraDirSuffix in enumerate(args.extraDirSuffixList) :
            
            tree_extra = ROOT.TChain("tree")
            
            for iFile, iFileName in enumerate(l_inFileName) :
                
                iFileName_extra = "%s_%s%s" %(
                    iFileName[0: iFileName.rfind("/")],
                    extraDirSuffix,
                    iFileName[iFileName.rfind("/"):],
                )
                
                #l_inFileName_extra.extend([iFileName_extra])
                
                tree_extra.Add(iFileName_extra)
            
            l_extraTree.append(tree_extra)
            
            tree.AddFriend(tree_extra)
    
    
    #l_tree.append(tree)
    
    nEvent_tree = tree.GetEntries()
    
    #a_var = Common.getArrayFromTBranch(
    #    tree = tree,
    #    varName = args.varList[iPlot],
    #    l_cutVar = l_cutVar,
    #    cutStr = args.cutList[iPlot],
    #    nSel_max = args.nEventMax,
    #)
    #
    #l_a_var.append(a_var)
    
    h1_temp = ROOT.TH1F("h1_temp", "h1_temp", args.nBinX, args.xMin, args.xMax)
    h1_temp.Sumw2()
    #h1_temp.SetDirectory(0)
    
    drawStr = "%s >> %s" %(args.plotList[iPlot], h1_temp.GetName())
    
    tree.Draw(drawStr, args.cutList[iPlot])
    
    print(h1_temp.Integral(), h1_temp.GetEntries())
    
    #time.sleep(10000)
    
    #h1_temp.Scale(args.norm / h1_temp.Integral())
    h1_temp.Scale(args.norm / h1_temp.GetEntries())
    
    histDetail_temp = Common.HistogramDetails()
    histDetail_temp.hist = h1_temp.Clone()
    histDetail_temp.drawOption = "hist"
    histDetail_temp.lineColor = args.lineColorList[iPlot]
    histDetail_temp.lineWidth = 3
    histDetail_temp.lineStyle = args.lineStyleList[iPlot]
    histDetail_temp.markerSize = 0
    histDetail_temp.fillStyle = 0
    histDetail_temp.histLabel = args.labelList[iPlot]
    
    l_histDetail.append(histDetail_temp)
    
    
    #tree.Close()


outFileName = "plots/variables/%s" %(args.outFileName)
outFileName_config = "plots/variables/%s_config.txt" %(args.outFileName)


os.system("mkdir -p %s" %(outFileName[:outFileName.rfind("/")]))


# Save the configuration

print("Saving the configuration to: %s" %(outFileName_config))

with open(outFileName_config, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")


#detailStr = "#splitline{%s}{%s}" %(args.detailSig, args.detailBkg)
#detailStr = "#splitline{%s}{%s}" %(AUC_str, detailStr)
#detailStr = "#splitline{#scale[1.75]{%s}}{%s}" %(args.detailROC, detailStr)



Common.plot1D(
    list_histDetails = l_histDetail,
    stackDrawOption = "nostack",
    title = args.title,
    titleSizeScale = 0.9,
    xTitle = args.xTitle, yTitle = args.yTitle,
    xMin = args.xMin, xMax = args.xMax,
    yMin = args.yMin, yMax = args.yMax,
    logX = args.logX, logY = args.logY,
    gridX = True, gridY = True,
    nDivisionsX = args.divX,
    #xTitleSizeScale = 1.0, yTitleSizeScale = 1.0,
    #xTitleOffset = 1.0, yTitleOffset = 1.0,
    #xLabelSizeScale = 1.0, yLabelSizeScale = 1.0,
    #centerLabelsX = True, centerLabelsY = True,
    axisLabelMaxDigits = args.axisMaxDigits,
    drawLegend = True,
    #legendDrawOption = "",
    #legendNcol = 1,
    #legendWidthScale = 1,
    #legendHeightScale = 0.7,
    transparentLegend = True,
    legendTextSize = 0.03,
    legendBorderSize = 0,
    legendPos = args.legendPos,
    legendTitle = "",
    #l_extraText = [[args.detailPos[0], args.detailPos[1], detailStr]], #[[x, y, text], ...]
    outFileName = outFileName.replace(".pdf", ""),
    outFileName_suffix = "",
)
