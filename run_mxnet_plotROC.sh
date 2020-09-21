#!/usr/bin/env python

#####!/home/sobhatta/opt/anaconda3/bin/python


import multiprocessing
import os


#nCPU = int(0.9*multiprocessing.cpu_count())
nCPU = 4

pool = multiprocessing.Pool(processes = nCPU)
l_job = []


l_pTbin_had = [200, 400, 600, 800, 1000]
l_pTbin_lep = [200, 400, 600, 800, 1000]


def cleanSpaces(string) :
    
    while ("  " in string) :
        
        string = string.replace("  ", " ")
    
    return string


 ########## network_stop-had_LvsR_nLayer-3_CNN-1

##for iBin in range(-1, len(l_pTbin_had)) :
#for iBin in range(-1, 0) :
#    
#    extraCutSig = "hepTop_nExcSubJet_reco >= 3"
#    extraCutBkg = "hepTop_nExcSubJet_reco >= 3"
#    
#    extraDetail = ""
#    
#    outFileSuffix = ""
#    
#    if (iBin >= 0) :
#        
#        extraCutSig = "\
#            hepTop_nearestGenHadTop_index >= 0 and \
#            hadTop_pT_truth[hepTop_nearestGenHadTop_index] > %f \
#        "%(
#            l_pTbin_had[iBin],
#        )
#        
#        extraCutSig = "%s and %s" %(extraCutSig, extraCutSig_temp)
#        
#        extraDetail = "%s < t^{had}_{gen} p_{T} [GeV]" %(l_pTbin_had[iBin])
#        
#        outFileSuffix = "_pT-%s" %(str(l_pTbin_had[iBin]))
#        
#        if (iBin < len(l_pTbin_had)-1) :
#            
#            extraCutSig = "\
#                %s and \
#                hadTop_pT_truth[hepTop_nearestGenHadTop_index] < %f \
#            "%(
#                extraCutSig,
#                l_pTbin_had[iBin+1],
#            )
#            
#            extraDetail = "%s < %s" %(extraDetail, str(l_pTbin_had[iBin+1]))
#            
#            outFileSuffix = "%s-%s" %(outFileSuffix, str(l_pTbin_had[iBin+1]))
#        
#        
#        extraCutBkg = extraCutSig
#    
#    
#    #cmdStr = """ \
#    #    python -u mxnet_plotROC.py \
#    #    --training stop-had_LvsR_nLayer-3 \
#    #    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    #    --epoch 25 \
#    #    --nEventMax 400000 \
#    #    --splitEvery 20000 \
#    #    --sigFiles l_ntupleFile_stop_L \
#    #    --bkgFiles l_ntupleFile_stop_R \
#    #    --extraCutSig "%s" \
#    #    --extraCutBkg "%s" \
#    #    --trainDetailSig "CNN Trn. sig.: t^{had}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    #    --trainDetailBkg "CNN Trn. bkg.: t^{had}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    #    --evalDetailSig  "CNN Eval. sig.: t^{had}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    #    --evalDetailBkg  "CNN Eval. bkg.: t^{had}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    #    --detailPos 0.05 3e-5 \
#    #    --extraDetailsStr "%s" \
#    #    --extraDetailsPos %s \
#    #    --outFileSuffix "%s" \
#    #""" %(
#    #    extraCutSig,
#    #    extraCutBkg,
#    #    extraDetail,
#    #    "0.4 2e-2",
#    #    outFileSuffix
#    #)
#    #
#    #cmdStr = cleanSpaces(cmdStr)
#    ##os.system(cmdStr)
#    #
#    #job = pool.apply_async(os.system, (), dict(command = cmdStr))
#    #l_job.append(job)
#    
#    
#    ##cmdStr = """ \
#    ##    python -u mxnet_plotROC.py \
#    ##    --training stop-had_LvsR_nLayer-3 \
#    ##    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    ##    --epoch 25 \
#    ##    --nEventMax 400000 \
#    ##    --splitEvery 20000 \
#    ##    --sigFiles l_ntupleFile_stop_L \
#    ##    --bkgFiles l_ntupleFile_stop_R \
#    ##    --extraCutSig "%s" \
#    ##    --extraCutBkg "%s" \
#    ##    --trainDetailSig "CNN Trn. sig.: t^{had}_{L} MBT-jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    ##    --trainDetailBkg "CNN Trn. bkg.: t^{had}_{R} MBT-jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    ##    --evalDetailSig  "CNN Eval. sig.: t^{had}_{L} MBT-jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    ##    --evalDetailBkg  "CNN Eval. bkg.: t^{had}_{R} MBT-jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    ##    --detailPos 0.05 3e-5 \
#    ##    --extraDetailsStr "%s" \
#    ##    --extraDetailsPos %s \
#    ##    --outFileSuffix "%s_with-isMayBeTop" \
#    ##""" %(
#    ##    extraCutSig,
#    ##    extraCutBkg,
#    ##    extraDetail,
#    ##    "0.4 2e-2",
#    ##    outFileSuffix
#    ##)
#    ##
#    ##cmdStr = cleanSpaces(cmdStr)
#    ##os.system(cmdStr)
#    
#    
#    cmdStr = """ \
#        python -u mxnet_plotROC.py \
#        --training stop-had_LvsR_nLayer-3 \
#        --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#        --epoch 25 \
#        --nEventMax 400000 \
#        --splitEvery 20000 \
#        --sigFiles l_ntupleFile_Wprime_1TeV_L_had \
#        --bkgFiles l_ntupleFile_Wprime_1TeV_R_had \
#        --extraCutSig "%s" \
#        --extraCutBkg "%s" \
#        --trainDetailSig "CNN Trn. sig.: t^{had}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#        --trainDetailBkg "CNN Trn. bkg.: t^{had}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#        --evalDetailSig  "CNN Eval. sig.: t^{had}_{L} jets from W'_{L}_{1 TeV}" \
#        --evalDetailBkg  "CNN Eval. bkg.: t^{had}_{R} jets from W'_{R}_{1 TeV}" \
#        --detailPos 0.05 3e-5 \
#        --extraDetailsStr "%s" \
#        --extraDetailsPos %s \
#        --outFileSuffix "%s_eval-Wprime-1TeV" \
#    """ %(
#        extraCutSig,
#        extraCutBkg,
#        extraDetail,
#        "0.4 2e-2",
#        outFileSuffix
#    )
#    
#    cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)
#    
#    job = pool.apply_async(os.system, (), dict(command = cmdStr))
#    l_job.append(job)
#    
#    
#    ##cmdStr = """ \
#    ##    python -u mxnet_plotROC.py \
#    ##    --training stop-had_LvsR_nLayer-3 \
#    ##    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    ##    --epoch 25 \
#    ##    --nEventMax 400000 \
#    ##    --splitEvery 20000 \
#    ##    --sigFiles l_ntupleFile_Wprime_1TeV_L_had \
#    ##    --bkgFiles l_ntupleFile_Wprime_1TeV_R_had \
#    ##    --extraCutSig "%s" \
#    ##    --extraCutBkg "%s" \
#    ##    --trainDetailSig "CNN Trn. sig.: t^{had}_{L} MBT-jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    ##    --trainDetailBkg "CNN Trn. bkg.: t^{had}_{R} MBT-jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    ##    --evalDetailSig  "CNN Eval. sig.: t^{had}_{L} MBT-jets from W'_{L}_{1 TeV}" \
#    ##    --evalDetailBkg  "CNN Eval. bkg.: t^{had}_{R} MBT-jets from W'_{R}_{1 TeV}" \
#    ##    --detailPos 0.05 3e-5 \
#    ##    --extraDetailsStr "%s" \
#    ##    --extraDetailsPos %s \
#    ##    --outFileSuffix "%s_with-isMayBeTop_eval-Wprime-1TeV" \
#    ##""" %(
#    ##    extraCutSig,
#    ##    extraCutBkg,
#    ##    extraDetail,
#    ##    "0.4 2e-2",
#    ##    outFileSuffix
#    ##)
#    ##
#    ##cmdStr = cleanSpaces(cmdStr)
#    ##os.system(cmdStr)
#    
#    
#    #cmdStr = """ \
#    #    python -u mxnet_plotROC.py \
#    #    --training stop-had_LvsR_nLayer-3 \
#    #    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    #    --epoch 25 \
#    #    --nEventMax 400000 \
#    #    --splitEvery 20000 \
#    #    --sigFiles l_ntupleFile_Wprime_3TeV_L_had \
#    #    --bkgFiles l_ntupleFile_Wprime_3TeV_R_had \
#    #    --extraCutSig "%s" \
#    #    --extraCutBkg "%s" \
#    #    --trainDetailSig "CNN Trn. sig.: t^{had}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    #    --trainDetailBkg "CNN Trn. bkg.: t^{had}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    #    --evalDetailSig  "CNN Eval. sig.: t^{had}_{L} jets from W'_{L}_{3 TeV}" \
#    #    --evalDetailBkg  "CNN Eval. bkg.: t^{had}_{R} jets from W'_{R}_{3 TeV}" \
#    #    --detailPos 0.05 3e-5 \
#    #    --extraDetailsStr "%s" \
#    #    --extraDetailsPos %s \
#    #    --outFileSuffix "%s_eval-Wprime-3TeV" \
#    #""" %(
#    #    extraCutSig,
#    #    extraCutBkg,
#    #    extraDetail,
#    #    "0.4 2e-2",
#    #    outFileSuffix
#    #)
#    #
#    #cmdStr = cleanSpaces(cmdStr)
#    ##os.system(cmdStr)
#    #
#    #job = pool.apply_async(os.system, (), dict(command = cmdStr))
#    #l_job.append(job)
#    
#    
#    ##cmdStr = """ \
#    ##    python -u mxnet_plotROC.py \
#    ##    --training stop-had_LvsR_nLayer-3 \
#    ##    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    ##    --epoch 25 \
#    ##    --nEventMax 400000 \
#    ##    --splitEvery 20000 \
#    ##    --sigFiles l_ntupleFile_Wprime_3TeV_L_had \
#    ##    --bkgFiles l_ntupleFile_Wprime_3TeV_R_had \
#    ##    --extraCutSig "%s" \
#    ##    --extraCutBkg "%s" \
#    ##    --trainDetailSig "CNN Trn. sig.: t^{had}_{L} MBT-jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    ##    --trainDetailBkg "CNN Trn. bkg.: t^{had}_{R} MBT-jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    ##    --evalDetailSig  "CNN Eval. sig.: t^{had}_{L} MBT-jets from W'_{L}_{3 TeV}" \
#    ##    --evalDetailBkg  "CNN Eval. bkg.: t^{had}_{R} MBT-jets from W'_{R}_{3 TeV}" \
#    ##    --detailPos 0.05 3e-5 \
#    ##    --extraDetailsStr "%s" \
#    ##    --extraDetailsPos %s \
#    ##    --outFileSuffix "%s_with-isMayBeTop_eval-Wprime-3TeV" \
#    ##""" %(
#    ##    extraCutSig,
#    ##    extraCutBkg,
#    ##    extraDetail,
#    ##    "0.4 2e-2",
#    ##    outFileSuffix
#    ##)
#    ##
#    ##cmdStr = cleanSpaces(cmdStr)
#    ##os.system(cmdStr)



##for iBin in range(-1, len(l_pTbin_lep)) :
#for iBin in range(-1, 0) :
#    
#    extraCutSig = "hepTop_nExcSubJet_reco >= 3"
#    extraCutBkg = "hepTop_nExcSubJet_reco >= 3"
#    
#    extraDetail = ""
#    
#    outFileSuffix = ""
#    
#    if (iBin >= 0) :
#        
#        extraCutSig_temp = "\
#            hepTop_nearestGenLepTop_index >= 0 and \
#            lepTopVis_pT_truth[hepTop_nearestGenLepTop_index] > %f \
#        "%(
#            l_pTbin_lep[iBin],
#        )
#        
#        extraCutSig = "%s and %s" %(extraCutSig, extraCutSig_temp)
#        
#        extraDetail = "%s < t^{lep}_{gen} p_{T} [GeV]" %(l_pTbin_lep[iBin])
#        
#        outFileSuffix = "_pT-%s" %(str(l_pTbin_lep[iBin]))
#        
#        if (iBin < len(l_pTbin_lep)-1) :
#            
#            extraCutSig = "\
#                %s and \
#                lepTopVis_pT_truth[hepTop_nearestGenLepTop_index] < %f \
#            "%(
#                extraCutSig,
#                l_pTbin_lep[iBin+1],
#            )
#            
#            extraDetail = "%s < %s" %(extraDetail, str(l_pTbin_lep[iBin+1]))
#            
#            outFileSuffix = "%s-%s" %(outFileSuffix, str(l_pTbin_lep[iBin+1]))
#        
#        
#        extraCutBkg = extraCutSig
#    
#    
#     ########## network_stop-lep_LvsR_nLayer-3_CNN-1
#    cmdStr = """ \
#        python -u mxnet_plotROC.py \
#        --training stop-lep_LvsR_nLayer-3 \
#        --trainingDirName network_stop-lep_LvsR_nLayer-3_CNN-1 \
#        --epoch 25 \
#        --nEventMax 400000 \
#        --splitEvery 20000 \
#        --sigFiles l_ntupleFile_stop_L \
#        --bkgFiles l_ntupleFile_stop_R \
#        --extraCutSig "%s" \
#        --extraCutBkg "%s" \
#        --trainDetailSig "CNN Trn. sig.: t^{lep}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#        --trainDetailBkg "CNN Trn. bkg.: t^{lep}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#        --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#        --evalDetailBkg  "CNN Eval. bkg.: t^{lep}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#        --detailPos 0.05 3e-5 \
#        --extraDetailsStr "%s" \
#        --extraDetailsPos %s \
#        --outFileSuffix "%s" \
#    """ %(
#        extraCutSig,
#        extraCutBkg,
#        extraDetail,
#        "0.4 2e-2",
#        outFileSuffix
#    )
#    
#    cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)
#    
#    job = pool.apply_async(os.system, (), dict(command = cmdStr))
#    l_job.append(job)
#    
#    
#    cmdStr = """ \
#        python -u mxnet_plotROC.py \
#        --training stop-lep_LvsR_nLayer-3 \
#        --trainingDirName network_stop-lep_LvsR_nLayer-3_CNN-1 \
#        --epoch 25 \
#        --nEventMax 400000 \
#        --splitEvery 20000 \
#        --sigFiles l_ntupleFile_Wprime_1TeV_L_lep \
#        --bkgFiles l_ntupleFile_Wprime_1TeV_R_lep \
#        --extraCutSig "%s" \
#        --extraCutBkg "%s" \
#        --trainDetailSig "CNN Trn. sig.: t^{lep}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#        --trainDetailBkg "CNN Trn. bkg.: t^{lep}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#        --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from W'_{L}_{1 TeV}" \
#        --evalDetailBkg  "CNN Eval. bkg.: t^{lep}_{R} jets from W'_{R}_{1 TeV}" \
#        --detailPos 0.05 3e-5 \
#        --extraDetailsStr "%s" \
#        --extraDetailsPos %s \
#        --outFileSuffix "%s_eval-Wprime-1TeV" \
#    """ %(
#        extraCutSig,
#        extraCutBkg,
#        extraDetail,
#        "0.4 2e-2",
#        outFileSuffix
#    )
#    
#    cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)
#    
#    job = pool.apply_async(os.system, (), dict(command = cmdStr))
#    l_job.append(job)
#    
#    
#    cmdStr = """ \
#        python -u mxnet_plotROC.py \
#        --training stop-lep_LvsR_nLayer-3 \
#        --trainingDirName network_stop-lep_LvsR_nLayer-3_CNN-1 \
#        --epoch 25 \
#        --nEventMax 400000 \
#        --splitEvery 20000 \
#        --sigFiles l_ntupleFile_Wprime_3TeV_L_lep \
#        --bkgFiles l_ntupleFile_Wprime_3TeV_R_lep \
#        --extraCutSig "%s" \
#        --extraCutBkg "%s" \
#        --trainDetailSig "CNN Trn. sig.: t^{lep}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#        --trainDetailBkg "CNN Trn. bkg.: t^{lep}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#        --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from W'_{L}_{3 TeV}" \
#        --evalDetailBkg  "CNN Eval. bkg.: t^{lep}_{R} jets from W'_{R}_{3 TeV}" \
#        --detailPos 0.05 3e-5 \
#        --extraDetailsStr "%s" \
#        --extraDetailsPos %s \
#        --outFileSuffix "%s_eval-Wprime-3TeV" \
#    """ %(
#        extraCutSig,
#        extraCutBkg,
#        extraDetail,
#        "0.4 2e-2",
#        outFileSuffix
#    )
#    
#    cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)
#    
#    job = pool.apply_async(os.system, (), dict(command = cmdStr))
#    l_job.append(job)
#    
#    
#    # ########## network_Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1
#    #cmdStr = """ \
#    #    python -u mxnet_plotROC.py \
#    #    --training Wprime-3TeV-lep_LvsR_nLayer-3 \
#    #    --trainingDirName network_Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1 \
#    #    --epoch 25 \
#    #    --nEventMax 400000 \
#    #    --splitEvery 20000 \
#    #    --sigFiles l_ntupleFile_Wprime_3TeV_L_lep \
#    #    --bkgFiles l_ntupleFile_Wprime_3TeV_R_lep \
#    #    --extraCutSig "%s" \
#    #    --extraCutBkg "%s" \
#    #    --trainDetailSig "CNN Trn. sig.: t^{lep}_{L} jets from W'_{L}_{3 TeV}" \
#    #    --trainDetailBkg "CNN Trn. bkg.: t^{lep}_{R} jets from W'_{R}_{3 TeV}" \
#    #    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from W'_{L}_{3 TeV}" \
#    #    --evalDetailBkg  "CNN Eval. bkg.: t^{lep}_{R} jets from W'_{R}_{3 TeV}" \
#    #    --detailPos 0.05 3e-5 \
#    #    --extraDetailsStr "%s" \
#    #    --extraDetailsPos %s \
#    #    --outFileSuffix "%s" \
#    #""" %(
#    #    extraCutSig,
#    #    extraCutBkg,
#    #    extraDetail,
#    #    "0.4 2e-2",
#    #    outFileSuffix
#    #)
#    #
#    #cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)
#    #
#    #
#    #cmdStr = """ \
#    #    python -u mxnet_plotROC.py \
#    #    --training Wprime-3TeV-lep_LvsR_nLayer-3 \
#    #    --trainingDirName network_Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1 \
#    #    --epoch 25 \
#    #    --nEventMax 400000 \
#    #    --splitEvery 20000 \
#    #    --sigFiles l_ntupleFile_Wprime_1TeV_L_lep \
#    #    --bkgFiles l_ntupleFile_Wprime_1TeV_R_lep \
#    #    --extraCutSig "%s" \
#    #    --extraCutBkg "%s" \
#    #    --trainDetailSig "CNN Trn. sig.: t^{lep}_{L} jets from W'_{L}_{3 TeV}" \
#    #    --trainDetailBkg "CNN Trn. bkg.: t^{lep}_{R} jets from W'_{R}_{3 TeV}" \
#    #    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from W'_{L}_{1 TeV}" \
#    #    --evalDetailBkg  "CNN Eval. bkg.: t^{lep}_{R} jets from W'_{R}_{1 TeV}" \
#    #    --detailPos 0.05 3e-5 \
#    #    --extraDetailsStr "%s" \
#    #    --extraDetailsPos %s \
#    #    --outFileSuffix "%s_eval-Wprime-1TeV" \
#    #""" %(
#    #    extraCutSig,
#    #    extraCutBkg,
#    #    extraDetail,
#    #    "0.4 2e-2",
#    #    outFileSuffix
#    #)
#    #
#    #cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)
#    #
#    #
#    #cmdStr = """ \
#    #    python -u mxnet_plotROC.py \
#    #    --training Wprime-3TeV-lep_LvsR_nLayer-3 \
#    #    --trainingDirName network_Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1 \
#    #    --epoch 25 \
#    #    --nEventMax 400000 \
#    #    --splitEvery 20000 \
#    #    --sigFiles l_ntupleFile_stop_L \
#    #    --bkgFiles l_ntupleFile_stop_R \
#    #    --extraCutSig "%s" \
#    #    --extraCutBkg "%s" \
#    #    --trainDetailSig "CNN Trn. sig.: t^{lep}_{L} jets from W'_{L}_{3 TeV}" \
#    #    --trainDetailBkg "CNN Trn. bkg.: t^{lep}_{R} jets from W'_{R}_{3 TeV}" \
#    #    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L}" \
#    #    --evalDetailBkg  "CNN Eval. bkg.: t^{lep}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R}" \
#    #    --detailPos 0.05 3e-5 \
#    #    --extraDetailsStr "%s" \
#    #    --extraDetailsPos %s \
#    #    --outFileSuffix "%s_eval-stop" \
#    #""" %(
#    #    extraCutSig,
#    #    extraCutBkg,
#    #    extraDetail,
#    #    "0.4 2e-2",
#    #    outFileSuffix
#    #)
#    #
#    #cmdStr = cleanSpaces(cmdStr)
#    #os.system(cmdStr)


# ########## network_ttbar-had_vs_qcd_nLayer-3_CNN-1
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 3e-5 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


cmdStr = """ \
    python -u mxnet_plotROC.py \
    --trainings \
        ttbar-had_vs_qcd_nLayer-3 \
        ttbar-had_vs_qcd_nLayer-3 \
        ttbar-lep_vs_qcd_nLayer-3 \
        ttbar-lep_vs_qcd_nLayer-3 \
    --trainingDirNames \
        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
        network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
        network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
        network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
    --epochs \
        25 \
        25 \
        25 \
        25 \
    --nEventMaxs \
        376000 \
        376000 \
        350000 \
        350000 \
    --splitEverys \
        20000 \
        20000 \
        20000 \
        20000 \
    --sigFiles \
        l_ntupleFile_ttbar \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_ttbar \
        l_ntupleFile_Wprime_3TeV_lep \
    --bkgFiles \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
    --extraCutsSig \
        "hepTop_nExcSubJet_reco >= 3" \
        "hepTop_nExcSubJet_reco >= 3" \
        "hepTop_nExcSubJet_reco >= 3" \
        "hepTop_nExcSubJet_reco >= 3" \
    --extraCutsBkg \
        "hepTop_nExcSubJet_reco >= 3" \
        "hepTop_nExcSubJet_reco >= 3" \
        "hepTop_nExcSubJet_reco >= 3" \
        "hepTop_nExcSubJet_reco >= 3" \
    --lineColors \
        2 \
        2 \
        4 \
        4 \
    --lineStyles \
        1 \
        7 \
        1 \
        7 \
    --labels \
        "t^{had} (t#bar{t}) vs. udsg (QCD) CNN" \
        "t^{had} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
        "t^{lep} (t#bar{t}) vs. udsg (QCD) CNN" \
        "t^{lep} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
    --legendPos "LL" \
    --trainDetailSig "" \
    --trainDetailBkg "" \
    --evalDetailSig "" \
    --evalDetailBkg "" \
    --outDir "plots/ROC" \
    --outFileName "ROC_network_ttbar-had-lep_vs_qcd_nLayer-3_CNN-1" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)



#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



###cmdStr = """ \
###    python -u mxnet_plotROC.py \
###    --training ttbar-had_vs_qcd_nLayer-3 \
###    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
###    --epoch 25 \
###    --nEventMax 400000 \
###    --splitEvery 20000 \
###    --sigFiles l_ntupleFile_ttbar \
###    --bkgFiles l_ntupleFile_qcd \
###    --extraCutSig "hepTop_isMayBeTop_reco" \
###    --extraCutBkg "hepTop_isMayBeTop_reco" \
###    --trainDetailSig "CNN Trn. sig.: t^{had} jets from t#bar{t}" \
###    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
###    --evalDetailSig  "CNN Eval. sig.: t^{had} MBT-jets from t#bar{t}" \
###    --evalDetailBkg  "CNN Eval. bkg.: QCD MBT-jets" \
###    --detailPos 0.05 3e-5 \
###    --outFileSuffix "_with-isMayBeTop" \
###"""


#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_had \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 3e-5 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_had \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 3e-5 \
#    --outFileSuffix "_eval-Wprime-3TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ########## network_ttbar-lep_vs_qcd_nLayer-3_CNN-1
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-3TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_L_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-3TeV-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_R_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{R} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ########## network_ttbar_lep-vs-had_nLayer-3_CNN-1
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar_lep-vs-had_nLayer-3 \
#    --trainingDirName network_ttbar_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_ttbar \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: t^{had} jets from t#bar{t}" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: t^{had} jets from t#bar{t}" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar_lep-vs-had_nLayer-3 \
#    --trainingDirName network_ttbar_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_lep \
#    --bkgFiles l_ntupleFile_Wprime_1TeV_had \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: t^{had} jets from t#bar{t}" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: t^{had} jets from W\'_{1 TeV}" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training ttbar_lep-vs-had_nLayer-3 \
#    --trainingDirName network_ttbar_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles l_ntupleFile_Wprime_3TeV_had \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from t#bar{t}" \
#    --trainDetailBkg "CNN Trn. bkg.: t^{had} jets from t#bar{t}" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: t^{had} jets from W\'_{3 TeV}" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-3TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ########## network_Wprime-3TeV_lep-vs-had_nLayer-3_CNN-1
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV_lep-vs-had_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles l_ntupleFile_Wprime_3TeV_had \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: t^{had} jets from W\'_{3 TeV}" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: t^{had} jets from W\'_{3 TeV}" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV_lep-vs-had_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_lep \
#    --bkgFiles l_ntupleFile_Wprime_1TeV_had \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: t^{had} jets from W\'_{3 TeV}" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: t^{had} jets from W\'_{1 TeV}" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV_lep-vs-had_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_ttbar \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: t^{had} jets from W\'_{3 TeV}" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: t^{had} jets from t#bar{t}" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ########## network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_had \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_had \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ########## network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_had \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_had \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1_withPtEtaReweighting \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{had} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{had} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-ttbar" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


# ########## network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_L_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{L} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-3TeV-L" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_3TeV_R_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep}_{R} jets from W\'_{3 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-3TeV-R" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)


#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_Wprime_1TeV_lep \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from W\'_{1 TeV}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-Wprime-1TeV" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#cmdStr = """ \
#    python -u mxnet_plotROC.py \
#    --training Wprime-3TeV-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --nEventMax 400000 \
#    --splitEvery 20000 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --extraCutSig "hepTop_nExcSubJet_reco >= 3" \
#    --extraCutBkg "hepTop_nExcSubJet_reco >= 3" \
#    --trainDetailSig "CNN Trn. sig.: t^{lep} jets from W\'_{3 TeV}" \
#    --trainDetailBkg "CNN Trn. bkg.: udsg jets from QCD" \
#    --evalDetailSig  "CNN Eval. sig.: t^{lep} jets from t#bar{t}" \
#    --evalDetailBkg  "CNN Eval. bkg.: udsg jets from QCD" \
#    --detailPos 0.05 0.01 \
#    --outFileSuffix "_eval-ttbar" \
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
