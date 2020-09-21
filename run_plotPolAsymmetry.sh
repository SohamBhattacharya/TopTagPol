python -u plotPolAsymmetry.py \
    --inputFiles \
        l_ntupleFile_stop_L \
        l_ntupleFile_stop_R \
        l_ntupleFile_stop_L \
        l_ntupleFile_stop_R \
    --extraDirSuffixes \
        "" \
        "" \
        "network_stop-had_LvsR_nLayer-3_CNN-1" \
        "network_stop-had_LvsR_nLayer-3_CNN-1" \
    --nEventMaxs \
        -1 \
        -1 \
        -1 \
        -1 \
    --asymVars \
        "hepTop_cosThetaStar_reco" \
        "hepTop_cosThetaStar_reco" \
        "network_stop_had_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
        "network_stop_had_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
    --asymVarLimits \
        -1 +1 \
        -1 +1 \
        0 +1 \
        0 +1 \
    --asymVarNdivs \
        800 \
        800 \
        800 \
        800 \
    --comparisons \
        "<" \
        "<" \
        ">" \
        ">" \
    --cuts \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
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
        "A^{L}_{cos#theta*}" \
        "A^{R}_{cos#theta*}" \
        "A^{L}_{CNN}" \
        "A^{R}_{CNN}" \
    --diffs \
        0 1 \
        2 3 \
    --diffColors \
        2 \
        4 \
    --diffStyles \
        3 \
        3 \
    --diffLabels \
        "A^{L}_{cos#theta*}#minusA^{R}_{cos#theta*}" \
        "A^{L}_{CNN}#minusA^{R}_{CNN}" \
    --legendPos "UL" \
    --xMin -1 \
    --xMax +1 \
    --yMin -1 \
    --yMax +1 \
    --nDivX 4 2 5 \
    --nDivY 4 2 5 \
    --xTitle "t^{had}_{L} vs. t^{had}_{R} discriminator cut value" \
    --yTitle "Asymmetry" \
    --outDir "plots/asymmetry" \
    --outFileName "asymmetry_network_stop-had_LvsR_nLayer-3_CNN-1_eval-stop" \



#python -u plotPolAsymmetry.py \
#    --inputFiles \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixes \
#        "" \
#        "" \
#        "" \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#        -1 \
#    --asymVars \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "network_stop_had_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
#        "network_stop_had_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
#        "network_stop_had_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
#    --asymVarLimits \
#        -1 +1 \
#        -1 +1 \
#        -1 +1 \
#        0 +1 \
#        0 +1 \
#        0 +1 \
#    --asymVarNdivs \
#        500 \
#        500 \
#        500 \
#        800 \
#        800 \
#        800 \
#    --comparisons \
#        "<" \
#        "<" \
#        "<" \
#        ">" \
#        ">" \
#        ">" \
#    --cuts \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --lineColors \
#        2 \
#        2 \
#        2 \
#        4 \
#        4 \
#        4 \
#    --lineStyles \
#        7 \
#        1 \
#        3 \
#        7 \
#        1 \
#        3 \
#    --labels \
#        "A(cos#theta*, L) W'_{3 TeV}" \
#        "A(cos#theta*, L+R) W'_{3 TeV}" \
#        "A(cos#theta*, R) W'_{3 TeV}" \
#        "A(CNN, L) W'_{3 TeV}" \
#        "A(CNN, L+R) W'_{3 TeV}" \
#        "A(CNN, R) W'_{3 TeV}" \
#    --diffs \
#        0 1 \
#        2 1 \
#        3 4 \
#        5 4 \
#    --diffColors \
#        8 \
#        8 \
#        6 \
#        6 \
#    --diffStyles \
#        7 \
#        3 \
#        7 \
#        3 \
#    --diffLabels \
#        "A(cos#theta*, L) #minus A(cos#theta*, L+R) W'_{3 TeV}" \
#        "A(cos#theta*, R) #minus A(cos#theta*, L+R) W'_{3 TeV}" \
#        "A(CNN, L) #minus A(CNN, L+R) W'_{3 TeV}" \
#        "A(CNN, R) #minus A(CNN, L+R) W'_{3 TeV}" \
#    --legendPos "LL" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --nDivX 4 2 5 \
#    --nDivY 4 2 5 \
#    --xTitle "t^{had}_{L} vs. t^{had}_{R} discriminator cut value" \
#    --yTitle "Asymmetry" \
#    --outDir "plots/asymmetry" \
#    --outFileName "asymmetry_network_stop-had_LvsR_nLayer-3_CNN-1_eval-Wprime-3TeV" \



python -u plotPolAsymmetry.py \
    --inputFiles \
        l_ntupleFile_stop_L \
        l_ntupleFile_stop_R \
        l_ntupleFile_stop_L \
        l_ntupleFile_stop_R \
    --extraDirSuffixes \
        "" \
        "" \
        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
    --nEventMaxs \
        -1 \
        -1 \
        -1 \
        -1 \
    --asymVars \
        "hepTop_zl_reco" \
        "hepTop_zl_reco" \
        "network_stop_lep_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
        "network_stop_lep_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
    --asymVarLimits \
        0 +1 \
        0 +1 \
        0 +1 \
        0 +1 \
    --asymVarNdivs \
        800 \
        800 \
        800 \
        800 \
    --comparisons \
        "<" \
        "<" \
        ">" \
        ">" \
    --cuts \
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
        1 \
        7 \
        1 \
        7 \
    --labels \
        "A^{L}_{z#lower[0.7]{l}}" \
        "A^{R}_{z#lower[0.7]{l}}" \
        "A^{L}_{CNN}" \
        "A^{R}_{CNN}" \
    --diffs \
        0 1 \
        2 3 \
    --diffColors \
        2 \
        4 \
    --diffStyles \
        3 \
        3 \
    --diffLabels \
        "A^{L}_{z#lower[0.7]{l}}#minusA^{R}_{z#lower[0.7]{l}}" \
        "A^{L}_{CNN}#minusA^{R}_{CNN}" \
    --legendPos "UL" \
    --xMin -0.5 \
    --xMax +1 \
    --yMin -1 \
    --yMax +1 \
    --nDivX 6 2 5 \
    --nDivY 4 2 5 \
    --xTitle "t^{lep}_{L} vs. t^{lep}_{R} discriminator cut value" \
    --yTitle "Asymmetry" \
    --outDir "plots/asymmetry" \
    --outFileName "asymmetry_network_stop-lep_LvsR_nLayer-3_CNN-1_eval-stop" \



#python -u plotPolAsymmetry.py \
#    --inputFiles \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#    --extraDirSuffixes \
#        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
#        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
#        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
#    --nEventMaxs \
#        -1 \
#        -1 \
#        -1 \
#    --asymVars \
#        "network_stop_lep_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
#        "network_stop_lep_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
#        "network_stop_lep_LvsR_nLayer_3_CNN_1.hepTop_CNN_reco" \
#    --asymVarLimits \
#        0 +1 \
#        0 +1 \
#        0 +1 \
#    --asymVarNdivs \
#        500 \
#        500 \
#        500 \
#    --comparisons \
#        ">" \
#        ">" \
#        ">" \
#    --cuts \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --lineColors \
#        2 \
#        2 \
#        2 \
#    --lineStyles \
#        7 \
#        1 \
#        3 \
#    --labels \
#        "A(CNN, L) W'_{3 TeV}" \
#        "A(CNN, L+R) W'_{3 TeV}" \
#        "A(CNN, R) W'_{3 TeV}" \
#    --diffs \
#        0 1 \
#        2 1 \
#    --diffColors \
#        8 \
#        8 \
#    --diffStyles \
#        7 \
#        3 \
#    --diffLabels \
#        "A(CNN, L) #minus A(CNN, L+R) W'_{3 TeV}" \
#        "A(CNN, R) #minus A(CNN, L+R) W'_{3 TeV}" \
#    --legendPos "LL" \
#    --xMin -1 \
#    --xMax +1 \
#    --yMin -1 \
#    --yMax +1 \
#    --nDivX 4 2 5 \
#    --nDivY 4 2 5 \
#    --xTitle "t^{lep}_{L} vs. t^{lep}_{R} discriminator cut value" \
#    --yTitle "Asymmetry" \
#    --outDir "plots/asymmetry" \
#    --outFileName "asymmetry_network_stop-lep_LvsR_nLayer-3_CNN-1_eval-Wprime-3TeV" \
