from __future__ import print_function

import array
import copy
import matplotlib
import matplotlib.pyplot
import mxnet
import numpy
import os
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


##ntupleFileName_sig = "outputTree_ttbar.root"
##ntupleFileName_sig = "outputTree_ttbar_withCNNdiscr.root"
#ntupleFileName_sig = "outputTree_ttbar_withCNNdiscr_oneLayer_relu_epoch020.root"
#
##ntupleFileName_bkg = "outputTree_qcd.root"
##ntupleFileName_bkg = "outputTree_qcd_withCNNdiscr.root"
#ntupleFileName_bkg = "outputTree_qcd_withCNNdiscr_oneLayer_relu_epoch020.root"
#
#ntupleFile_sig = ROOT.TFile(ntupleFileName_sig)
#ntupleFile_bkg = ROOT.TFile(ntupleFileName_bkg)
#
#tree_sig = ntupleFile_sig.Get("tree")
#tree_bkg = ntupleFile_bkg.Get("tree")


l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_qcd"]
infileName_extra_dirSuffix = "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1"


methodName = "BDT"

#weightFileName = "weights/TMVAClassification_BDT.weights.xml"
#weightFileName = "weights_noIsMayBeTop/TMVAClassification_BDT.weights.xml"
#weightFileName = "weights_train-isMayBeTop/TMVAClassification_BDT.weights.xml"
#weightFileName = "weights_train-withBmatchedVar/TMVAClassification_BDT.weights.xml"
#weightFileName = "weights_withCNNdiscr/TMVAClassification_BDT.weights.xml"
#weightFileName = "weights_withIsMayBeTop_noCNNdiscr/TMVAClassification_BDT.weights.xml"
#weightFileName = "weights_withIsMayBeTop_withCNNdiscr/TMVAClassification_BDT.weights.xml"

weightFileName = "TMVAinfo/ttbar-lep_vs_qcd/weights/TMVAClassification_BDT.weights.xml"


l_variable = [
    #"hepTop_pT_reco",
    #"hepTop_eta_reco",
    
    "hepTop_m_reco",
    
    #"hepTop_subJet12_m_reco",
    #"hepTop_subJet23_m_reco",
    #"hepTop_subJet31_m_reco",
    
    #"hepTop_subJet123_m_reco",
    
    #"hepTop_frec_reco",
    
    #"hepTop_tau1ratio_reco",
    #"hepTop_tau2ratio_reco",
    #"hepTop_tau3ratio_reco",
    #"hepTop_tau4ratio_reco",
    
    #"hepTop_C1_reco",
    #"hepTop_C2_reco",
    #"hepTop_C3_reco",
    
    #"hepTop_nSubJetBtagged_reco",
    #"hepTop_nBtaggedJetInFatJet_reco",
    
    #"hepTop_nSubJetBmatched_reco",
    #"hepTop_nBinFatJet_reco",
    
    #"hepTop_showerDecon_chi_reco",
    
    #"hepTop_isMayBeTop_reco",
    
    #"hepTop_boosted_CNNdiscr_reco",
    
    "hepTop_CNN_reco",
]


l_spectator = [
    #"hepTop_genTop_deltaR_reco",
    #
    #"hepTop_isTagged_reco",
    #
    ##"hepTop_nSubJetBmatched_reco",
    ##"hepTop_nBinFatJet_reco",
    #
    #"hepTop_zk_reco",
    #"hepTop_zb_reco",
    #"hepTop_cosThetaStar_reco",
]


l_cutVariable = [
    #"hepTop_genTop_deltaR_reco",
    #"hepTop_isMayBeTop_reco",
    
    "hepTop_pT_reco",
    "hepTop_genHadTop_deltaR_reco",
    "hepTop_genLepTop_deltaR_reco",
    "hepTop_nExcSubJet_reco",
]


l_returnVariable = [
    #"hepTop_isMayBeTop_reco",
    "hepTop_isTagged_reco",
]


#
baselineCutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3"

baselineCutStr_bkg = "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3"


#
extraCutStr_sig = "1"
#extraCutStr_sig = "hepTop_isMayBeTop_reco"

extraCutStr_bkg = "1"
#extraCutStr_bkg = "hepTop_isMayBeTop_reco"


#tree_nEvent_sig = tree_sig.GetEntries()
#tree_nEvent_bkg = tree_bkg.GetEntries()
#
#eventList_sig = ROOT.TEventList("eventList_sig", "eventList_sig")
#tree_sig.Draw(">> %s" %(eventList_sig.GetName()))
##tree_sig.Draw(">> %s" %(eventList_sig.GetName()), baselineCutStr_sig)
#
#eventList_bkg = ROOT.TEventList("eventList_bkg", "eventList_bkg")
#tree_bkg.Draw(">> %s" %(eventList_bkg.GetName()))
##tree_bkg.Draw(">> %s" %(eventList_bkg.GetName()), baselineCutStr_bkg)
#
#tree_nEvent_sig = eventList_sig.GetN()
#tree_nEvent_bkg = eventList_bkg.GetN()
#
#print tree_nEvent_sig
#print tree_nEvent_bkg


tree_sig = ROOT.TChain("tree")
tree_bkg = ROOT.TChain("tree")


for iFile, iFileName in enumerate(l_inFileName_sig) :
    
    tree_sig.Add(iFileName)


for iFile, iFileName in enumerate(l_inFileName_bkg) :
    
    tree_bkg.Add(iFileName)


l_inFileName_extra_sig = []
l_inFileName_extra_bkg = []


for iFile, iFileName in enumerate(l_inFileName_sig) :
    
    iFileName_extra = "%s_%s%s" %(
        iFileName[0: iFileName.rfind("/")],
        infileName_extra_dirSuffix,
        iFileName[iFileName.rfind("/"):],
    )
    
    l_inFileName_extra_sig.extend([iFileName_extra])


for iFile, iFileName in enumerate(l_inFileName_bkg) :
    
    iFileName_extra = "%s_%s%s" %(
        iFileName[0: iFileName.rfind("/")],
        infileName_extra_dirSuffix,
        iFileName[iFileName.rfind("/"):],
    )
    
    l_inFileName_extra_bkg.extend([iFileName_extra])


#print("\n".join(l_inFileName_extra_sig), "\n")
#print("\n".join(l_inFileName_extra_bkg), "\n")


tree_extra_sig = ROOT.TChain("tree")
tree_extra_bkg = ROOT.TChain("tree")


for iFile, iFileName in enumerate(l_inFileName_extra_sig) :
    
    tree_extra_sig.Add(iFileName)


for iFile, iFileName in enumerate(l_inFileName_extra_bkg) :
    
    tree_extra_bkg.Add(iFileName)


tree_sig.AddFriend(tree_extra_sig)
tree_bkg.AddFriend(tree_extra_bkg)


d_tmvaResult_sig = Common.evaluateTMVAandGetDiscr(
    methodName = methodName,
    weightFileName = weightFileName,
    tree = tree_sig,
    l_variable = l_variable,
    l_spectator = l_spectator,
    l_cutVariable = l_cutVariable,
    l_returnVariable = l_returnVariable,
    cutStr = baselineCutStr_sig,
    nEventSel_max = 10000,
)

d_tmvaResult_bkg = Common.evaluateTMVAandGetDiscr(
    methodName = methodName,
    weightFileName = weightFileName,
    tree = tree_bkg,
    l_variable = l_variable,
    l_spectator = l_spectator,
    l_cutVariable = l_cutVariable,
    l_returnVariable = l_returnVariable,
    cutStr = baselineCutStr_bkg,
    nEventSel_max = 10000,
)

l_discrVal_sig = d_tmvaResult_sig["l_discrVal"]
l_discrVal_bkg = d_tmvaResult_bkg["l_discrVal"]


l_extraCut_sig = numpy.ones(len(l_discrVal_sig))

#print d_tmvaResult_sig

if (extraCutStr_sig != "1") :
    
    for iEntry in range(0, len(l_discrVal_sig)) :
        
        extraCutStr_eval = extraCutStr_sig
        
        for iVar, varName in enumerate(l_returnVariable) :
            
            extraCutStr_eval = extraCutStr_eval.replace(varName, str(d_tmvaResult_sig[varName][iEntry]))
        
        l_extraCut_sig[iEntry] = eval(extraCutStr_eval)



l_extraCut_bkg = numpy.ones(len(l_discrVal_bkg))

if (extraCutStr_bkg != "1") :
    
    for iEntry in range(0, len(l_discrVal_bkg)) :
        
        extraCutStr_eval = extraCutStr_bkg
        
        for iVar, varName in enumerate(l_returnVariable) :
            
            extraCutStr_eval = extraCutStr_eval.replace(varName, str(d_tmvaResult_bkg[varName][iEntry]))
        
        l_extraCut_bkg[iEntry] = eval(extraCutStr_eval)


#matplotlib.pyplot.hist(l_discrVal_sig, bins = 100, range = (-1, 1), histtype = "step", color = "b")
#matplotlib.pyplot.hist(l_discrVal_bkg, bins = 100, range = (-1, 1), histtype = "step", color = "r")
#matplotlib.pyplot.show()

print(len(l_discrVal_sig))
print(len(l_discrVal_bkg))


discrMin = -1
discrMax = +1
discr_nSample = 500
discr_stepSize = float(discrMax-discrMin) / discr_nSample
discr_stepSize_small = discr_stepSize / 500.0

l_discrCut = numpy.arange(discrMin, discrMax, discr_stepSize)


l_eff_sig = []
l_eff_bkg = []


for iDiscr, discrCut in enumerate(l_discrCut) :
    
    eff_sig = float(sum(numpy.multiply(
        numpy.array(l_discrVal_sig) > discrCut,
        l_extraCut_sig
    )))
    
    eff_sig /= len(l_discrVal_sig)
    
    
    eff_bkg = float(sum(numpy.multiply(
        numpy.array(l_discrVal_bkg) > discrCut,
        l_extraCut_bkg
    )))
    
    eff_bkg /= len(l_discrVal_bkg)
    #eff_bkg = 1 - eff_bkg
    
    #if (eff_bkg) :
    #    
    #    eff_bkg = 1.0 / eff_bkg
    #
    #else :
    #    
    #    eff_bkg = 99999
    
    print(
        "%d/%d: %0.8f: "
        "eff_sig %0.8f, "
        "eff_bkg %0.8f, "
        "\n" %(
        
        iDiscr+1, len(l_discrCut),
        discrCut,
        eff_sig,
        eff_bkg
    ))
    
    l_eff_sig.append(eff_sig)
    l_eff_bkg.append(eff_bkg)


eff_hepTT_sig = float(sum(d_tmvaResult_sig["hepTop_isTagged_reco"]))
eff_hepTT_sig /= len(l_discrVal_sig)

eff_hepTT_bkg = float(sum(d_tmvaResult_bkg["hepTop_isTagged_reco"]))
eff_hepTT_bkg /= len(l_discrVal_bkg)
#eff_hepTT_bkg = 1 - eff_hepTT_bkg
#eff_hepTT_bkg = 1.0 / eff_hepTT_bkg


#################### Plot ROC ####################

colorAxis1 = "r"
colorAxis2 = "b"

fig = matplotlib.pyplot.figure(figsize = [9, 7])
axis1 = fig.add_subplot(1, 1, 1)

axis1.set_xlabel("Signal efficiency")
#axis1.set_ylabel("Background rejection")
axis1.set_ylabel("Background efficiency")

#axis2 = axis1.twinx()


xMin = 0
xMax = 1
tickInterval_major = 0.1
tickInterval_minor = tickInterval_major / 10.0

l_tick_major = numpy.arange(xMin, xMax+tickInterval_major, tickInterval_major)
l_tick_minor = numpy.arange(xMin, xMax+tickInterval_minor, tickInterval_minor)

axis1.set_xticks(l_tick_major)
axis1.set_xticks(l_tick_minor, minor = True)


yMin = 0
yMax = 1
tickInterval_major = 0.01
tickInterval_minor = tickInterval_major / 10.0

l_tick_major = numpy.arange(yMin, yMax+tickInterval_major, tickInterval_major)
l_tick_minor = numpy.arange(yMin, yMax+tickInterval_minor, tickInterval_minor)

#axis1.set_yticks(l_tick_major)
#axis1.set_yticks(l_tick_minor, minor = True)


axis1.tick_params("x", which = "major", length = matplotlib.pyplot.rcParams["xtick.major.size"] * 2)
axis1.tick_params("x", which = "minor", length = matplotlib.pyplot.rcParams["xtick.minor.size"] * 2)

axis1.tick_params("y", which = "major", length = matplotlib.pyplot.rcParams["ytick.major.size"] * 2)
axis1.tick_params("y", which = "minor", length = matplotlib.pyplot.rcParams["ytick.minor.size"] * 2)

#axis1.set_ylim([0.95, 1])
axis1.set_ylim([1e-5, 1])
axis1.set_yscale("log")

axis1.set_xlim([0, 1])


axis1.plot(
    [0, 1],
    [eff_hepTT_bkg, eff_hepTT_bkg],
    color = "g",
    alpha = 0.75,
    linestyle = "--",
    linewidth = 1,
    markersize = 15,
)

axis1.plot(
    [eff_hepTT_sig, eff_hepTT_sig],
    [0, 1],
    color = "g",
    alpha = 0.75,
    linestyle = "--",
    linewidth = 1,
    markersize = 15,
)

axis1.plot(
    [eff_hepTT_sig],
    [eff_hepTT_bkg],
    color = "g",
    marker = "*",
    #linewidth = 2,
    markersize = 15,
)


axis1.plot(
    l_eff_sig,
    l_eff_bkg,
    color = "b",
    linestyle = "-",
    linewidth = 2,
    markersize = 0,
)


axis1.grid(
    which = "major",
)


fig.tight_layout()


fig.savefig("plots/temp/ROC.pdf")

#fig.savefig("plots/tmva/ROC_sig-isMayBeTop.pdf")
#fig.savefig("plots/tmva/ROC_sig-isMayBeTop_bkg-isMayBeTop.pdf")
#fig.savefig("plots/tmva/ROC_train-isMayBeTop.pdf")
#fig.savefig("plots/tmva/ROC_train-withBmatchedVar.pdf")
#fig.savefig("plots/tmva/ROC_withCNNdiscr.pdf")
#fig.savefig("plots/tmva/ROC_withIsMayBeTop_noCNNdiscr_wrtAllJets.pdf")
#fig.savefig("plots/tmva/ROC_withIsMayBeTop_withCNNdiscr_wrtAllJets.pdf")


#matplotlib.pyplot.show()
