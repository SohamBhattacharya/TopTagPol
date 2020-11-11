#python -u plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles l_ntupleFile_stop_L \
#    --bkgFiles l_ntupleFile_stop_R \
#    --varROC "hepTop_cosThetaStar_reco" \
#    --cutSig "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --cutBkg "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3" \
#    --detailROC "ROC for cos#theta*" \
#    --detailSig "Sig.: t^{had}_{L} jets from #tilde{t}_{L}#bar{#tilde{t}}_{L} events" \
#    --detailBkg "Bkg.: t^{had}_{R} jets from #tilde{t}_{R}#bar{#tilde{t}}_{R} events" \
#    --detailPos 0.05 0.0001 \
#    --outFileName "cosThetaStar_stop-had_LvsR"


#python -u plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles l_ntupleFile_stop_L \
#    --bkgFiles l_ntupleFile_stop_R \
#    --varROC "hepTop_cosThetaStar_reco" \
#    --cutSig "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_isMayBeTop_reco" \
#    --cutBkg "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_isMayBeTop_reco" \
#    --detailROC "ROC for cos#theta*" \
#    --detailSig "Sig.: t^{had}_{L} MBT-jets from #tilde{t}_{L}#bar{#tilde{t}}_{L} events" \
#    --detailBkg "Bkg.: t^{had}_{R} MBT-jets from #tilde{t}_{R}#bar{#tilde{t}}_{R} events" \
#    --detailPos 0.05 0.0001 \
#    --outFileName "cosThetaStar_stop-had_LvsR_with-isMayBeTop"


python -u plotROC.py \
    --sigFiles \
        l_ntupleFile_ttbar \
        l_ntupleFile_ttbar \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_ttbar \
        l_ntupleFile_ttbar \
        l_ntupleFile_Wprime_3TeV_lep \
        l_ntupleFile_Wprime_3TeV_lep \
    --bkgFiles \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
        l_ntupleFile_qcd \
    --extraDirSuffixes \
        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
    --varsROC \
        "hepTop_CNN_reco" \
        "TMVAinfo/ttbar-had_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
        "hepTop_CNN_reco" \
        "TMVAinfo/ttbar-had_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
        "hepTop_CNN_reco" \
        "TMVAinfo/ttbar-lep_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
        "hepTop_CNN_reco" \
        "TMVAinfo/ttbar-lep_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
    --comparisons \
        ">" \
        ">" \
        ">" \
        ">" \
        ">" \
        ">" \
        ">" \
        ">" \
    --cutsSig \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --cutsBkg \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --nEventMaxs \
        -1 \
        -1 \
        -1 \
        -1 \
        -1 \
        -1 \
        -1 \
        -1 \
    --lineColors \
        2 \
        2 \
        2 \
        2 \
        4 \
        4 \
        4 \
        4 \
    --lineStyles \
        1 \
        3 \
        7 \
        10 \
        1 \
        3 \
        7 \
        10 \
    --labels \
        "t^{had} (t#bar{t}) vs. QCD (CNN)" \
        "t^{had} (t#bar{t}) vs. QCD (CNN+BDT)" \
        "t^{had} (W'_{3 TeV}) vs. QCD (CNN)" \
        "t^{had} (W'_{3 TeV}) vs. QCD (CNN+BDT)" \
        "t^{lep} (t#bar{t}) vs. QCD (CNN)" \
        "t^{lep} (t#bar{t}) vs. QCD (CNN+BDT)" \
        "t^{lep} (W'_{3 TeV}) vs. QCD (CNN)" \
        "t^{lep} (W'_{3 TeV}) vs. QCD (CNN+BDT)" \
    --legendPos "UL" \
    --legendHeightScale 0.9 \
    --yMin 1e-5 \
    --yMax 1e2 \
    --logY \
    --xTitle "Signal efficiency" \
    --yTitle "Background efficiency" \
    --omitAUC \
    --outFileName "network_ttbar-had-lep_vs_qcd_nLayer-3_CNN-1_BDT" \



#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixes \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "TMVAinfo/ttbar-had_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
#        "hepTop_CNN_reco" \
#        "TMVAinfo/ttbar-had_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
#    --comparisons \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        2 \
#        4 \
#        4 \
#    --lineStyles \
#        1 \
#        7 \
#        1 \
#        7 \
#    --labels \
#        "t^{had} (t#bar{t}) vs. QCD (CNN)" \
#        "t^{had} (t#bar{t}) vs. QCD (CNN+BDT)" \
#        "t^{had} (W'_{3 TeV}) vs. QCD (CNN)" \
#        "t^{had} (W'_{3 TeV}) vs. QCD (CNN+BDT)" \
#    --legendPos "UL" \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --omitAUC \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1_BDT" \



#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixes \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-2" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --comparisons \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        4 \
#    --lineStyles \
#        1 \
#        1 \
#    --labels \
#        "t^{had} (t#bar{t}) vs. QCD (CNN-1)" \
#        "t^{had} (t#bar{t}) vs. QCD (CNN-2)" \
#    --legendPos "UL" \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --omitAUC \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1-2" \



#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixes \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-2" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --comparisons \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        4 \
#    --lineStyles \
#        1 \
#        1 \
#    --labels \
#        "t^{lep} (t#bar{t}) vs. QCD (CNN-1)" \
#        "t^{lep} (t#bar{t}) vs. QCD (CNN-2)" \
#    --legendPos "UL" \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --omitAUC \
#    --outFileName "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1-2" \



#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixes \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "TMVAinfo/ttbar-lep_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
#        "hepTop_CNN_reco" \
#        "TMVAinfo/ttbar-lep_vs_qcd/weights/TMVAClassification_BDT.weights.xml" \
#    --comparisons \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        2 \
#        4 \
#        4 \
#    --lineStyles \
#        1 \
#        7 \
#        1 \
#        7 \
#    --labels \
#        "t^{lep} (t#bar{t}) vs. QCD (CNN)" \
#        "t^{lep} (t#bar{t}) vs. QCD (CNN+BDT)" \
#        "t^{lep} (W'_{3 TeV}) vs. QCD (CNN)" \
#        "t^{lep} (W'_{3 TeV}) vs. QCD (CNN+BDT)" \
#    --legendPos "UL" \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --omitAUC \
#    --outFileName "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1_BDT" \



python -u plotROC.py \
    --sigFiles \
        l_ntupleFile_ttbar \
        l_ntupleFile_ttbar \
        l_ntupleFile_Wprime_3TeV_lep \
        l_ntupleFile_Wprime_3TeV_lep \
    --bkgFiles \
        l_ntupleFile_ttbar \
        l_ntupleFile_ttbar \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_Wprime_3TeV_had \
    --extraDirSuffixes \
        "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
        "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
        "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
        "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
    --varsROC \
        "hepTop_CNN_reco" \
        "TMVAinfo/ttbar_lep-vs-had_with-miniIso/weights/TMVAClassification_BDT.weights.xml" \
        "hepTop_CNN_reco" \
        "TMVAinfo/ttbar_lep-vs-had_with-miniIso/weights/TMVAClassification_BDT.weights.xml" \
    --comparisons \
        ">" \
        ">" \
        ">" \
        ">" \
    --cutsSig \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --cutsBkg \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --nEventMaxs \
        -1 \
        -1 \
        -1 \
        -1 \
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
        "t^{lep} vs. t^{had} (t#bar{t}) (CNN)" \
        "t^{lep} vs. t^{had} (t#bar{t}) (CNN+BDT)" \
        "t^{lep} vs. t^{had} (W'_{3 TeV}) (CNN)" \
        "t^{lep} vs. t^{had} (W'_{3 TeV}) (CNN+BDT)" \
    --legendPos "UL" \
    --yMin 1e-5 \
    --yMax 1e2 \
    --logY \
    --xTitle "Signal efficiency" \
    --yTitle "Background efficiency" \
    --omitAUC \
    --outFileName "network_ttbar_lep-vs-had_nLayer-3_CNN-1_BDT" \



#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixes \
#        "network_ttbar-had_vs_qcd_nLayer-3-DetaDphi_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3-DetaDphi_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3-DetaDphi_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3-DetaDphi_CNN-1" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --comparisons \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        2 \
#        4 \
#        4 \
#    --lineStyles \
#        1 \
#        7 \
#        1 \
#        7 \
#    --labels \
#        "t^{had} (t#bar{t}) vs. QCD" \
#        "t^{had} (W'_{3 TeV}) vs. QCD" \
#        "t^{lep} (t#bar{t}) vs. QCD" \
#        "t^{lep} (W'_{3 TeV}) vs. QCD" \
#    --legendPos "UL" \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --omitAUC \
#    --outFileName "network_ttbar-had-lep_vs_qcd_nLayer-3-DetaDphi_CNN-1" \


#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#    --extraDirSuffixes \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --comparisons \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        4 \
#        4 \
#        4 \
#        6 \
#        8 \
#        8 \
#        8 \
#    --lineStyles \
#        1 \
#        1 \
#        7 \
#        3 \
#        1 \
#        1 \
#        7 \
#        3 \
#    --labels \
#        "t^{had} (t#bar{t}) vs. udsg (QCD) CNN" \
#        "t^{had} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
#        "t^{had}_{L} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
#        "t^{had}_{R} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
#        "t^{lep} (t#bar{t}) vs. udsg (QCD) CNN" \
#        "t^{lep} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
#        "t^{lep}_{L} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
#        "t^{lep}_{R} (W'_{3 TeV}) vs. udsg (QCD) CNN" \
#    --legendPos "UL" \
#    --legendTextSize 0.02 \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --outFileName "network_ttbar-had-lep-LR_vs_qcd_nLayer-3_CNN-1" \



#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_lep \
#    --bkgFiles \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_qcd \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_Wprime_3TeV_had \
#    --extraDirSuffixes \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_Wprime-3TeV-had_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_Wprime-3TeV-lep_vs_qcd_nLayer-3_CNN-1" \
#        "network_ttbar_lep-vs-had_nLayer-3_CNN-1" \
#        "network_Wprime-3TeV_lep-vs-had_nLayer-3_CNN-1" \
#    --varsROC \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --comparisons \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#        ">" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --cutsBkg \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#    --lineColors \
#        2 \
#        2 \
#        4 \
#        4 \
#        6 \
#        6 \
#    --lineStyles \
#        1 \
#        7 \
#        1 \
#        7 \
#        1 \
#        7 \
#    --labels \
#        "t^{had} (t#bar{t}) vs. QCD" \
#        "t^{had} (W'_{3 TeV}) vs. QCD" \
#        "t^{lep} (t#bar{t}) vs. QCD" \
#        "t^{lep} (W'_{3 TeV}) vs. QCD" \
#        "t^{lep} (t#bar{t}) vs. t^{had} (t#bar{t})" \
#        "t^{lep} (W'_{3 TeV}) vs. t^{had} (W'_{3 TeV})" \
#    --legendPos "UL" \
#    --yMin 1e-5 \
#    --yMax 1e2 \
#    --logY \
#    --xTitle "Signal efficiency" \
#    --yTitle "Background efficiency" \
#    --omitAUC \
#    --outFileName "network_top-had-lep_vs_qcd_nLayer-3_CNN-1" \



python -u plotROC.py \
    --sigFiles \
        l_ntupleFile_stop_L \
        l_ntupleFile_stop_L \
        l_ntupleFile_Wprime_3TeV_L_had \
        l_ntupleFile_Wprime_3TeV_L_had \
    --bkgFiles \
        l_ntupleFile_stop_R \
        l_ntupleFile_stop_R \
        l_ntupleFile_Wprime_3TeV_R_had \
        l_ntupleFile_Wprime_3TeV_R_had \
    --extraDirSuffixes \
        "" \
        "network_stop-had_LvsR_nLayer-3_CNN-1" \
        "" \
        "network_stop-had_LvsR_nLayer-3_CNN-1" \
    --varsROC \
        "hepTop_cosThetaStar_reco" \
        "hepTop_CNN_reco" \
        "hepTop_cosThetaStar_reco" \
        "hepTop_CNN_reco" \
    --comparisons \
        "<" \
        ">" \
        "<" \
        ">" \
    --cutsSig \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --cutsBkg \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --nEventMaxs \
        -1 \
        -1 \
        -1 \
        -1 \
    --lineColors \
        2 \
        2 \
        4 \
        4 \
    --lineStyles \
        7 \
        1 \
        7 \
        1 \
    --labels \
        "cos#theta* (#tilde{t}#bar{#tilde{t}})" \
        "t^{had}_{L} vs. t^{had}_{R} CNN (#tilde{t}#bar{#tilde{t}})" \
        "cos#theta* (W'_{3 TeV})" \
        "t^{had}_{L} vs. t^{had}_{R} CNN (W'_{3 TeV})" \
    --legendPos "UL" \
    --yMin 0 \
    --yMax 1 \
    --xTitle "t^{had}_{L} efficiency" \
    --yTitle "t^{had}_{R} efficiency" \
    --omitAUC \
    --outFileName "network_stop-had_LvsR_nLayer-3_CNN-1_eval-stop-Wprime-3TeV" \


#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_L_had \
#    --bkgFiles \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixes \
#        "" \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#    --varsROC \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_CNN_reco" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_nGenTopConstiMatched_reco == 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_nGenTopConstiMatched_reco == 3" \
#    --cutsBkg \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_nGenTopConstiMatched_reco == 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_nGenTopConstiMatched_reco == 3" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#    --lineColors \
#        4 \
#        4 \
#    --lineStyles \
#        7 \
#        1 \
#    --labels \
#        "cos#theta* (W'_{3 TeV}) (n_{prong}=3)" \
#        "t^{had}_{L} vs. t^{had}_{R} CNN (W'_{3 TeV}) (n_{prong}=3)" \
#    --legendPos "LL" \
#    --outFileName "top-had_LvsR_nProngMatched3" \
#
#
#python -u plotROC.py \
#    --sigFiles \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_L_had \
#    --bkgFiles \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixes \
#        "" \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#    --varsROC \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_CNN_reco" \
#    --cutsSig \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_isMayBeTop_reco" \
#    --cutsBkg \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_isMayBeTop_reco" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#    --lineColors \
#        4 \
#        4 \
#    --lineStyles \
#        7 \
#        1 \
#    --labels \
#        "cos#theta* (W'_{3 TeV}) (MBT jets)" \
#        "t^{had}_{L} vs. t^{had}_{R} CNN (W'_{3 TeV}) (MBT jets)" \
#    --legendPos "LL" \
#    --outFileName "top-had_LvsR_MBT" \


python -u plotROC.py \
    --sigFiles \
        l_ntupleFile_stop_L \
        l_ntupleFile_stop_L \
        l_ntupleFile_Wprime_3TeV_L_lep \
        l_ntupleFile_Wprime_3TeV_L_lep \
    --bkgFiles \
        l_ntupleFile_stop_R \
        l_ntupleFile_stop_R \
        l_ntupleFile_Wprime_3TeV_R_lep \
        l_ntupleFile_Wprime_3TeV_R_lep \
    --extraDirSuffixes \
        "" \
        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
        "" \
        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
    --nEventMaxs \
        -1 \
        -1 \
        -1 \
        -1 \
    --varsROC \
        "hepTop_zl_reco" \
        "hepTop_CNN_reco" \
        "hepTop_zl_reco" \
        "hepTop_CNN_reco" \
    --comparisons \
        "<" \
        ">" \
        "<" \
        ">" \
    --cutsSig \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --cutsBkg \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --lineColors \
        2 \
        2 \
        4 \
        4 \
    --lineStyles \
        7 \
        1 \
        7 \
        1 \
    --labels \
        "z_{l} (#tilde{t}#bar{#tilde{t}})" \
        "t^{lep}_{L} vs. t^{lep}_{R} CNN (#tilde{t}#bar{#tilde{t}})" \
        "z_{l} (W'_{3 TeV})" \
        "t^{lep}_{L} vs. t^{lep}_{R} CNN (W'_{3 TeV})" \
    --legendPos "LR" \
    --yMin 1e-3 \
    --yMax 1 \
    --logY \
    --xTitle "t^{lep}_{L} efficiency" \
    --yTitle "t^{lep}_{R} efficiency" \
    --omitAUC \
    --outFileName "network_stop-lep_LvsR_nLayer-3_CNN-1_eval-stop-Wprime-3TeV" \
