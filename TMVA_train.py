import argparse
import array
import copy
import getpass
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot
#import mxnet
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

#import multiprocessing
import ROOT


nThread = 30;
#ROOT.ROOT.EnableImplicitMT(nThread);



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_stop_L"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_stop_R"]
#infileName_extra_dirSuffix = "network_stop-had_LvsR_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_zk_reco",
#    "hepTop_zb_reco",
#    "hepTop_cosThetaStar_reco",
#    "hepTop_CNN_reco",
#]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_stop_L"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_stop_R"]
#infileName_extra_dirSuffix = "network_stop-lep_LvsR_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_zl_reco",
#    "hepTop_CNN_reco",
#]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_qcd"]
#infileName_extra_dirSuffix = "network_ttbar-had_vs_qcd_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_m_reco",
#    "hepTop_tau2ratio_reco",
#    "hepTop_tau3ratio_reco",
#    "hepTop_tau4ratio_reco",
#    "hepTop_CNN_reco",
#]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_qcd"]
#infileName_extra_dirSuffix = "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_m_reco",
#    "hepTop_tau2ratio_reco",
#    "hepTop_tau3ratio_reco",
#    "hepTop_tau4ratio_reco",
#    #"min(hepTop_lepSubJet1_miniIso_reco, hepTop_lepSubJet2_miniIso_reco)",
#    "hepTop_CNN_reco",
#]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#infileName_extra_dirSuffix = "network_ttbar_lep-vs-had_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_m_reco",
#    "hepTop_tau2ratio_reco",
#    "hepTop_tau3ratio_reco",
#    "hepTop_tau4ratio_reco",
#    #"min(hepTop_lepSubJet1_miniIso_reco, hepTop_lepSubJet2_miniIso_reco)",
#    "hepTop_CNN_reco",
#]



l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_W_lep"]
infileName_extra_dirSuffix = "network_ttbar-lep_vs_W-lep_nLayer-3_CNN-1"

cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
cutStr_bkg = "hepTop_genLepW_deltaR_reco < 1 && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"

l_varName = [
    "hepTop_m_reco",
    "hepTop_tau2ratio_reco",
    "hepTop_tau3ratio_reco",
    "hepTop_tau4ratio_reco",
    "hepTop_CNN_reco",
]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_Z_lep"]
#infileName_extra_dirSuffix = "network_ttbar-lep_vs_Z-lep_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_genLepZ_deltaR_reco < 1 && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_m_reco",
#    "hepTop_tau2ratio_reco",
#    "hepTop_tau3ratio_reco",
#    "hepTop_tau4ratio_reco",
#    "hepTop_CNN_reco",
#]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_W_had"]
#infileName_extra_dirSuffix = "network_ttbar-lep_vs_W-had_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_genHadW_deltaR_reco < 1 && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_m_reco",
#    "hepTop_tau2ratio_reco",
#    "hepTop_tau3ratio_reco",
#    "hepTop_tau4ratio_reco",
#    "hepTop_CNN_reco",
#]



#l_inFileName_sig = mxnet_train_info.d_ntupleFile["l_ntupleFile_ttbar"]
#l_inFileName_bkg = mxnet_train_info.d_ntupleFile["l_ntupleFile_Z_had"]
#infileName_extra_dirSuffix = "network_ttbar-lep_vs_Z-had_nLayer-3_CNN-1"
#
#cutStr_sig = "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#cutStr_bkg = "hepTop_genHadZ_deltaR_reco < 1 && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3"
#
#l_varName = [
#    "hepTop_m_reco",
#    "hepTop_tau2ratio_reco",
#    "hepTop_tau3ratio_reco",
#    "hepTop_tau4ratio_reco",
#    "hepTop_CNN_reco",
#]



splitRatio_sig = 4
splitRatio_bkg = 1


chain_sig = ROOT.TChain("tree")
chain_bkg = ROOT.TChain("tree")


for iFile, iFileName in enumerate(l_inFileName_sig) :
    
    chain_sig.Add(iFileName)


for iFile, iFileName in enumerate(l_inFileName_bkg) :
    
    chain_bkg.Add(iFileName)


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


chain_extra_sig = ROOT.TChain("tree")
chain_extra_bkg = ROOT.TChain("tree")


for iFile, iFileName in enumerate(l_inFileName_extra_sig) :
    
    chain_extra_sig.Add(iFileName)


for iFile, iFileName in enumerate(l_inFileName_extra_bkg) :
    
    chain_extra_bkg.Add(iFileName)


chain_sig.AddFriend(chain_extra_sig)
chain_bkg.AddFriend(chain_extra_bkg)

t = ROOT.TTree("t", "t")
a = array.array("d", [0.0])
t.Branch("hepTop_genHadW_deltaR_reco", a, "hepTop_genHadW_deltaR_reco/D")
t.Branch("hepTop_genHadZ_deltaR_reco", a, "hepTop_genHadZ_deltaR_reco/D")
t.Branch("hepTop_genLepW_deltaR_reco", a, "hepTop_genLepW_deltaR_reco/D")
t.Branch("hepTop_genLepZ_deltaR_reco", a, "hepTop_genLepZ_deltaR_reco/D")
chain_sig.AddFriend(t)


outFileName = "TMVA.root"
outFile = ROOT.TFile.Open(outFileName, "RECREATE")

str_transformation = "I"
#str_transformation = "IDP"

factory = ROOT.TMVA.Factory(
    "TMVAClassification",
    outFile,
    "!V:!Silent:Color:DrawProgressBar:Transformations=" + str_transformation + ":AnalysisType=Classification"
)

dataloader = ROOT.TMVA.DataLoader("dataset")


for iVar, varName in enumerate(l_varName) :
    
    dataloader.AddVariable(varName)


weight_sig = 1.0
weight_bkg = 1.0

dataloader.AddSignalTree    (chain_sig, weight_sig)
dataloader.AddBackgroundTree(chain_bkg, weight_bkg)

nEvent_sig = int(chain_sig.Draw(l_varName[0], cutStr_sig, "goff"))
nEvent_bkg = int(chain_bkg.Draw(l_varName[0], cutStr_bkg, "goff"))

nEventTrn_sig = int(splitRatio_sig / (1.0 + splitRatio_sig) * nEvent_sig)
nEventTrn_bkg = int(splitRatio_bkg / (1.0 + splitRatio_bkg) * nEvent_bkg)


dataloader.PrepareTrainingAndTestTree(
    ROOT.TCut(cutStr_sig),
    ROOT.TCut(cutStr_bkg),
    
    #"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V"
    
    #"nTrain_Signal=%d:nTrain_Background=%d:SplitMode=Random:NormMode=NumEvents:!V" %(nEventTrn_sig, nEventTrn_bkg)
    "nTrain_Signal=%d:nTrain_Background=%d:SplitMode=Random:NormMode=EqualNumEvents:!V" %(nEventTrn_sig, nEventTrn_bkg)
)


factory.BookMethod(
    dataloader,
    ROOT.TMVA.Types.kBDT,
    "BDT",
    "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20"
)

#factory.BookMethod(
#    dataloader,
#    ROOT.TMVA.Types.kBDT,
#    "BDTG",
#    "!H:!V:NTrees=1000:MinNodeSize=2.5%:BoostType=Grad:Shrinkage=0.10:UseBaggedBoost:BaggedSampleFraction=0.5:nCuts=20:MaxDepth=2"
#)


ROOT.ROOT.EnableImplicitMT(nThread);

# Train MVAs using the set of training events
factory.TrainAllMethods()

# ---- Evaluate all MVAs using the set of test events
factory.TestAllMethods()

# ----- Evaluate and compare performance of all configured MVAs
factory.EvaluateAllMethods()

# --------------------------------------------------------------

# Save the output
outFile.Close()

print("==> Wrote root file:", outFile.GetName())
print("==> TMVAClassification is done!")


## Launch the GUI for the root macros
#if (not ROOT.gROOT.IsBatch()) :
#    
#    ROOT.TMVA.TMVAGui(outFileName)
