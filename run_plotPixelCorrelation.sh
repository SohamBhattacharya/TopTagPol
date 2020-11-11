#!/usr/bin/env python

import multiprocessing
import os


nCPU = 4

pool = multiprocessing.Pool(processes = nCPU)
l_job = []


def cleanSpaces(string) :
    
    while ("  " in string) :
        
        string = string.replace("  ", " ")
    
    return string



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_ttbar" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --cutStr \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "preprocessed t^{had} jet from t#bar{t}" \
#    --outFileName "pixelCorr_h2_hepTop_boosted_fracE_phiEtaPlane_reco_with_hepTop_m_reco_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_ttbar" \
#    --processSuffix "_noSD" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --cutStr \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "preprocessed t^{had} jet (w/o soft-drop) from t#bar{t}" \
#    --outFileName "pixelCorr_h2_hepTop_boosted_fracE_phiEtaPlane_reco_with_hepTop_m_reco_ttbar_noSD" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_ttbar" \
#    --imageHistName "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --cutStr \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "unprocessed t^{had} jet from t#bar{t}" \
#    --outFileName "pixelCorr_h2_hepTop_fracE_phiEtaPlane_reco_with_hepTop_m_reco_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_ttbar" \
#    --processSuffix "_noSD" \
#    --imageHistName "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --cutStr \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "unprocessed t^{had} jet (w/o soft-drop) from t#bar{t}" \
#    --outFileName "pixelCorr_h2_hepTop_fracE_phiEtaPlane_reco_with_hepTop_m_reco_ttbar_noSD" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_qcd" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --cutStr \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "preprocessed udsg jet from QCD" \
#    --outFileName "pixelCorr_h2_hepTop_boosted_fracE_phiEtaPlane_reco_with_hepTop_m_reco_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_qcd" \
#    --processSuffix "_noSD" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --cutStr \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "preprocessed udsg jet (w/o soft-drop) from QCD" \
#    --outFileName "pixelCorr_h2_hepTop_boosted_fracE_phiEtaPlane_reco_with_hepTop_m_reco_qcd_noSD" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_qcd" \
#    --imageHistName "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --pixelScaleVar "hepTop_E_reco" \
#    --cutStr \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "unprocessed udsg jet from QCD" \
#    --outFileName "pixelCorr_h2_hepTop_fracE_phiEtaPlane_reco_with_hepTop_m_reco_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_qcd" \
#    --processSuffix "_noSD" \
#    --imageHistName "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_m_reco" \
#    --pixelScaleVar "hepTop_E_reco" \
#    --cutStr \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with m_{jet} [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "unprocessed udsg jet (w/o soft-drop) from QCD" \
#    --outFileName "pixelCorr_h2_hepTop_fracE_phiEtaPlane_reco_with_hepTop_m_reco_qcd_noSD" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 10000 \
#    --process "l_ntupleFile_ttbar" \
#    --extraDirSuffixes "network_ttbar-had_vs_qcd_nLayer-3-DetaDphi_CNN-1" \
#    --imageHistName "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_CNN_reco" \
#    --cutStr \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with t^{had}/QCD CNN [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "Unprocessed t^{had} jets from t#bar{t}" \
#    --outFileName "pixelCorr_hadTop_with_ttbar-had-vs-qcd_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --extraDirSuffixes "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_CNN_reco" \
#    --cutStr \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with t^{had}/QCD CNN [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "t^{had} jets from t#bar{t}" \
#    --outFileName "pixelCorr_hadTop-boosted_with_ttbar-had-vs-qcd_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --extraDirSuffixes "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_CNN_reco" \
#    --cutStr \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with t^{had}/QCD CNN [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "udsg jets from QCD" \
#    --outFileName "pixelCorr_hadTop-boosted_with_ttbar-had-vs-qcd_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --extraDirSuffixes "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_CNN_reco" \
#    --pixelScaleVar "1" \
#    --cutStr \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with t^{lep}/QCD CNN [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "t^{lep} jets from t#bar{t}" \
#    --outFileName "pixelCorr_lepTop-boosted_with_ttbar-lep-vs-qcd_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
#cmdStr = """ \
#    python -u plotPixelCorrelation.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --extraDirSuffixes "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#    --imageHistName "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --corrVar "hepTop_CNN_reco" \
#    --pixelScaleVar "hepTop_E_reco" \
#    --cutStr \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutVars \
#        "hepTop_genHadTop_deltaR_reco" \
#        "hepTop_genLepTop_deltaR_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_nExcSubJet_reco" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Corr. with t^{lep}/QCD CNN [%]" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin -100 \
#    --zMax +100 \
#    --title "udsg jets from QCD" \
#    --outFileName "pixelCorr_lepTop-boosted_with_ttbar-lep-vs-qcd_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



cmdStr = """ \
    python -u plotPixelCorrelation.py \
    --nEventMax 500000 \
    --process "l_ntupleFile_ttbar" \
    --extraDirSuffixes "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
    --imageHistName "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
    --corrVar "hepTop_CNN_reco" \
    --pixelScaleVar "hepTop_E_reco" \
    --cutStr \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --cutVars \
        "hepTop_genHadTop_deltaR_reco" \
        "hepTop_genLepTop_deltaR_reco" \
        "hepTop_pT_reco" \
        "hepTop_nExcSubJet_reco" \
    --xTitle "Image x-coordinate" \
    --yTitle "Image y-coordinate" \
    --zTitle "Corr. with t^{lep}/t^{had} CNN [%]" \
    --xMin -1.5 \
    --xMax +1.5 \
    --yMin -1.5 \
    --yMax +1.5 \
    --zMin -100 \
    --zMax +100 \
    --title "t^{lep}/t^{had} jets from t#bar{t}" \
    --outFileName "pixelCorr_lepTop-boosted_with_ttbar-lep-vs-had_ttbar" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)



cmdStr = """ \
    python -u plotPixelCorrelation.py \
    --nEventMax 500000 \
    --process "l_ntupleFile_ttbar" \
    --extraDirSuffixes "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
    --imageHistName "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
    --corrVar "hepTop_CNN_reco" \
    --pixelScaleVar "hepTop_E_reco" \
    --cutStr \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --cutVars \
        "hepTop_genHadTop_deltaR_reco" \
        "hepTop_genLepTop_deltaR_reco" \
        "hepTop_pT_reco" \
        "hepTop_nExcSubJet_reco" \
    --xTitle "Image x-coordinate" \
    --yTitle "Image y-coordinate" \
    --zTitle "Corr. with t^{lep}/t^{had} CNN [%]" \
    --xMin -1.5 \
    --xMax +1.5 \
    --yMin -1.5 \
    --yMax +1.5 \
    --zMin -100 \
    --zMax +100 \
    --title "t^{lep}/t^{had} jets from t#bar{t}" \
    --outFileName "pixelCorr_hadTop-boosted_with_ttbar-lep-vs-had_ttbar" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)



# Close the pool and wait for jobs to complete
pool.close()
pool.join()

for iJob, job in enumerate(l_job) :
    
    job.get()
