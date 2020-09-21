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
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--extraDirSuffixList",
    help = "List (space separated) of extra directory suffixes (to be added as friend trees)",
    type = str,
    nargs = "*",
    required = False,
    default = None,
)

parser.add_argument(
    "--plotX",
    help = "X-axis variable",
    type = str,
    required = True,
)

parser.add_argument(
    "--plotY",
    help = "Y-axis variable",
    type = str,
    required = True,
)

parser.add_argument(
    "--cut",
    help = "Cut to be applied",
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
    required = True,
    default = 0.0,
)

parser.add_argument(
    "--yMax",
    help = "Y-axis maximum",
    type = float,
    required = True,
    default = 1.0,
)

parser.add_argument(
    "--nBinY",
    help = "Number of Y-axis bins",
    type = int,
    required = True,
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
    "--divY",
    help = "Y-axis divisions (list of 3 numbers)",
    type = int,
    nargs = 3,
    required = False,
    default = [5, 2, 5],
)

#parser.add_argument(
#    "--norm",
#    help = "Normalize to this value",
#    type = float,
#    required = False,
#    default = 1.0,
#)

parser.add_argument(
    "--title",
    help = "Plot title",
    type = str,
    required = False,
    default = "",
)

#parser.add_argument(
#    "--legendPos",
#    help = "Legend position",
#    type = str,
#    choices = ["UR", "LR", "LL", "UL"],
#    required = False,
#    default = "LR",
#)
#
#parser.add_argument(
#    "--detailStr",
#    help = "Extra details to be shown on the plot",
#    type = str,
#    required = False,
#    default = "",
#)
#
#parser.add_argument(
#    "--detailPos",
#    help = "Position of the detail (LL coordinate)",
#    type = float,
#    nargs = 2,
#    required = False,
#    default = [0.0, 0.0],
#)

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
    "--outFileName",
    help = "Output file name",
    type = str,
    required = True,
)


# Parse arguments
args = parser.parse_args()
d_args = vars(args)


l_inFileName = mxnet_train_info.d_ntupleFile[args.fileList]

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

h2_temp = ROOT.TH2F("h2_temp", "h2_temp", args.nBinX, args.xMin, args.xMax, args.nBinY, args.yMin, args.yMax)
h2_temp.Sumw2()
#h2_temp.SetDirectory(0)

drawStr = "%s : %s >> %s" %(args.plotY, args.plotX, h2_temp.GetName())

tree.Draw(drawStr, args.cut, "goff")

print(h2_temp.Integral(), h2_temp.GetEntries())


outFileName = "plots/variables2D/%s.pdf" %(args.outFileName)
outFileName_config = "plots/variables2D/%s_config.txt" %(args.outFileName)


os.system("mkdir -p %s" %(outFileName[:outFileName.rfind("/")]))


# Save the configuration

print("Saving the configuration to: %s" %(outFileName_config))

with open(outFileName_config, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")

histMin = h2_temp.GetMinimum(0)
histMax = h2_temp.GetMaximum()

# Normalize
norm = h2_temp.Integral()
h2_temp.Scale(1.0 / norm)

#print(histMin, histMax)

histDetail = Common.HistogramDetails()
histDetail.hist = h2_temp.Clone()
histDetail.drawOption = "colz"
histDetail.histTitle = args.title
histDetail.titleSizeScale = 0.9
#histDetail.titleOffsetScale = 1.3
histDetail.xTitle = args.xTitle
histDetail.yTitle = args.yTitle
histDetail.zTitle = "a.u."
#histDetail.xTitleSizeScale = 1.7
#histDetail.yTitleSizeScale = 1.65
#histDetail.zTitleSizeScale = 1.65
histDetail.xTitleOffsetScale = 1.25
histDetail.yTitleOffsetScale = 0.95
histDetail.zTitleOffsetScale = 1.25
#histDetail.xLabelSizeScale = 1.4
#histDetail.yLabelSizeScale = 1.4
#histDetail.zLabelSizeScale = 1.4
histDetail.zMin = histMin / norm
#histDetail.zMin = h2_temp.GetMaximum()
histDetail.logX = args.logX
histDetail.logY = args.logY
histDetail.logZ = args.logZ
histDetail.outFileName = outFileName

corr = h2_temp.GetCorrelationFactor()
corrStr = "Correlation #[]{#frac{Cov(x, y)}{#sigma(x)#sigma(y)}#times100} = %0.1f%%" %(corr*100)

print("Correlation factor: %0.4e" %(corr))

Common.plot2D(
    histDetail,
    l_extraText = [
        [args.printCorrPos[0], args.printCorrPos[1], corrStr],
    ]
)
