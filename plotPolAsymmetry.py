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


#pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


parser.add_argument(
    "--inputFiles",
    help = "List of input files: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    nargs = "*",
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--extraDirSuffixes",
    help = "List of extra directory suffixes (to be added as friend trees)",
    type = str,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--nEventMaxs",
    help = "Number of signal and background (each) events to be used",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--asymVars",
    help = "List of asymmetry variables to be used",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--asymVarLimits",
    help = "List (space separated pairs of lwr and upr) of asymmetry variable limits to be used",
    type = float,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--asymVarNdivs",
    help = "List of the number of divisions of the asymmetry variables",
    type = float,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--cuts",
    help = "List of selections",
    type = str,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--comparisons",
    help = "List of comparisons to use for the variable cut (>, <)",
    type = str,
    nargs = "*",
    required = True,
    choices = [">", "<"],
)

parser.add_argument(
    "--xTitle",
    help = "X-axis title",
    type = str,
    required = False,
    default = "Signal efficiency",
)

parser.add_argument(
    "--yTitle",
    help = "Y-axis title",
    type = str,
    required = False,
    default = "Background efficiency",
)

parser.add_argument(
    "--xMin",
    help = "X-axis minumum",
    type = float,
    required = False,
    default = 0,
)

parser.add_argument(
    "--xMax",
    help = "X-axis maximum",
    type = float,
    required = False,
    default = 1.0,
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
    "--logY",
    help = "Y-axis in log scale",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--nDivX",
    help = "X-axis divisions",
    type = int,
    nargs = 3,
    required = False,
    default = [5, 2, 5],
)

parser.add_argument(
    "--nDivY",
    help = "Y-axis divisions",
    type = int,
    nargs = 3,
    required = False,
    default = [5, 2, 5],
)

parser.add_argument(
    "--lineColors",
    help = "Line colors",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--lineStyles",
    help = "Line styles",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--labels",
    help = "List of plot labels",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--diffs",
    help = "List (of indices) of asymmetry differences. Example: 0 1 2 1 (this will plot 0-1 and 2-1)",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--diffColors",
    help = "Asymmetry difference line colors",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--diffStyles",
    help = "Asymmetry difference line styles",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--diffLabels",
    help = "List of labels for the asymmetry differences",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--legendPos",
    help = "Plot labels",
    type = str,
    required = False,
    default = "UR",
    choices = ["UR", "LR", "LL", "UL"],
)

parser.add_argument(
    "--legendTextSize",
    help = "Legent text size",
    type = float,
    required = False,
    default = 0.03,
)

parser.add_argument(
    "--title",
    help = "Plot title",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--outDir",
    help = "Output directory",
    type = str,
    required = True,
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


outFileName = "plots/asymmetry/%s" %(args.outFileName)
outFileName_config = "plots/asymmetry/%s_config.txt" %(args.outFileName)


os.system("mkdir -p %s" %(outFileName[:outFileName.rfind("/")]))


# Save the configuration

print("Saving the configuration to: %s" %(outFileName_config))

with open(outFileName_config, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")


def getAsymmetry(arr, val, comparison) :
    
    count_upr = float(sum(arr > val))
    count_lwr = float(sum(arr < val))
    
    count_tot = count_lwr + count_upr
    
    asym = 0
    
    if (comparison == ">") :
        
        asym = (count_upr - count_lwr) / count_tot
    
    elif (comparison == "<") :
        
        asym = (count_lwr - count_upr) / count_tot
    
    else :
        
        print("Error in getAsymmetry(...): Invalid comparison \"%s\"" %(comparison))
    
    return asym


l_histDetail = []

for iPlot in range(0, len(args.inputFiles)) :
    
    l_inFileName = mxnet_train_info.d_ntupleFile[args.inputFiles[iPlot]]
    
    tree = ROOT.TChain("tree")
    
    for iFile in range(0, len(l_inFileName)) :
        
        tree.Add(l_inFileName[iFile])
    
    
    l_extraTree = []
    
    
    if (len(args.extraDirSuffixes[iPlot])) :
        
        extraDirSuffixes = args.extraDirSuffixes[iPlot].strip().split(":")
        
        for iExtra, extraDirSuffix in enumerate(extraDirSuffixes) :
            
            if (not len(extraDirSuffix)) :
                
                continue
            
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
            
            friendAlias = extraDirSuffix.replace("-", "_")
            
            tree.AddFriend(tree_extra, friendAlias)
    
    
    nEvent_tree = tree.GetEntries()
    
    
    a_var = Common.getArrayFromTBranch(
        tree = tree,
        varName = args.asymVars[iPlot],
        l_cutVar = [],
        cutStr = args.cuts[iPlot],
        nSel_max = args.nEventMaxs[iPlot],
    )
    
    varMin = args.asymVarLimits[2*iPlot]
    varMax = args.asymVarLimits[2*iPlot+1]
    
    var_nDiv = args.asymVarNdivs[iPlot]
    
    var_stepSize = float(varMax-varMin) / var_nDiv
    
    l_varCut = numpy.arange(varMin, varMax, var_stepSize)
    #print(l_varCut)
    
    if (l_varCut[0] != varMin) :
        
        l_varCut = numpy.insert(l_varCut, 0, varMin)
    
    if (l_varCut[-1] != varMax) :
        
        l_varCut = numpy.insert(l_varCut, len(l_varCut), varMax)
    
    nCPU = min(multiprocessing.cpu_count(), len(l_varCut))
    
    pool = multiprocessing.Pool(processes = nCPU)
    
    l_job = []
    
    nEventTot = a_var.shape[0]
    
    print("\n")
    print("Calculating asymmetries. \n")
    
    
    for iCut, cutVar in enumerate(l_varCut) :
        
        job = pool.apply_async(
            getAsymmetry,
            (),
            dict(
                arr = a_var,
                val = cutVar,
                comparison = args.comparisons[iPlot],
            ),
        )
        
        l_job.append(job)
    
    
    pool.close()
    pool.join()
    
    
    l_asym = numpy.zeros(len(l_varCut))
    
    for iJob in range(0, len(l_job)) :
        
        l_asym[iJob] = l_job[iJob].get()
        
        
        if (iJob == 0 or iJob == len(l_job)-1 or not (iJob+1)%30) :
        
            print(
                "%d/%d: %0.8f: "
                "asymmetry %0.8f, "
                "\n" %(
                
                iJob+1, len(l_varCut),
                l_varCut[iJob],
                l_asym[iJob],
            ))
    
    
    #print(l_varCut)
    #print(l_asym)
    
    
    #################### Plot Asymmetry ####################
    
    a_x = array.array("f", l_varCut)
    a_y = array.array("f", l_asym)
    
    #print(list(zip(a_x, a_y)))
    
    gr = ROOT.TGraph(len(a_x), a_x, a_y)
    gr.SetName("graph_%d" %(iPlot+1))
    h1 = Common.TGraphToTH1(graph = gr, setError = False)
    
    #for iBin in range(1, h1.GetNbinsX()+1) :
    #    
    #    print(iBin, h1.GetBinCenter(iBin), h1.GetBinContent(iBin))
    
    #h1.GetXaxis().SetRangeUser(varMin, varMax)
    h1.SetMinimum(args.yMin)
    h1.SetMaximum(args.yMax)
    
    histDetail = Common.HistogramDetails()
    histDetail.hist = h1.Clone()
    histDetail.drawOption = "L"
    histDetail.lineColor = args.lineColors[iPlot]
    histDetail.lineStyle = args.lineStyles[iPlot]
    histDetail.lineWidth = 3
    histDetail.markerSize = 0
    histDetail.fillStyle = 0
    histDetail.histLabel = "%s" %(args.labels[iPlot])
    histDetail.histTitle = args.title
    
    l_histDetail.append(histDetail)
    
    
    print("\n")


# Asymmetry differences
for iDiff in range(0, int(len(args.diffs)/2)) :
    
    idx1 = args.diffs[2*iDiff]
    idx2 = args.diffs[2*iDiff+1]
    
    histDetail = Common.HistogramDetails()
    histDetail.hist = l_histDetail[idx1].hist.Clone()
    histDetail.hist.Add(l_histDetail[idx2].hist, -1)
    histDetail.drawOption = "L"
    histDetail.lineColor = args.diffColors[iDiff]
    histDetail.lineStyle = args.diffStyles[iDiff]
    histDetail.lineWidth = 3
    histDetail.markerSize = 0
    histDetail.fillStyle = 0
    histDetail.histLabel = "%s" %(args.diffLabels[iDiff])
    
    l_histDetail.append(histDetail)


Common.plot1D(
    list_histDetails = l_histDetail,
    stackDrawOption = "nostack",
    title = args.title,
    titleSizeScale = 0.9,
    xTitle = args.xTitle,
    yTitle = args.yTitle,
    xTitleSizeScale = 0.75,
    yTitleSizeScale = 0.75,
    xTitleOffsetScale = 1.4,
    yTitleOffsetScale = 1.35,
    xMin = args.xMin, xMax = args.xMax,
    yMin = args.yMin, yMax = args.yMax,
    logX = False, logY = args.logY,
    gridX = True, gridY = True,
    nDivisionsX = args.nDivX,
    nDivisionsY = args.nDivY,
    #xTitleSizeScale = 1.0, yTitleSizeScale = 1.0,
    #xTitleOffset = 1.0, yTitleOffset = 1.0,
    #xLabelSizeScale = 1.0, yLabelSizeScale = 1.0,
    #centerLabelsX = True, centerLabelsY = True,
    drawLegend = True,
    #legendDrawOption = "",
    #legendNcol = 1,
    #legendWidthScale = 1,
    #legendHeightScale = 1,
    transparentLegend = True,
    legendTextSize = args.legendTextSize,
    legendBorderSize = 0,
    legendPos = args.legendPos,
    legendTitle = "",
    #l_extraText = [[args.detailPos[0], args.detailPos[1], detailStr]], #[[x, y, text], ...]
    outFileName = outFileName.replace(".pdf", ""),
    outFileName_suffix = "",
)
