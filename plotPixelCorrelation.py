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


ROOT.gSystem.Load("HeaderFiles/CustomRootDict_cc.so")


#matplotlib.pyplot.rc("text", usetex = True)
#matplotlib.rcParams["text.latex.preamble"] = [
#    r"\usepackage{amsmath}",
#    r"\usepackage{slashed}",
#]


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
    "--processSuffix",
    help = "suffix to be added to the process name: ttbar-tj --> ttbar-tj\"_noSD\"",
    type = str,
    required = False,
    default = ""
)

parser.add_argument(
    "--extraDirSuffixes",
    help = "List of extra directory suffixes (to be added as friend trees)",
    type = str,
    nargs = "*",
    required = False,
    default = None,
)

parser.add_argument(
    "--imageHistName",
    help = "Image hitogram name",
    type = str,
    required = True,
)

parser.add_argument(
    "--corrVar",
    help = "Correlation variable",
    type = str,
    required = True,
)

parser.add_argument(
    "--pixelScaleVar",
    help = "Scale each pixel with this variable/value",
    type = str,
    required = False,
    default = None,
)

parser.add_argument(
    "--cutStr",
    help = "Cut",
    type = str,
    required = True,
)

parser.add_argument(
    "--cutVars",
    help = "List of the cut variables",
    type = str,
    nargs = "*",
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

l_extraTree = []

for iFile in range(0, len(l_inFileName)) :
    
    idx = l_inFileName[iFile].rfind("/")
    
    inFileName = l_inFileName[iFile]
    
    inFileName = "%s%s%s" %(
        inFileName[0: idx],
        args.processSuffix,
        inFileName[idx:]
    )
    
    tree.Add(inFileName)


if (args.extraDirSuffixes is not None) :
    
    extraDirSuffixes = args.extraDirSuffixes
    #extraDirSuffixes = args.extraDirSuffixes.split(":")
    
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
        
        tree.AddFriend(tree_extra)


# Create output directory
outFileName = "plots/pixelCorrelation/%s.pdf" %(args.outFileName)
outFileName_config = "plots/pixelCorrelation/%s_config.txt" %(args.outFileName)

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
    
    for iEvent in range(0, nEventSel) :
        
        #eventNumber = eventList_temp.GetEntry(iEvent)
        eventNumber = iEvent
        
        #print("Event %d: \n" %(iEvent))
        
        tree.GetEntry(eventNumber)
        
        a_hist = getattr(tree, varName)
        
        nHist = len(a_hist)
        
        for iHist in range(0, nHist) :
            
            cutStr_eval = cutStr
            
            for iCutVar in range(0, len(l_cutVar)) :
                
                if (l_cutVar[iCutVar] in cutStr_eval) :
                    
                    cutVarVal = getattr(tree, l_cutVar[iCutVar])[iHist]
                    
                    cutStr_eval = cutStr_eval.replace(l_cutVar[iCutVar], str(cutVarVal))
            
            #print(iEvent, iHist, cutStr_eval)
            
            if (not eval(cutStr_eval)) :
                
                continue
            
            #varValue = getattr(tree, varInfo.varName)
            #
            #if (varInfo.varIndex >= 0) :
            #    
            #    varValue = varValue[varInfo.varIndex]
            #
            #print varValue
            #
            #l_var.append(varValue)
            
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
#h2_corr = ROOT.TH2F("h2_corr", "h2_corr", args.nBinX, args.xMin, args.xMax, args.nBinY, args.yMin, args.yMax)
#
#imageHistName = "%s >> %s" %(args.imageHistName, args.cutStr)
#
#tree.Draw(imageHistName, args.cutStr)

#h2_corr.Scale(args.norm / h2_corr.GetEntries())


cutStr_mod = args.cutStr
cutStr_mod = cutStr_mod.replace("&&", "and")
cutStr_mod = cutStr_mod.replace("||", "or")

a_corrVar = Common.getArrayFromTBranch(
    tree = tree,
    varName = args.corrVar,
    cutStr = args.cutStr,
    nSel_max = args.nEventMax,
)
print(a_corrVar.shape)

a_pixelScaleVar = None

if (args.pixelScaleVar is not None) :
    
    a_pixelScaleVar = Common.getArrayFromTBranch(
        tree = tree,
        varName = args.pixelScaleVar,
        cutStr = args.cutStr,
        nSel_max = args.nEventMax,
    )

else :
    
    a_pixelScaleVar = numpy.ones(a_corrVar.shape[0])

a_imageHist = Common.getArrayFromVecTH2(
    tree = tree,
    varName = args.imageHistName,
    l_cutVar = args.cutVars,
    cutStr = cutStr_mod,
    nSel_max = args.nEventMax,
    printProgress = True,
)

h2_imageSample = getImageHist(
    tree = tree,
    varName = args.imageHistName,
    l_cutVar = args.cutVars,
    cutStr = cutStr_mod,
    nEvent_max = 1,
)

nBinX = h2_imageSample.GetNbinsX()
nBinY = h2_imageSample.GetNbinsY()

h2_corr = h2_imageSample.Clone("h2_corr")
h2_corr.SetTitle(h2_corr.GetName())
h2_corr.Reset()

print(h2_corr.GetNbinsX(), h2_corr.GetNbinsY())
print(a_corrVar.shape)
print(a_imageHist.shape)
print(a_imageHist[:, 0, 0].shape)

minCorr = 0
maxCorr = 0

for iBinX in range(0, nBinX) :
    
    for iBinY in range(0, nBinY) :
        
        if (numpy.any(a_imageHist[:, iBinY, iBinX])) :
            
            corr = numpy.corrcoef(
                x = [
                    a_corrVar,
                    a_imageHist[:, iBinY, iBinX]*a_pixelScaleVar,
                ]
            )
            
            #corr = abs(corr[0, 1]) * 100
            corr = corr[0, 1] * 100
            
            minCorr = min(minCorr, corr)
            maxCorr = max(maxCorr, corr)
            
            #corr = numpy.mean(a_imageHist[:, iBinY, iBinX])
            
            
            #v1 = a_corrVar
            #v2 = a_imageHist[:, iBinY, iBinX]
            #
            #v1_avg = numpy.mean(v1)
            #v2_avg = numpy.mean(v2)
            #
            #v1_dev = v1 - v1_avg
            #v2_dev = v2 - v2_avg
            #
            #v1_var = numpy.mean(v1_dev * v1_dev)
            #v2_var = numpy.mean(v2_dev * v2_dev)
            #
            #v1v2_cov = numpy.mean(v1_dev * v2_dev)
            #
            #corr = v1v2_cov / numpy.sqrt(v1_var * v2_var) * 100
            
            
            #print(corr)
            
            h2_corr.SetBinContent(iBinX+1, iBinY+1, corr)


print("minCorr %0.4f, maxCorr %0.4f" %(minCorr, maxCorr))


histDetail = Common.HistogramDetails()
histDetail.hist = h2_corr.Clone()
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
#histDetail.zMin = args.zMin
#histDetail.zMax = args.zMax
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

h2_corr.Write()

outRootFile.Close()
