#!/usr/bin/env python

import multiprocessing
import os


nCPU = 30

pool = multiprocessing.Pool(processes = nCPU)
l_job = []


def cleanSpaces(string) :
    
    while ("  " in string) :
        
        string = string.replace("  ", " ")
    
    return string



# #############################################################################################
# ######################################## ttbar (had) ########################################
# #############################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image from t#bar{t}" \
#    --outFileName "jetImage_hadTop_boosted_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image (tracks) from t#bar{t}" \
#    --outFileName "jetImage_hadTop_boosted_track_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image (photons) from t#bar{t}" \
#    --outFileName "jetImage_hadTop_boosted_photon_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image (neutral hadrons) from t#bar{t}" \
#    --outFileName "jetImage_hadTop_boosted_neutralHad_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image from t#bar{t}" \
#    --outFileName "jetImage_hadTop_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image (tracks) from t#bar{t}" \
#    --outFileName "jetImage_hadTop_track_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image (photons) from t#bar{t}" \
#    --outFileName "jetImage_hadTop_photon_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had} jet image (neutral hadrons) from t#bar{t}" \
#    --outFileName "jetImage_hadTop_neutralHad_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #############################################################################################
# ######################################## ttbar (lep) ########################################
# #############################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image from t#bar{t}" \
#    --outFileName "jetImage_lepTop_boosted_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image (tracks) from t#bar{t}" \
#    --outFileName "jetImage_lepTop_boosted_track_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image (photons) from t#bar{t}" \
#    --outFileName "jetImage_lepTop_boosted_photon_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image (neutral hadrons) from t#bar{t}" \
#    --outFileName "jetImage_lepTop_boosted_neutralHad_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
# 
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image from t#bar{t}" \
#    --outFileName "jetImage_lepTop_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image (tracks) from t#bar{t}" \
#    --outFileName "jetImage_lepTop_track_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image (photons) from t#bar{t}" \
#    --outFileName "jetImage_lepTop_photon_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_ttbar" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep} jet image (neutral hadrons) from t#bar{t}" \
#    --outFileName "jetImage_lepTop_neutralHad_ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ##############################################################################################
# ######################################## stop-L (had) ########################################
# ##############################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_track_stop-L" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_photon_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_neutralHad_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_track_stop-L" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_photon_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_neutralHad_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ##############################################################################################
# ######################################## stop-L (lep) ########################################
# ##############################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_track_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_photon_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_neutralHad_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_track_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_photon_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_L" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_neutralHad_stop-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ##############################################################################################
# ######################################## stop-R (had) ########################################
# ##############################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_track_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_photon_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_boosted_neutralHad_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_track_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_photon_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_hadTop_neutralHad_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ##############################################################################################
# ######################################## stop-R (lep) ########################################
# ##############################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_track_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_photon_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_boosted_neutralHad_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (tracks) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_track_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (photons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_photon_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_stop_R" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (neutral hadrons) from #tilde{t}#bar{#tilde{t}}" \
#    --outFileName "jetImage_lepTop_neutralHad_stop-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


 ##################################################################################################
 ######################################## Wprime-3TeV (had) #######################################
 ##################################################################################################

cmdStr = """ \
    python -u plotJetImage.py \
    --nEventMax 500000 \
    --process "l_ntupleFile_Wprime_3TeV_had" \
    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
    --xTitle "Image x-coordinate" \
    --yTitle "Image y-coordinate" \
    --zTitle "Fraction of jet energy" \
    --xMin -1 \
    --xMax +1 \
    --yMin -1 \
    --yMax +1 \
    --zMin 1e-6 \
    --zMax 1e-1 \
    --logZ \
    --title "t^{had} jet image from W\'_{3 TeV}" \
    --outFileName "jetImage_hadTop_boosted_Wprime-3TeV" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)


 #################### eta-phi plane ####################

cmdStr = """ \
    python -u plotJetImage.py \
    --nEventMax 500000 \
    --process "l_ntupleFile_Wprime_3TeV_had" \
    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
    --xTitle "Image x-coordinate" \
    --yTitle "Image y-coordinate" \
    --zTitle "Fraction of jet energy" \
    --xMin -1.5 \
    --xMax +1.5 \
    --yMin -1.5 \
    --yMax +1.5 \
    --zMin 1e-6 \
    --zMax 1e-1 \
    --logZ \
    --title "t^{had} jet image from W\'_{3 TeV}" \
    --outFileName "jetImage_hadTop_Wprime-3TeV" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)


# #####################################################################################################
# ######################################## Wprime-3TeV-L (had) ########################################
# #####################################################################################################
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_had" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_Wprime-3TeV-L" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_had" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (tracks) from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_track_Wprime-3TeV-L" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_had" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (photons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_photon_Wprime-3TeV-L" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{L} jet image (neutral hadrons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_neutralHad_Wprime-3TeV-L" \
#
#
# ###################################################################################################
# ######################################## Wprime-3TeV (lep) ########################################
# ###################################################################################################

cmdStr = """ \
    python -u plotJetImage.py \
    --nEventMax 500000 \
    --process "l_ntupleFile_Wprime_3TeV_lep" \
    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
    --xTitle "Image x-coordinate" \
    --yTitle "Image y-coordinate" \
    --zTitle "Fraction of jet energy" \
    --xMin -1 \
    --xMax +1 \
    --yMin -1 \
    --yMax +1 \
    --zMin 1e-6 \
    --zMax 1e-1 \
    --logZ \
    --title "t^{lep} jet image from W\'_{3 TeV}" \
    --outFileName "jetImage_lepTop_boosted_Wprime-3TeV-L" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)


 #################### eta-phi plane ####################

cmdStr = """ \
    python -u plotJetImage.py \
    --nEventMax 500000 \
    --process "l_ntupleFile_Wprime_3TeV_lep" \
    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
    --xTitle "Image x-coordinate" \
    --yTitle "Image y-coordinate" \
    --zTitle "Fraction of jet energy" \
    --xMin -1.5 \
    --xMax +1.5 \
    --yMin -1.5 \
    --yMax +1.5 \
    --zMin 1e-6 \
    --zMax 1e-1 \
    --logZ \
    --title "t^{lep} jet image from W\'_{3 TeV}" \
    --outFileName "jetImage_lepTop_Wprime-3TeV-L" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)


# #####################################################################################################
# ######################################## Wprime-3TeV-L (lep) ########################################
# #####################################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_lep" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_Wprime-3TeV-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_lep" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (tracks) from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_track_Wprime-3TeV-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_lep" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (photons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_photon_Wprime-3TeV-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_L_lep" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{L} jet image (neutral hadrons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_neutralHad_Wprime-3TeV-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
# 
# #####################################################################################################
# ######################################## Wprime-3TeV-R (had) ########################################
# #####################################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_had" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_had" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (tracks) from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_track_Wprime-3TeV-R" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_had" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (photons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_photon_Wprime-3TeV-R" \
#
#
#python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_had" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image (neutral hadrons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_boosted_neutralHad_Wprime-3TeV-R" \
#
#
# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_had" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{had}_{R} jet image from W\'_{3 TeV}" \
#    --outFileName "jetImage_hadTop_Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



# #####################################################################################################
# ######################################## Wprime-3TeV-R (lep) ########################################
# #####################################################################################################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_lep" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_lep" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (tracks) from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_track_Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_lep" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (photons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_photon_Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_Wprime_3TeV_R_lep" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "t^{lep}_{R} jet image (neutral hadrons) from W\'_{3 TeV}" \
#    --outFileName "jetImage_lepTop_boosted_neutralHad_Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


 #####################################################################################
 ######################################## QCD ########################################
 #####################################################################################

#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_boosted_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image from QCD" \
#    --outFileName "jetImage_boosted_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image (tracks) from QCD" \
#    --outFileName "jetImage_boosted_track_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image (photons) from QCD" \
#    --outFileName "jetImage_boosted_photon_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image (neutral hadrons) from QCD" \
#    --outFileName "jetImage_boosted_neutralHad_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# #################### eta-phi plane ####################
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image from QCD" \
#    --outFileName "jetImage_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_track_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image (tracks) from QCD" \
#    --outFileName "jetImage_track_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_photon_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image (photons) from QCD" \
#    --outFileName "jetImage_photon_qcd" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u plotJetImage.py \
#    --nEventMax 500000 \
#    --process "l_ntupleFile_qcd" \
#    --plotStr "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco" \
#    --cutStr "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "Image x-coordinate" \
#    --yTitle "Image y-coordinate" \
#    --zTitle "Fraction of jet energy" \
#    --xMin -1.5 \
#    --xMax +1.5 \
#    --yMin -1.5 \
#    --yMax +1.5 \
#    --zMin 1e-6 \
#    --zMax 1e-1 \
#    --logZ \
#    --title "udsg jet image (neutral hadrons) from QCD" \
#    --outFileName "jetImage_neutralHad_qcd" \
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
