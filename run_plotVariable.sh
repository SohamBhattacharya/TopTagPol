# ##### hepTop_pT (had)
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_1TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_qcd \
#    --plotList \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had} jets from t#bar{t}" \
#        "t^{had} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had} jets from W'(1 TeV)" \
#        "t^{had} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --lineColorList \
#        1 \
#        2 \
#        3 \
#        4 \
#        6 \
#    --xTitle "Raw p^{jet}_{T} [GeV]" \
#    --yTitle "a.u." \
#    --xMin 200 \
#    --xMax 1800 \
#    --nBinX 320 \
#    --yMin 0 \
#    --yMax 4e-2 \
#    --axisMaxDigits 4 \
#    --divX 4 2 5 \
#    --legendPos "UL" \
#    --outFileName "hepTop_raw_pT_reco_had"
#
#
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_1TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_qcd \
#    --plotList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had} jets from t#bar{t}" \
#        "t^{had} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had} jets from W'(1 TeV)" \
#        "t^{had} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --lineColorList \
#        1 \
#        2 \
#        3 \
#        4 \
#        6 \
#    --xTitle "p^{jet}_{T} [GeV]" \
#    --yTitle "a.u." \
#    --xMin 200 \
#    --xMax 1800 \
#    --nBinX 320 \
#    --yMin 0 \
#    --yMax 4e-2 \
#    --axisMaxDigits 4 \
#    --divX 4 2 5 \
#    --legendPos "UL" \
#    --outFileName "hepTop_pT_reco_had"
#
#
# ##### hepTop_pT (lep)
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_1TeV_lep \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_qcd \
#    --plotList \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#        "hepTop_raw_pT_reco" \
#    --cutList \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{lep} jets from t#bar{t}" \
#        "t^{lep} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{lep} jets from W'(1 TeV)" \
#        "t^{lep} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --lineColorList \
#        1 \
#        2 \
#        3 \
#        4 \
#        6 \
#    --xTitle "Raw p^{jet}_{T} [GeV]" \
#    --yTitle "a.u." \
#    --xMin 200 \
#    --xMax 1800 \
#    --nBinX 320 \
#    --yMin 0 \
#    --yMax 4e-2 \
#    --axisMaxDigits 4 \
#    --divX 4 2 5 \
#    --legendPos "UL" \
#    --outFileName "hepTop_raw_pT_reco_lep"
#
#
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_1TeV_lep \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_qcd \
#    --plotList \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#        "hepTop_pT_reco" \
#    --cutList \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{lep} jets from t#bar{t}" \
#        "t^{lep} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{lep} jets from W'(1 TeV)" \
#        "t^{lep} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --lineColorList \
#        1 \
#        2 \
#        3 \
#        4 \
#        6 \
#    --xTitle "p^{jet}_{T} [GeV]" \
#    --yTitle "a.u." \
#    --xMin 200 \
#    --xMax 1800 \
#    --nBinX 320 \
#    --yMin 0 \
#    --yMax 4e-2 \
#    --axisMaxDigits 4 \
#    --divX 4 2 5 \
#    --legendPos "UL" \
#    --outFileName "hepTop_pT_reco_lep"


 ##### hepTop_m (had)
python -u plotVariable.py \
    --fileList \
        l_ntupleFile_ttbar \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_1TeV_had \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_qcd \
    --plotList \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
    --cutList \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --labelList \
        "t^{had} jets from t#bar{t}" \
        "t^{had} jets from #tilde{t}#bar{#tilde{t}}" \
        "t^{had} jets from W'(1 TeV)" \
        "t^{had} jets from W'(3 TeV)" \
        "udsg jets from QCD" \
    --lineColorList \
        1 \
        2 \
        3 \
        4 \
        6 \
    --xTitle "Raw m_{jet} [GeV]" \
    --yTitle "a.u." \
    --xMin 0 \
    --xMax 500 \
    --nBinX 100 \
    --yMin 0 \
    --yMax 0.1 \
    --divX 5 2 5 \
    --legendPos "UL" \
    --outFileName "hepTop_raw_m_reco_had"


python -u plotVariable.py \
    --fileList \
        l_ntupleFile_ttbar \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_1TeV_had \
        l_ntupleFile_Wprime_3TeV_had \
        l_ntupleFile_qcd \
    --plotList \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
    --cutList \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --labelList \
        "t^{had} jets from t#bar{t}" \
        "t^{had} jets from #tilde{t}#bar{#tilde{t}}" \
        "t^{had} jets from W'(1 TeV)" \
        "t^{had} jets from W'(3 TeV)" \
        "udsg jets from QCD" \
    --lineColorList \
        1 \
        2 \
        3 \
        4 \
        6 \
    --xTitle "m_{jet} [GeV]" \
    --yTitle "a.u." \
    --xMin 0 \
    --xMax 500 \
    --nBinX 100 \
    --yMin 0 \
    --yMax 0.1 \
    --divX 5 2 5 \
    --legendPos "UL" \
    --outFileName "hepTop_m_reco_had"


 ##### hepTop_m (lep)
python -u plotVariable.py \
    --fileList \
        l_ntupleFile_ttbar \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_1TeV_lep \
        l_ntupleFile_Wprime_3TeV_lep \
        l_ntupleFile_qcd \
    --plotList \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
        "hepTop_raw_m_reco" \
    --cutList \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_raw_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --labelList \
        "t^{lep} jets from t#bar{t}" \
        "t^{lep} jets from #tilde{t}#bar{#tilde{t}}" \
        "t^{lep} jets from W'(1 TeV)" \
        "t^{lep} jets from W'(3 TeV)" \
        "udsg jets from QCD" \
    --lineColorList \
        1 \
        2 \
        3 \
        4 \
        6 \
    --xTitle "Raw m_{jet} [GeV]" \
    --yTitle "a.u." \
    --xMin 0 \
    --xMax 500 \
    --nBinX 100 \
    --yMin 0 \
    --yMax 0.1 \
    --divX 5 2 5 \
    --legendPos "UL" \
    --outFileName "hepTop_raw_m_reco_lep"


python -u plotVariable.py \
    --fileList \
        l_ntupleFile_ttbar \
        l_ntupleFile_stop \
        l_ntupleFile_Wprime_1TeV_lep \
        l_ntupleFile_Wprime_3TeV_lep \
        l_ntupleFile_qcd \
    --plotList \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
        "hepTop_m_reco" \
    --cutList \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
    --labelList \
        "t^{lep} jets from t#bar{t}" \
        "t^{lep} jets from #tilde{t}#bar{#tilde{t}}" \
        "t^{lep} jets from W'(1 TeV)" \
        "t^{lep} jets from W'(3 TeV)" \
        "udsg jets from QCD" \
    --lineColorList \
        1 \
        2 \
        3 \
        4 \
        6 \
    --xTitle "m_{jet} [GeV]" \
    --yTitle "a.u." \
    --xMin 0 \
    --xMax 500 \
    --nBinX 100 \
    --yMin 0 \
    --yMax 0.1 \
    --divX 5 2 5 \
    --legendPos "UL" \
    --outFileName "hepTop_m_reco_lep"


# ##### hepTop_subJet123_m 
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_1TeV_had \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_qcd \
#    --plotList \
#        "hepTop_subJet123_m_reco" \
#        "hepTop_subJet123_m_reco" \
#        "hepTop_subJet123_m_reco" \
#        "hepTop_subJet123_m_reco" \
#        "hepTop_subJet123_m_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#    --labelList \
#        "t^{had} jets from t#bar{t}" \
#        "t^{had} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had} jets from W'(1 TeV)" \
#        "t^{had} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --xTitle "m_{123} [GeV]" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 500 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 0.1 \
#    --divX 5 2 5 \
#    --legendPos "UL" \
#    --outFileName "hepTop_subJet123_m_had_with-isMayBeTop"


# ##### cosThetaStar_truth #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_ttbar \
#    --plotList \
#        "cosThetaStar_truth" \
#        "cosThetaStar_truth" \
#        "cosThetaStar_truth" \
#        "cosThetaStar_truth" \
#        "cosThetaStar_truth" \
#    --cutList \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#        "hadTop_pT_truth > 200" \
#    --labelList \
#        "t^{had}_{L,gen} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{R,gen} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{L,gen} jets from W'(3 TeV)" \
#        "t^{had}_{R,gen} jets from W'(3 TeV)" \
#        "t^{had}_{gen} jets from t#bar{t}" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#        1 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#        1 \
#    --xTitle "cos#theta*" \
#    --yTitle "a.u." \
#    --xMin -1 \
#    --xMax +1 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 2.5e-2 \
#    --legendPos "UL" \
#    --title " " \
#    --outFileName "cosThetaStar_LvsR_truth"


# ##### hepTop_cosThetaStar_reco #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_ttbar \
#    --plotList \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had}_{L} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{R} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{L} jets from W'(3 TeV)" \
#        "t^{had}_{R} jets from W'(3 TeV)" \
#        "t^{had} jets from t#bar{t}" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#        1 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#        1 \
#    --xTitle "cos#theta*" \
#    --yTitle "a.u." \
#    --xMin -1 \
#    --xMax +1 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 2.5e-2 \
#    --legendPos "UL" \
#    --title " " \
#    --outFileName "cosThetaStar_LvsR"


#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#        l_ntupleFile_ttbar \
#    --plotList \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#        "hepTop_cosThetaStar_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#    --labelList \
#        "t^{had}_{L} MBT-jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{R} MBT-jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{L} MBT-jets from W'(3 TeV)" \
#        "t^{had}_{R} MBT-jets from W'(3 TeV)" \
#        "t^{had} MBT-jets from t#bar{t}" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#        1 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#        1 \
#    --xTitle "cos#theta*" \
#    --yTitle "a.u." \
#    --xMin -1 \
#    --xMax +1 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 2.5e-2 \
#    --legendPos "UL" \
#    --outFileName "cosThetaStar_LvsR_with-isMayBeTop"


# ##### network_stop-had_LvsR_nLayer-3_CNN-1 #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixList \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#    --plotList \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had}_{L} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{R} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{L} jets from W'(3 TeV)" \
#        "t^{had}_{R} jets from W'(3 TeV)" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#    --xTitle "t^{had}_{L} vs. t^{had}_{R} CNN classifier" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 0.1 \
#    --legendPos "UL" \
#    --title "Trained on #tilde{t}#bar{#tilde{t}} events" \
#    --detailStr "" \
#    --detailPos 0 0 \
#    --outFileName "stop-had_LvsR_nLayer-3_CNN-1"


#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_had \
#        l_ntupleFile_Wprime_3TeV_R_had \
#    --extraDirSuffixList \
#        "network_stop-had_LvsR_nLayer-3_CNN-1" \
#    --plotList \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_isMayBeTop_reco" \
#    --labelList \
#        "t^{had}_{L} MBT-jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{R} MBT-jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{L} MBT-jets from W'(3 TeV)" \
#        "t^{had}_{R} MBT-jets from W'(3 TeV)" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#    --xTitle "t^{had}_{L} vs. t^{had}_{R} CNN classifier" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 200 \
#    --yMin 0 \
#    --yMax 4e-2 \
#    --legendPos "UL" \
#    --title "Trained on #tilde{t}#bar{#tilde{t}} events" \
#    --detailStr "" \
#    --detailPos 0 0 \
#    --outFileName "stop-had_LvsR_nLayer-3_CNN-1_with-isMayBeTop"


# ##### hepTop_zl_reco #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#    --plotList \
#        "hepTop_zl_reco" \
#        "hepTop_zl_reco" \
#        "hepTop_zl_reco" \
#        "hepTop_zl_reco" \
#    --cutList \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had}_{L} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{R} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had}_{L} jets from W'(3 TeV)" \
#        "t^{had}_{R} jets from W'(3 TeV)" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#    --xTitle "z_{l}" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 0.05 \
#    --legendPos "UR" \
#    --title " " \
#    --outFileName "zl_LvsR"


# ##### network_stop-lep_LvsR_nLayer-3_CNN-1 #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#    --extraDirSuffixList \
#        "network_stop-lep_LvsR_nLayer-3_CNN-1" \
#    --plotList \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --cutList \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{lep}_{L} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{lep}_{R} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{lep}_{L} jets from W'(3 TeV)" \
#        "t^{lep}_{R} jets from W'(3 TeV)" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#    --xTitle "t^{lep}_{L} vs. t^{lep}_{R} CNN classifier" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 0.1 \
#    --legendPos "UL" \
#    --title "Trained on #tilde{t}#bar{#tilde{t}} events" \
#    --detailStr "" \
#    --detailPos 0 0 \
#    --outFileName "stop-lep_LvsR_nLayer-3_CNN-1"


# ##### network_Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1 #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_Wprime_3TeV_L_lep \
#        l_ntupleFile_Wprime_3TeV_R_lep \
#        l_ntupleFile_stop_L \
#        l_ntupleFile_stop_R \
#    --extraDirSuffixList \
#        "network_Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1" \
#    --plotList \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --cutList \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200" \
#    --labelList \
#        "t^{lep}_{L} jets from W'(3 TeV)" \
#        "t^{lep}_{R} jets from W'(3 TeV)" \
#        "t^{lep}_{L} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{lep}_{R} jets from #tilde{t}#bar{#tilde{t}}" \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#    --xTitle "t^{lep}_{L} vs. t^{lep}_{R} CNN classifier" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 200 \
#    --yMin 0 \
#    --yMax 4e-2 \
#    --legendPos "UL" \
#    --title "Trained on W'(3TeV) events" \
#    --detailStr "" \
#    --detailPos 0 0 \
#    --outFileName "Wprime-3TeV-lep_LvsR_nLayer-3_CNN-1"


# ##### network_ttbar-had_vs_qcd_nLayer-3_CNN-1 #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_3TeV_had \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --plotList \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --cutList \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{had} jets from t#bar{t}" \
#        "t^{had} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{had} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        8 \
#        6 \
#        4 \
#    --xTitle "t^{had} vs. udsg CNN classifier" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 100 \
#    --yMin 1e-4 \
#    --yMax 1 \
#    --logY \
#    --legendPos "UL" \
#    --title "Trained on t#bar{t} and QCD events" \
#    --detailStr "" \
#    --detailPos 0 0 \
#    --outFileName "ttbar-had_vs_qcd_nLayer-3_CNN-1"
#
#
# ##### network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 #####
#python -u plotVariable.py \
#    --fileList \
#        l_ntupleFile_ttbar \
#        l_ntupleFile_stop \
#        l_ntupleFile_Wprime_3TeV_lep \
#        l_ntupleFile_qcd \
#    --extraDirSuffixList \
#        "network_ttbar-lep_vs_qcd_nLayer-3_CNN-1" \
#    --plotList \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#        "hepTop_CNN_reco" \
#    --cutList \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_genLepTop_deltaR_reco < 1 && hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --labelList \
#        "t^{lep} jets from t#bar{t}" \
#        "t^{lep} jets from #tilde{t}#bar{#tilde{t}}" \
#        "t^{lep} jets from W'(3 TeV)" \
#        "udsg jets from QCD" \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#        7 \
#    --lineColorList \
#        2 \
#        8 \
#        6 \
#        4 \
#    --xTitle "t^{lep} vs. udsg CNN classifier" \
#    --yTitle "a.u." \
#    --xMin 0 \
#    --xMax 1 \
#    --nBinX 100 \
#    --yMin 1e-4 \
#    --yMax 1 \
#    --logY \
#    --legendPos "UL" \
#    --title "Trained on t#bar{t} and QCD events" \
#    --detailStr "" \
#    --detailPos 0 0 \
#    --outFileName "ttbar-lep_vs_qcd_nLayer-3_CNN-1"
