from __future__ import print_function

import argparse
import array
import copy
import gc
import getpass
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot
import mxnet
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


matplotlib.pyplot.rc("text", usetex = True)
matplotlib.rcParams["text.latex.preamble"] = [
    r"\usepackage{amsmath}",
    r"\usepackage{slashed}",
]


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


parser.add_argument(
    "--trainings",
    help = "Name of the training to be used",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--trainingDirNames",
    help = "Training directory name",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--epochs",
    help = "Result afer which epoch to be used",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--nEventMaxs",
    help = "Number of signal and background (each) events to be used",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--splitEverys",
    help = "Load how many images per (multiprocessing) process",
    type = int,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--sigFiles",
    help = "Signal files: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    nargs = "*",
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--bkgFiles",
    help = "Background files: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    nargs = "*",
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
)

parser.add_argument(
    "--extraCutsSig",
    help = "Extra selection on signal",
    type = str,
    nargs = "*",
    required = True,
    #default = "1"
)

parser.add_argument(
    "--extraCutsBkg",
    help = "Extra selection on background",
    type = str,
    nargs = "*",
    required = True,
    #default = "1"
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
    "--title",
    help = "Plot title",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--trainDetailSig",
    help = "Training detail for signal",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--trainDetailBkg",
    help = "Training detail for background",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--evalDetailSig",
    help = "Evaluation detail for signal",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--evalDetailBkg",
    help = "Evaluation detail for background",
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
    "--extraDetailsStr",
    help = "List (space separated) of extra details to be shown on the plot",
    type = str,
    nargs = "*",
    required = False,
    default = [],
)

parser.add_argument(
    "--extraDetailsPos",
    help = "Positions (space separated pairs of x and y) of the extra details (LL coordinate)",
    type = float,
    nargs = "*",
    required = False,
    default = [],
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
    help = "Plot labels",
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
    "--outDir",
    help = "Output directory",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--outFileName",
    help = "Output filename",
    type = str,
    required = True,
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


if (len(args.extraDetailsPos) != 2*len(args.extraDetailsStr)) :
    
    print("Error: Invalid extra detail info format.")
    exit(1)


os.system("mkdir -p %s" %(args.outDir))


context = mxnet.cpu()
username = getpass.getuser()

if (username == "sobhatta") :
    
    print("*********************")
    print("***** Using GPU *****")
    print("*********************")
    print("\n")
    
    context = mxnet.gpu()
    
    #ROOT.ROOT.EnableImplicitMT(30)


def getEfficiency(arr, val, norm = 1.0) :
    
    eff = float(sum(arr > val)) / norm
    
    return eff


d_tree = {}
l_histDetail_ROC = []


for iPlot in range(0, len(args.trainings)) :
    
    if (args.sigFiles[iPlot] not in d_tree) :
        
        l_inFileName_sig = mxnet_train_info.d_ntupleFile[args.sigFiles[iPlot]]
        tree_sig = ROOT.TChain("tree")
        
        for iFile in range(0, len(l_inFileName_sig)) :
            
            tree_sig.Add(l_inFileName_sig[iFile])
        
        d_tree[args.sigFiles[iPlot]] = tree_sig
    
    
    if (args.bkgFiles[iPlot] not in d_tree) :
        
        l_inFileName_bkg = mxnet_train_info.d_ntupleFile[args.bkgFiles[iPlot]]
        tree_bkg = ROOT.TChain("tree")
        
        for iFile in range(0, len(l_inFileName_bkg)) :
            
            tree_bkg.Add(l_inFileName_bkg[iFile])
        
        d_tree[args.bkgFiles[iPlot]] = tree_bkg
    
    
    tree_sig = d_tree[args.sigFiles[iPlot]]
    tree_bkg = d_tree[args.bkgFiles[iPlot]]
    
    
    nEvent_tree_sig = tree_sig.GetEntries()
    nEvent_tree_bkg = tree_bkg.GetEntries()
    
    l_varStr = mxnet_train_info.d_info[args.trainings[iPlot]]["layerNames"]
    l_cutVar = mxnet_train_info.d_info[args.trainings[iPlot]]["varNames"]
    
    nVar = len(l_varStr)
    
    cutStr_sig = "%s and (%s)" %(mxnet_train_info.d_info[args.trainings[iPlot]]["cutStr_sig"], args.extraCutsSig[iPlot])
    cutStr_bkg = "%s and (%s)" %(mxnet_train_info.d_info[args.trainings[iPlot]]["cutStr_bkg"], args.extraCutsBkg[iPlot])
    
    
    d_varInfo = Common.getVarInfoFromTree(
        l_varStr = l_varStr,
        tree_sig = tree_sig,
        tree_bkg = tree_bkg,
        l_cutVar = l_cutVar,
        cutStr_sig = cutStr_sig,
        cutStr_bkg = cutStr_bkg,
        nEventTotal_sig = args.nEventMaxs[iPlot],
        nEventTotal_bkg = args.nEventMaxs[iPlot],
        splitEvery = args.splitEverys[iPlot],
        #nCPUfraction = args.nCPUfraction,
    )
    
    
    networkSymbolFile = "mxnetNetworkInfo/%s/network-symbol.json" %(args.trainingDirNames[iPlot])
    networkParamFile = "mxnetNetworkInfo/%s/network-%04d.params" %(args.trainingDirNames[iPlot], args.epochs[iPlot])
    #outFileName_ROC = "plots/mxnet/%s/ROC_epoch%03d%s.pdf" %(args.trainingDirNames[iPlot], args.epochs[iPlot], args.outFileSuffix)
    #outFileName_config = "plots/mxnet/%s/ROC_epoch%03d%s_config.txt" %(args.trainingDirNames[iPlot], args.epochs[iPlot], args.outFileSuffix)
    #
    #
    ## Save the configuration
    #
    #print("Saving the configuration to: %s" %(outFileName_config))
    #
    #with open(outFileName_config, "w") as configOutFile :
    #    
    #    configOutFile.write(pprint.pformat(d_args, width = 1))
    #    configOutFile.write("\n")
    #
    #print("\n")
    
    
    neuralNetwork = mxnet.gluon.nn.SymbolBlock.imports(
        symbol_file = networkSymbolFile,
        param_file  = networkParamFile,
        input_names = ["data"],
        ctx = context,
    )
    
    
    l_data_sig = []
    l_data_bkg = []
    
    l_data = []
    
    nRow = d_varInfo[l_varStr[0]].a_sig[0].shape[0]
    nCol = d_varInfo[l_varStr[0]].a_sig[0].shape[1]
    
    a_data_sig = numpy.zeros((d_varInfo[l_varStr[0]].a_sig.shape[0], nVar, nRow, nCol), dtype = "float32")
    a_data_bkg = numpy.zeros((d_varInfo[l_varStr[0]].a_bkg.shape[0], nVar, nRow, nCol), dtype = "float32")
    
    
    for iVar in range(0, nVar) :
        
        varStr = l_varStr[iVar]
        
        varInfo = d_varInfo[varStr]
        
        a_data_sig[:, iVar, :, :] = varInfo.a_sig
        print(varInfo.a_sig.shape)
        
        # Free memory
        varInfo.a_sig = None
        gc.collect()
        
        a_data_bkg[:, iVar, :, :] = varInfo.a_bkg
        print(varInfo.a_bkg.shape)
        
        # Free memory
        varInfo.a_bkg = None
        gc.collect()
    
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
    
    
    #print(pred_sig)
    #print(pred_bkg)
    
    discMin = 0
    discMax = 1
    disc_nSample = 500
    #disc_nSample = 200
    disc_stepSize = float(discMax-discMin) / disc_nSample
    disc_stepSize_small = disc_stepSize / 500.0
    
    l_discr = numpy.arange(discMin, discMax, disc_stepSize)
    
    # Add a very small increment(s) (decrement(s)) near discMin (discMax)
    #l_discr = numpy.append(discMin + disc_stepSize_small, l_discr)
    
    # If the lowest signal efficiency is too large, add a very small increment(s) near discMax
    if (float(sum(pred_sig > max(l_discr)))/pred_sig.shape[0] > 0.05) :
        
        l_discr = numpy.append(l_discr, numpy.arange(max(l_discr), discMax, disc_stepSize_small))
    
    
    l_eff_sig = numpy.zeros(len(l_discr)+2)
    l_eff_bkg = numpy.zeros(len(l_discr)+2)
    
    # The first/last point will be (1, 1)/(0, 0)
    # So include these
    #l_eff_sig = [1.0]
    #l_eff_bkg = [1.0]
    l_eff_sig[0] = 1.0
    l_eff_bkg[0] = 1.0
    
    
    nCPU = min(multiprocessing.cpu_count(), len(l_eff_sig))
    
    pool = multiprocessing.Pool(processes = nCPU)
    
    l_job_sig = []
    l_job_bkg = []
    
    nEventTot_sig = pred_sig.shape[0]
    nEventTot_bkg = pred_bkg.shape[0]
    
    print("\n")
    print("Calculating signal and background efficiencies. \n")
    
    for iDiscr, discVal in enumerate(l_discr) :
        
        #nEventSel_sig = float(sum(pred_sig > discVal))
        #nEventSel_bkg = float(sum(pred_bkg > discVal))
        #
        #eff_sig = nEventSel_sig / nEventTot_sig
        #eff_bkg = nEventSel_bkg / nEventTot_bkg
        
        #eff_sig = getEfficiency(arr = pred_sig, val = discVal, norm = nEventTot_sig)
        #eff_bkg = getEfficiency(arr = pred_bkg, val = discVal, norm = nEventTot_bkg)
        
        # Background rejection efficiency
        #eff_bkg = 1 - eff_bkg
        
        #print(
        #    "%d/%d: %0.8f: "
        #    "eff_sig %0.8f, "
        #    "eff_bkg %0.8f, "
        #    "\n" %(
        #    
        #    iDiscr+1, len(l_discr),
        #    discVal,
        #    eff_sig,
        #    eff_bkg
        #))
        
        #l_eff_sig.append(eff_sig)
        #l_eff_bkg.append(eff_bkg)
        
        job = pool.apply_async(
            getEfficiency,
            (),
            dict(
                arr = pred_sig,
                val = discVal,
                norm = nEventTot_sig,
            ),
        )
        
        l_job_sig.append(job)
        
        
        job = pool.apply_async(
            getEfficiency,
            (),
            dict(
                arr = pred_bkg,
                val = discVal,
                norm = nEventTot_bkg,
            ),
        )
        
        l_job_bkg.append(job)
    
    
    pool.close()
    pool.join()
    
    
    for iJob in range(0, len(l_job_sig)) :
        
        l_eff_sig[iJob+1] = l_job_sig[iJob].get()
        l_eff_bkg[iJob+1] = l_job_bkg[iJob].get()
        
        
        print(
            "%d/%d: %0.8f: "
            "eff_sig %0.8f, "
            "eff_bkg %0.8f, "
            "\n" %(
            
            iJob+1, len(l_discr),
            l_discr[iJob],
            l_eff_sig[iJob+1],
            l_eff_bkg[iJob+1]
        ))
    
    
    
    # The last point will be (0, 0)
    # So include this
    #l_eff_sig.extend([0.0])
    #l_eff_bkg.extend([0.0])
    
    
    # Get the unique x-values (i.e. the signal efficiency)
    # Required for the interpolation
    l_uniqueIndex = numpy.unique(l_eff_sig, return_index = True)[1]
    
    #l_eff_sig_unique = numpy.array(l_eff_sig)[l_uniqueIndex]
    #l_eff_bkg_unique = numpy.array(l_eff_bkg)[l_uniqueIndex]
    l_eff_sig_unique = l_eff_sig[l_uniqueIndex]
    l_eff_bkg_unique = l_eff_bkg[l_uniqueIndex]
    
    #l_significance_unique = numpy.array(l_significance)[l_uniqueIndex]
    
    # Add the x=0 point by hand if not already there
    if (0 not in l_eff_sig_unique) :
        
        l_eff_sig_unique = numpy.append(l_eff_sig_unique, 0.0)
        l_eff_bkg_unique = numpy.append(l_eff_bkg_unique, max(l_eff_bkg_unique))
        
        #l_significance_unique = numpy.append(l_significance_unique, 0.0)
    
    # Sort by the x-axis values (i.e. the signal efficiency)
    # Required for the interpolation
    l_sortedIndex = numpy.argsort(l_eff_sig_unique)
    
    l_eff_sig_unique = l_eff_sig_unique[l_sortedIndex]
    l_eff_bkg_unique = l_eff_bkg_unique[l_sortedIndex]
    
    #l_significance_unique = l_significance_unique[l_sortedIndex]
    
    #fInter_ROC = scipy.interpolate.InterpolatedUnivariateSpline(l_eff_sig_unique, l_eff_bkg_unique, bbox = [0, 1], ext = "zeros")
    fInter_ROC = scipy.interpolate.InterpolatedUnivariateSpline(l_eff_sig_unique, l_eff_bkg_unique, bbox = [0, 1], k = 1, ext = "zeros")
    print([fInter_ROC(ele) for ele in numpy.arange(0, 1, 0.0999)])
    
    areaROC = fInter_ROC.integral(0, 1)
    print("Area under ROC: %0.4f" %(areaROC))
    
    
    AUC_str = "#scale[1.65]{AUC=%0.2g}" %(areaROC)
    
    
    a_x = array.array("f", numpy.linspace(0, 1, 1000))
    a_y = array.array("f", [fInter_ROC(ele) for ele in a_x])
    
    gr_ROC = ROOT.TGraph(len(a_x), a_x, a_y)
    gr_ROC.SetName("graph_%d" %(iPlot+1))
    h1_ROC = Common.TGraphToTH1(graph = gr_ROC, setError = False)
    
    h1_ROC.GetXaxis().SetRangeUser(0.0, 1.0)
    h1_ROC.SetMinimum(args.yMin)
    h1_ROC.SetMaximum(args.yMax)
    
    histDetail_ROC = Common.HistogramDetails()
    histDetail_ROC.hist = h1_ROC.Clone()
    histDetail_ROC.drawOption = "L"
    histDetail_ROC.lineColor = args.lineColors[iPlot]
    histDetail_ROC.lineStyle = args.lineStyles[iPlot]
    histDetail_ROC.lineWidth = 3
    histDetail_ROC.markerSize = 0
    histDetail_ROC.fillStyle = 0
    histDetail_ROC.histLabel = "%s [AUC=%0.2g]" %(args.labels[iPlot], areaROC)
    histDetail_ROC.histTitle = args.title
    
    l_histDetail_ROC.append(histDetail_ROC)
    
    detailStr_train = "#splitline{%s}{%s}" %(args.trainDetailSig, args.trainDetailBkg)
    detailStr_eval = "#splitline{%s}{%s}" %(args.evalDetailSig, args.evalDetailBkg)
    detailStr = "#splitline{%s}{%s}" %(detailStr_train, detailStr_eval)
    
    detailStr = "#splitline{%s}{%s}" %(AUC_str, detailStr)
    
    
    l_extraText = [
        [args.detailPos[0], args.detailPos[1], detailStr],
    ]
    
    
    for iExtraText in range(0, len(args.extraDetailsStr)) :
        
        l_extraText.append([
            args.extraDetailsPos[iExtraText],
            args.extraDetailsPos[iExtraText+1],
            args.extraDetailsStr[iExtraText],
        ])
    
    
    # Free memory
    d_varInfo.clear()
    d_varInfo = None


epochStr = ""

if (len(args.trainings) == 1) :
    
    epochStr = "_epoch%03d" %(args.epochs[0])


#outFileName_ROC = "plots/mxnet/%s/ROC_epoch%03d%s.pdf" %(args.trainingDirNames[iPlot], args.epochs[iPlot], args.outFileSuffix)
outFileName_ROC = "%s/%s%s%s.pdf" %(args.outDir, args.outFileName, epochStr, args.outFileSuffix)

#outFileName_config = "plots/mxnet/%s/ROC_epoch%03d%s_config.txt" %(args.trainingDirNames[iPlot], args.epochs[iPlot], args.outFileSuffix)
outFileName_config = "%s/%s%s%s_config.txt" %(args.outDir, args.outFileName, epochStr, args.outFileSuffix)


# Save the configuration

print("Saving the configuration to: %s" %(outFileName_config))

with open(outFileName_config, "w") as configOutFile :
    
    configOutFile.write(pprint.pformat(d_args, width = 1))
    configOutFile.write("\n")

print("\n")


Common.plot1D(
    list_histDetails = l_histDetail_ROC,
    stackDrawOption = "nostack",
    title = args.title,
    titleSizeScale = 0.9,
    xTitle = "Signal efficiency", yTitle = "Background efficiency",
    xMin = 0.0, xMax = 1.0,
    yMin = args.yMin, yMax = args.yMax,
    logX = False, logY = True,
    gridX = True, gridY = True,
    nDivisionsX = [5, 2, 5],
    #xTitleSizeScale = 1.0, yTitleSizeScale = 1.0,
    #xTitleOffset = 1.0, yTitleOffset = 1.0,
    #xLabelSizeScale = 1.0, yLabelSizeScale = 1.0,
    #centerLabelsX = True, centerLabelsY = True,
    drawLegend = True,
    #legendDrawOption = "",
    #legendNcol = 1,
    #legendWidthScale = 1,
    #legendHeightScale = 0.5,
    transparentLegend = True,
    legendTextSize = args.legendTextSize,
    legendBorderSize = 0,
    legendPos = args.legendPos,
    legendTitle = "",
    l_extraText = l_extraText, #[[x, y, text], ...]
    outFileName = outFileName_ROC.replace(".pdf", ""),
    outFileName_suffix = "",
)
