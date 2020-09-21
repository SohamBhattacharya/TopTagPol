#!/usr/bin/env python

import multiprocessing
import os


nCPU = 10

pool = multiprocessing.Pool(processes = nCPU)
l_job = []


def cleanSpaces(string) :
    
    while ("  " in string) :
        
        string = string.replace("  ", " ")
    
    return string


# ############################## network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 ##############################
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#    --plotDenList \
#        "lepTopVis_pT_truth" \
#        "lepTopVis_pT_truth" \
#        "lepTopVis_pT_truth" \
#        "lepTopVis_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9961" \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9961" \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9376" \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9376" \
#    --cutDenList \
#        "lepTopVis_pT_truth > 200" \
#        "lepTopVis_pT_truth > 200" \
#        "lepTopVis_pT_truth > 200" \
#        "lepTopVis_pT_truth > 200" \
#    --labelList \
#        "t^{lep}_{L} from W'_{3TeV} (ROC_{60})" \
#        "t^{lep}_{R} from W'_{3TeV} (ROC_{60})" \
#        "t^{lep}_{L} from W'_{3TeV} (ROC_{80})" \
#        "t^{lep}_{R} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{lep}_{gen} p^{vis}_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{lep} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT_LR" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_Wprime_3TeV_lep \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#    --plotDenList \
#        "lepTopVis_pT_truth" \
#        "lepTopVis_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9961" \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9376" \
#    --cutDenList \
#        "lepTopVis_pT_truth > 200" \
#        "lepTopVis_pT_truth > 200" \
#    --labelList \
#        "t^{lep} from W'_{3TeV} (ROC_{60})" \
#        "t^{lep} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "t^{lep}_{gen} p^{vis}_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{lep} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9961" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9376" \
#    --cutDenList \
#        "hepTop_pT_reco > 200" \
#        "hepTop_pT_reco > 200" \
#    --labelList \
#        "udsg jets from QCD (ROC_{60})" \
#        "udsg jets from QCD (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "Jet p_{T} [GeV]" \
#    --yTitle "Mis-id. probability" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 1e-6 \
#    --yMax 1 \
#    --logY \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{lep} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1/misId_vs_reco-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ############################## network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 ##############################
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#    --extraDirSuffixList \
#        network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
#    --plotDenList \
#        "lepTopVis_pT_truth" \
#        "lepTopVis_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9983" \
#        "hepTop_nearestGenLepTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9766" \
#    --cutDenList \
#        "lepTopVis_pT_truth > 200" \
#        "lepTopVis_pT_truth > 200" \
#    --labelList \
#        "t^{lep} from t#bar{t} (ROC_{60})" \
#        "t^{lep} from t#bar{t} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "t^{lep}_{gen} p^{vis}_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{lep} (from t#bar{t}) vs. udsg (from QCD) jets" \
#    --outFileName "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#        network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9983" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.9766" \
#    --cutDenList \
#        "hepTop_pT_reco > 200" \
#        "hepTop_pT_reco > 200" \
#    --labelList \
#        "udsg jets from QCD (ROC_{60})" \
#        "udsg jets from QCD (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "Jet p_{T} [GeV]" \
#    --yTitle "Mis-id. probability" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 1e-6 \
#    --yMax 1 \
#    --logY \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{lep} (from t#bar{t}) vs. udsg (from QCD) jets" \
#    --outFileName "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1/misId_vs_reco-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


 ############################## network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 ##############################

#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had}_{L} from W'_{3TeV} (ROC_{60})" \
#        "t^{had}_{R} from W'_{3TeV} (ROC_{60})" \
#        "t^{had}_{L} from W'_{3TeV} (ROC_{80})" \
#        "t^{had}_{R} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had}_{gen} p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT_LR" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.7030" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.4374" \
#    --cutDenList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had} from W'_{3TeV} (ROC_{60})" \
#        "t^{had} from W'_{3TeV} (ROC_{80})" \
#        "t^{had} from t#bar{t} (ROC_{60})" \
#        "t^{had} from t#bar{t} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had}_{gen} p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.7030" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.4374" \
#    --cutDenList \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had} jet from W'_{3TeV} (ROC_{60})" \
#        "t^{had} jet from W'_{3TeV} (ROC_{80})" \
#        "t^{had} jet from t#bar{t} (ROC_{60})" \
#        "t^{had} jet from t#bar{t} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had} jet p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1/eff_vs_reco-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hadTop_E_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_E_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_E_truth" \
#        "hadTop_E_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_E_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_E_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hadTop_E_truth > 200" \
#        "hadTop_E_truth > 200" \
#    --labelList \
#        "t^{had} from W'_{3TeV} (ROC_{60})" \
#        "t^{had} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "t^{had}_{gen} E [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-E" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hepTop_pT_reco > 200" \
#        "hepTop_pT_reco > 200" \
#    --labelList \
#        "udsg jets from QCD (ROC_{60})" \
#        "udsg jets from QCD (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "Jet p_{T} [GeV]" \
#    --yTitle "Mis-id. probability" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 1e-6 \
#    --yMax 1 \
#    --logY \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1/misId_vs_reco-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ############################## network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting ##############################
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#    --plotNumList \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8747" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8747" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had}_{L} from W'_{3TeV} (ROC_{60})" \
#        "t^{had}_{R} from W'_{3TeV} (ROC_{60})" \
#        "t^{had}_{L} from W'_{3TeV} (ROC_{80})" \
#        "t^{had}_{R} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had}_{gen} p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting/eff_vs_gen-pT_LR" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#    --plotNumList \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8747" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had} from W'_{3TeV} (ROC_{60})" \
#        "t^{had} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "t^{had}_{gen} p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting/eff_vs_gen-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8747" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hepTop_pT_reco > 200" \
#        "hepTop_pT_reco > 200" \
#    --labelList \
#        "udsg jets from QCD (ROC_{60})" \
#        "udsg jets from QCD (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "Jet p_{T} [GeV]" \
#    --yTitle "Mis-id. probability" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 1e-6 \
#    --yMax 1 \
#    --logY \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{3TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting/misId_vs_reco-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ############################## network_Wprime-1TeV-had_vs_qcd_nLayer-3_CNN-1 ##############################
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_1TeV_had \
#        l_ntupleFile_Wprime_1TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#    --extraDirSuffixList \
#        network_Wprime-1TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-1TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-1TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-1TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8464" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6709" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.7488" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.4992" \
#    --cutDenList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had} from W'_{1TeV} (ROC_{60})" \
#        "t^{had} from W'_{1TeV} (ROC_{80})" \
#        "t^{had} from W'_{3TeV} (ROC_{60})" \
#        "t^{had} from W'_{3TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had}_{gen} p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from W'_{1TeV}) vs. udsg (from QCD) jets" \
#    --outFileName "network_Wprime-1TeV-had_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



# ############################## network_ttbar-had_vs_qcd_nLayer-3_CNN-1 ##############################
#
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#    --extraDirSuffixList \
#        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
#    --plotDenList \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#        "hadTop_pT_truth" \
#    --cutNumList \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8655" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.7017" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8342" \
#        "hepTop_nearestGenHadTop_index >= 0 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6237" \
#    --cutDenList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had} from t#bar{t} (ROC_{60})" \
#        "t^{had} from t#bar{t} (ROC_{80})" \
#        "t^{had} from W\'_{3 TeV} (ROC_{60})" \
#        "t^{had} from W\'_{3 TeV} (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had}_{gen} p_{T} [GeV]" \
#    --yTitle "Efficiency" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from t#bar{t}) vs. udsg (from QCD) jets" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/eff_vs_gen-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8655" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.7017" \
#    --cutDenList \
#        "hepTop_pT_reco > 200" \
#        "hepTop_pT_reco > 200" \
#    --labelList \
#        "udsg jets from QCD (ROC_{60})" \
#        "udsg jets from QCD (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "Jet p_{T} [GeV]" \
#    --yTitle "Mis-id. probability" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 1e-6 \
#    --yMax 1 \
#    --logY \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "CNN trn.: t^{had} (from t#bar{t}) vs. udsg (from QCD) jets" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/misId_vs_reco-pT" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#        network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.8514" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_CNN_reco > 0.6561" \
#    --cutDenList \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "udsg jets from QCD (ROC_{60})" \
#        "udsg jets from QCD (ROC_{80})" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "Jet p_{T} [GeV]" \
#    --yTitle "Mis-id. probability" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 1e-3 \
#    --yMax 1 \
#    --logY \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --title "t^{had} vs. udsg jet CNN" \
#    --outFileName "misId_vs_reco-pT_hadTop-vs-qcd_Wprime-3TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


 ############################## nProngFraction ##############################

cmdStr = """ \
    python -u plotEfficiency.py \
    --processList \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_3TeV_lep \
    --plotNumList \
        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
    --plotDenList \
        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
        "hadTop_pT_truth[hepTop_nearestGenHadTop_index]" \
        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
        "lepTopVis_pT_truth[hepTop_nearestGenLepTop_index]" \
    --cutNumList \
        "hepTop_nearestGenHadTop_index >= 0 && hadTop_pT_truth[hepTop_nearestGenHadTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 3" \
        "hepTop_nearestGenHadTop_index >= 0 && hadTop_pT_truth[hepTop_nearestGenHadTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 3" \
        "hepTop_nearestGenLepTop_index >= 0 && lepTopVis_pT_truth[hepTop_nearestGenLepTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 2" \
        "hepTop_nearestGenLepTop_index >= 0 && lepTopVis_pT_truth[hepTop_nearestGenLepTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 2" \
    --cutDenList \
        "hepTop_nearestGenHadTop_index >= 0 && hadTop_pT_truth[hepTop_nearestGenHadTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco" \
        "hepTop_nearestGenHadTop_index >= 0 && hadTop_pT_truth[hepTop_nearestGenHadTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco" \
        "hepTop_nearestGenLepTop_index >= 0 && lepTopVis_pT_truth[hepTop_nearestGenLepTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco" \
        "hepTop_nearestGenLepTop_index >= 0 && lepTopVis_pT_truth[hepTop_nearestGenLepTop_index] > 200 && hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco" \
    --labelList \
        "t^{had} jet from #tilde{t}#bar{#tilde{t}}" \
        "t^{had} jet from W\'_{3 TeV}" \
        "t^{lep} jet from #tilde{t}#bar{#tilde{t}}" \
        "t^{lep} jet from W\'_{3 TeV}" \
    --lineColorList \
        2 \
        2 \
        4 \
        4 \
    --lineStyleList \
        1 \
        7 \
        1 \
        7 \
    --xTitle "t^{had/lep}_{gen} p^{vis}_{T} [GeV]" \
    --yTitle "Fraction" \
    --xMin 0 \
    --xMax 2000 \
    --nBinX 40 \
    --xMinDraw 200 \
    --xMaxDraw 1400 \
    --yMin 0 \
    --yMax 1 \
    --divX 4 2 5 \
    --axisMaxDigits 4 \
    --legendTextSize 0.03 \
    --title "Fraction of reco-jets capturing all the prongs" \
    --outFileName "nProngFraction_vs_gen-pT" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)


cmdStr = """ \
    python -u plotEfficiency.py \
    --processList \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_3TeV_lep \
    --plotNumList \
        "hepTop_pT_reco" \
        "hepTop_pT_reco" \
        "hepTop_pT_reco" \
        "hepTop_pT_reco" \
    --plotDenList \
        "hepTop_pT_reco" \
        "hepTop_pT_reco" \
        "hepTop_pT_reco" \
        "hepTop_pT_reco" \
    --cutNumList \
        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 3" \
        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 3" \
        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 2" \
        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 2" \
    --cutDenList \
        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco" \
        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco" \
        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco" \
        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco" \
    --labelList \
        "t^{had} jet from #tilde{t}#bar{#tilde{t}}" \
        "t^{had} jet from W\'_{3 TeV}" \
        "t^{lep} jet from #tilde{t}#bar{#tilde{t}}" \
        "t^{lep} jet from W\'_{3 TeV}" \
    --lineColorList \
        2 \
        2 \
        4 \
        4 \
    --lineStyleList \
        1 \
        7 \
        1 \
        7 \
    --xTitle "t^{had/lep} jet p_{T} [GeV]" \
    --yTitle "Fraction" \
    --xMin 0 \
    --xMax 2000 \
    --nBinX 40 \
    --xMinDraw 200 \
    --xMaxDraw 1400 \
    --yMin 0 \
    --yMax 1 \
    --divX 4 2 5 \
    --axisMaxDigits 4 \
    --legendTextSize 0.03 \
    --title "Fraction of AK15 jets capturing all visible prongs" \
    --outFileName "nProngFraction_vs_reco-pT" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)


#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_lep \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_nGenTopConstiMatched_reco == 3" \
#        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3 && hepTop_nGenTopConstiMatched_reco == 2" \
#    --cutDenList \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had} jet from W\'_{3 TeV}" \
#        "t^{lep} jet from W\'_{3 TeV}" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --xTitle "t^{had/lep} jet p_{T} [GeV]" \
#    --yTitle "Fraction" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --legendTextSize 0.05 \
#    --title "Fraction of AK15 jets capturing all visible prongs" \
#    --outFileName "nProngFraction_vs_reco-pT_Wprime-3TeV_nExcSubJet-geq-3" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --processList \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#    --plotNumList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --plotDenList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutNumList \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 3" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 3" \
#        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 2" \
#        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_nGenTopConstiMatched_reco == 2" \
#    --cutDenList \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco > 200 && hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco" \
#        "hepTop_pT_reco > 200 && hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco" \
#    --labelList \
#        "t^{had}_{L} jet from W\'_{3 TeV}" \
#        "t^{had}_{R} jet from W\'_{3 TeV}" \
#        "t^{lep}_{L} jet from W\'_{3 TeV}" \
#        "t^{lep}_{R} jet from W\'_{3 TeV}" \
#    --lineColorList \
#        2 \
#        4 \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#        7 \
#        7 \
#    --xTitle "t^{had/lep} jet p_{T} [GeV]" \
#    --yTitle "Fraction" \
#    --xMin 0 \
#    --xMax 2000 \
#    --nBinX 40 \
#    --xMinDraw 200 \
#    --xMaxDraw 1400 \
#    --yMin 0 \
#    --yMax 1 \
#    --divX 4 2 5 \
#    --axisMaxDigits 4 \
#    --legendTextSize 0.05 \
#    --title "Fraction of AK15 jets capturing all visible prongs" \
#    --outFileName "nProngFraction_vs_reco-pT_Wprime-3TeV-LR" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)




# Close the pool and wait for jobs to complete
pool.close()
pool.join()

for iJob, job in enumerate(l_job) :
    
    job.get()
