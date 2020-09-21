#python -u plotVariable2D.py \
#    --fileList \
#        "l_ntupleFile_ttbar" \
#    --extraDirSuffixList \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --plotX \
#        "hepTop_m_reco" \
#    --plotY \
#        "hepTop_CNN_reco" \
#    --cut \
#        "hepTop_genHadTop_deltaR_reco < 1 && hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco && hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "m_{jet} [GeV]" \
#    --yTitle "CNN [t^{had} (t#bar{t}) vs. udsg (QCD)]" \
#    --xMin 0 \
#    --xMax 500 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 1 \
#    --nBinY 100 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --title "t^{had} jet from t#bar{t}" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/CNN_vs_hepTop_m_reco_ttbar" \



#python -u plotVariable2D.py \
#    --fileList \
#        "l_ntupleFile_qcd" \
#    --extraDirSuffixList \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --plotX \
#        "hepTop_m_reco" \
#    --plotY \
#        "hepTop_CNN_reco" \
#    --cut \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3" \
#    --xTitle "m_{jet} [GeV]" \
#    --yTitle "CNN [t^{had} (t#bar{t}) vs. udsg (QCD)]" \
#    --xMin 0 \
#    --xMax 500 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 1 \
#    --nBinY 100 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --title "udsg jet from QCD" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/CNN_vs_hepTop_m_reco_qcd" \
#
#
#
#python -u plotVariable2D.py \
#    --fileList \
#        "l_ntupleFile_qcd" \
#    --extraDirSuffixList \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --plotX \
#        "hepTop_m_reco" \
#    --plotY \
#        "hepTop_CNN_reco" \
#    --cut \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_m_reco < 100" \
#    --xTitle "m_{jet} [GeV]" \
#    --yTitle "CNN [t^{had} (t#bar{t}) vs. udsg (QCD)]" \
#    --xMin 0 \
#    --xMax 500 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 1 \
#    --nBinY 100 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --title "udsg jet from QCD" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/CNN_vs_hepTop_m_reco_m-lt-100_qcd" \
#
#
#
#python -u plotVariable2D.py \
#    --fileList \
#        "l_ntupleFile_qcd" \
#    --extraDirSuffixList \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --plotX \
#        "hepTop_m_reco" \
#    --plotY \
#        "hepTop_CNN_reco" \
#    --cut \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_m_reco > 100" \
#    --xTitle "m_{jet} [GeV]" \
#    --yTitle "CNN [t^{had} (t#bar{t}) vs. udsg (QCD)]" \
#    --xMin 0 \
#    --xMax 500 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 1 \
#    --nBinY 100 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --title "udsg jet from QCD" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/CNN_vs_hepTop_m_reco_m-gt-100_qcd" \
#
#
#
#python -u plotVariable2D.py \
#    --fileList \
#        "l_ntupleFile_qcd" \
#    --extraDirSuffixList \
#        "network_ttbar-had_vs_qcd_nLayer-3_CNN-1" \
#    --plotX \
#        "hepTop_m_reco" \
#    --plotY \
#        "hepTop_CNN_reco" \
#    --cut \
#        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_m_reco > 150" \
#    --xTitle "m_{jet} [GeV]" \
#    --yTitle "CNN [t^{had} (t#bar{t}) vs. udsg (QCD)]" \
#    --xMin 0 \
#    --xMax 500 \
#    --nBinX 100 \
#    --yMin 0 \
#    --yMax 1 \
#    --nBinY 100 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --title "udsg jet from QCD" \
#    --outFileName "network_ttbar-had_vs_qcd_nLayer-3_CNN-1/CNN_vs_hepTop_m_reco_m-gt-150_qcd" \



python -u plotVariable2D.py \
    --fileList \
        "l_ntupleFile_qcd" \
    --extraDirSuffixList \
        "network_ttbar-had_vs_qcd_nLayer-3-DetaDphi_CNN-1" \
    --plotX \
        "hepTop_m_reco" \
    --plotY \
        "hepTop_CNN_reco" \
    --cut \
        "hepTop_pT_reco > 200 && hepTop_nExcSubJet_reco >= 3 && hepTop_m_reco < 100" \
    --xTitle "m_{jet} [GeV]" \
    --yTitle "CNN [t^{had} (t#bar{t}) vs. udsg (QCD)]" \
    --xMin 0 \
    --xMax 500 \
    --nBinX 100 \
    --yMin 0 \
    --yMax 1 \
    --nBinY 100 \
    --printCorrPos 50 0.65 \
    --logZ \
    --title "udsg jet from QCD" \
    --outFileName "network_ttbar-had_vs_qcd_nLayer-3-DetaDphi_CNN-1/CNN_vs_hepTop_m_reco_qcd" \
