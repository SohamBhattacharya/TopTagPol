#python -u mxnet_getCorrelation.py \
#    --training stop-had_LvsR_nLayer-3 \
#    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --sigFiles l_ntupleFile_stop_L \
#    --bkgFiles l_ntupleFile_stop_R \
#    --corrVarName hepTop_cosThetaStar_reco \
#    --corrVarRange -1.0 1.0 \
#    --corrVarNbin 100 \
#    --corrVarLatex "cos#theta*" \
#    --nEventMax 200000 \
#    --splitEvery 10000 \
#    --printCorrPos -0.9 0.95 \
#    --titleSig "CNN classifier (t^{had}_{L} vs. t^{had}_{R}) vs. cos#theta* in #tilde{t}_{L}-pair events" \
#    --titleBkg "CNN classifier (t^{had}_{L} vs. t^{had}_{R}) vs. cos#theta* in #tilde{t}_{R}-pair events"
#
#
#python -u mxnet_getCorrelation.py \
#    --training stop-had_LvsR_nLayer-3 \
#    --trainingDirName network_stop-had_LvsR_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --sigFiles l_ntupleFile_stop_L \
#    --bkgFiles l_ntupleFile_stop_R \
#    --corrVarName hepTop_cosThetaStar_reco \
#    --corrVarRange -1.0 1.0 \
#    --corrVarNbin 100 \
#    --corrVarLatex "#font[62]{cos#theta*}" \
#    --nEventMax 200000 \
#    --splitEvery 10000 \
#    --extraCutSig "hepTop_isMayBeTop_reco" \
#    --extraCutBkg "hepTop_isMayBeTop_reco" \
#    --outFileSuffix "_with-isMayBeTop" \
#    --printCorrPos -0.9 0.95 \
#    --titleSig "CNN classifier (t^{had}_{L} vs. t^{had}_{R}) vs. cos#theta* in #tilde{t}_{L}-pair events" \
#    --titleBkg "CNN classifier (t^{had}_{L} vs. t^{had}_{R}) vs. cos#theta* in #tilde{t}_{R}-pair events"


python -u mxnet_getCorrelation.py \
    --training ttbar-had_vs_qcd_nLayer-3 \
    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
    --epoch 25 \
    --sigFiles l_ntupleFile_ttbar \
    --bkgFiles l_ntupleFile_qcd \
    --corrVarName hepTop_m_reco \
    --corrVarRange 0 600 \
    --corrVarNbin 300 \
    --corrVarLatex "m_{jet}" \
    --nEventMax 200000 \
    --splitEvery 10000 \
    --printCorrPos 50 0.65 \
    --logZ \
    --titleSig "CNN classifier (t^{had} vs. QCD) vs. m_{jet} in t#bar{t} events" \
    --titleBkg "CNN classifier (t^{had} vs. QCD) vs. m_{jet} in QCD events"


#python -u mxnet_getCorrelation.py \
#    --training ttbar-had_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --corrVarName hepTop_m_reco \
#    --corrVarRange 0 600 \
#    --corrVarNbin 300 \
#    --corrVarLatex "m_{jet}" \
#    --nEventMax 200000 \
#    --splitEvery 10000 \
#    --extraCutSig "hepTop_isMayBeTop_reco" \
#    --extraCutBkg "hepTop_isMayBeTop_reco" \
#    --outFileSuffix "_with-isMayBeTop" \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --titleSig "CNN classifier (t^{had} vs. QCD) vs. m_{jet} in t#bar{t} events" \
#    --titleBkg "CNN classifier (t^{had} vs. QCD) vs. m_{jet} in QCD events"


python -u mxnet_getCorrelation.py \
    --training ttbar-had_vs_qcd_nLayer-3 \
    --trainingDirName network_ttbar-had_vs_qcd_nLayer-3_CNN-1 \
    --epoch 25 \
    --sigFiles l_ntupleFile_ttbar \
    --bkgFiles l_ntupleFile_qcd \
    --corrVarName hepTop_m_reco \
    --corrVarRange 0 600 \
    --corrVarNbin 300 \
    --corrVarLatex "m_{jet}" \
    --nEventMax 200000 \
    --splitEvery 10000 \
    --extraCutSig "hepTop_m_reco > 100" \
    --extraCutBkg "hepTop_m_reco > 100" \
    --outFileSuffix "_m-gtr-100" \
    --printCorrPos 50 0.65 \
    --logZ \
    --titleSig "CNN classifier (t^{had} vs. QCD) vs. m_{jet} in t#bar{t} events" \
    --titleBkg "CNN classifier (t^{had} vs. QCD) vs. m_{jet} in QCD events"


#python -u mxnet_getCorrelation.py \
#    --training ttbar-lep_vs_qcd_nLayer-3 \
#    --trainingDirName network_ttbar-lep_vs_qcd_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_qcd \
#    --corrVarName hepTop_m_reco \
#    --corrVarRange 0 600 \
#    --corrVarNbin 300 \
#    --corrVarLatex "m_{jet}" \
#    --nEventMax 200000 \
#    --splitEvery 10000 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --titleSig "CNN classifier (t^{lep} vs. QCD) vs. m_{jet} in t#bar{t} events" \
#    --titleBkg "CNN classifier (t^{lep} vs. QCD) vs. m_{jet} in QCD events"
#
#
#python -u mxnet_getCorrelation.py \
#    --training ttbar_lep-vs-had_nLayer-3 \
#    --trainingDirName network_ttbar_lep-vs-had_nLayer-3_CNN-1 \
#    --epoch 25 \
#    --sigFiles l_ntupleFile_ttbar \
#    --bkgFiles l_ntupleFile_ttbar \
#    --corrVarName hepTop_m_reco \
#    --corrVarRange 0 600 \
#    --corrVarNbin 300 \
#    --corrVarLatex "m_{jet}" \
#    --nEventMax 200000 \
#    --splitEvery 10000 \
#    --printCorrPos 50 0.65 \
#    --logZ \
#    --titleSig "CNN classifier (t^{lep} vs. t^{had}) vs. m_{jet} for t^{had} jets in t#bar{t} events" \
#    --titleBkg "CNN classifier (t^{lep} vs. t^{had}) vs. m_{jet} for t^{lep} jets in t#bar{t} events"

