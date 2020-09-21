import Common
import mxnet_networks


l_varName_common = [
    "hadTop_pT_truth",
    "lepTopVis_pT_truth",
    
    "hepTop_pT_reco",
    "hepTop_genHadTop_deltaR_reco",
    "hepTop_genLepTop_deltaR_reco",
    "hepTop_isMayBeTop_reco",
    "hepTop_nearestGenHadTop_index",
    "hepTop_nearestGenLepTop_index",
    "hepTop_nExcSubJet_reco"
]


l_layerName_nLayer3 = [
    "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco",
    "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco",
    "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco",
]

l_layerName_nLayer3_DetaDphi = [
    "h2_hepTop_track_fracE_phiEtaPlane_reco",
    "h2_hepTop_photon_fracE_phiEtaPlane_reco",
    "h2_hepTop_neutralHad_fracE_phiEtaPlane_reco",
]


d_ntupleFile = {}


 ########## stop-L ##########
l_ntupleFile_stop_L = [
    "outputTree/stop-L/outputTree_stop-L_001.root",
    "outputTree/stop-L/outputTree_stop-L_002.root",
    "outputTree/stop-L/outputTree_stop-L_003.root",
    "outputTree/stop-L/outputTree_stop-L_004.root",
    "outputTree/stop-L/outputTree_stop-L_005.root",
    "outputTree/stop-L/outputTree_stop-L_006.root",
    "outputTree/stop-L/outputTree_stop-L_007.root",
    "outputTree/stop-L/outputTree_stop-L_008.root",
    "outputTree/stop-L/outputTree_stop-L_009.root",
    "outputTree/stop-L/outputTree_stop-L_010.root",
    "outputTree/stop-L/outputTree_stop-L_011.root",
    "outputTree/stop-L/outputTree_stop-L_012.root",
    "outputTree/stop-L/outputTree_stop-L_013.root",
    "outputTree/stop-L/outputTree_stop-L_014.root",
    "outputTree/stop-L/outputTree_stop-L_015.root",
    "outputTree/stop-L/outputTree_stop-L_016.root",
    "outputTree/stop-L/outputTree_stop-L_017.root",
    "outputTree/stop-L/outputTree_stop-L_018.root",
    "outputTree/stop-L/outputTree_stop-L_019.root",
    "outputTree/stop-L/outputTree_stop-L_020.root",
    "outputTree/stop-L/outputTree_stop-L_021.root",
    "outputTree/stop-L/outputTree_stop-L_022.root",
    "outputTree/stop-L/outputTree_stop-L_023.root",
    "outputTree/stop-L/outputTree_stop-L_024.root",
    "outputTree/stop-L/outputTree_stop-L_025.root",
    "outputTree/stop-L/outputTree_stop-L_026.root",
    "outputTree/stop-L/outputTree_stop-L_027.root",
    "outputTree/stop-L/outputTree_stop-L_028.root",
    "outputTree/stop-L/outputTree_stop-L_029.root",
    "outputTree/stop-L/outputTree_stop-L_030.root",
    "outputTree/stop-L/outputTree_stop-L_031.root",
    "outputTree/stop-L/outputTree_stop-L_032.root",
]

d_ntupleFile["l_ntupleFile_stop_L"] = l_ntupleFile_stop_L


 ########## stop-R ##########
l_ntupleFile_stop_R = [
    "outputTree/stop-R/outputTree_stop-R_001.root",
    "outputTree/stop-R/outputTree_stop-R_002.root",
    "outputTree/stop-R/outputTree_stop-R_003.root",
    "outputTree/stop-R/outputTree_stop-R_004.root",
    "outputTree/stop-R/outputTree_stop-R_005.root",
    "outputTree/stop-R/outputTree_stop-R_006.root",
    "outputTree/stop-R/outputTree_stop-R_007.root",
    "outputTree/stop-R/outputTree_stop-R_008.root",
    "outputTree/stop-R/outputTree_stop-R_009.root",
    "outputTree/stop-R/outputTree_stop-R_010.root",
    "outputTree/stop-R/outputTree_stop-R_011.root",
    "outputTree/stop-R/outputTree_stop-R_012.root",
    "outputTree/stop-R/outputTree_stop-R_013.root",
    "outputTree/stop-R/outputTree_stop-R_014.root",
    "outputTree/stop-R/outputTree_stop-R_015.root",
    "outputTree/stop-R/outputTree_stop-R_016.root",
    "outputTree/stop-R/outputTree_stop-R_017.root",
    "outputTree/stop-R/outputTree_stop-R_018.root",
    "outputTree/stop-R/outputTree_stop-R_019.root",
    "outputTree/stop-R/outputTree_stop-R_020.root",
    "outputTree/stop-R/outputTree_stop-R_021.root",
    "outputTree/stop-R/outputTree_stop-R_022.root",
    "outputTree/stop-R/outputTree_stop-R_023.root",
    "outputTree/stop-R/outputTree_stop-R_024.root",
    "outputTree/stop-R/outputTree_stop-R_025.root",
    "outputTree/stop-R/outputTree_stop-R_026.root",
    "outputTree/stop-R/outputTree_stop-R_027.root",
    "outputTree/stop-R/outputTree_stop-R_028.root",
    "outputTree/stop-R/outputTree_stop-R_029.root",
    "outputTree/stop-R/outputTree_stop-R_030.root",
    "outputTree/stop-R/outputTree_stop-R_031.root",
    "outputTree/stop-R/outputTree_stop-R_032.root",
]

d_ntupleFile["l_ntupleFile_stop_R"] = l_ntupleFile_stop_R


# Alternating stop L and R files
l_ntupleFile_stop = Common.mergeListsAlternating(
    l_ntupleFile_stop_L,
    l_ntupleFile_stop_R
)

d_ntupleFile["l_ntupleFile_stop"] = l_ntupleFile_stop


 ########## Wprime-1TeV ##########
l_ntupleFile_Wprime_1TeV_L_lep = [
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_001.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_002.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_003.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_004.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_005.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_006.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_007.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_008.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_009.root",
    "outputTree/Wprime-1TeV-L-lep/outputTree_Wprime-1TeV-L-lep_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_1TeV_L_lep"] = l_ntupleFile_Wprime_1TeV_L_lep


l_ntupleFile_Wprime_1TeV_L_had = [
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_001.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_002.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_003.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_004.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_005.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_006.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_007.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_008.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_009.root",
    "outputTree/Wprime-1TeV-L-had/outputTree_Wprime-1TeV-L-had_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_1TeV_L_had"] = l_ntupleFile_Wprime_1TeV_L_had


l_ntupleFile_Wprime_1TeV_R_lep = [
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_001.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_002.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_003.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_004.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_005.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_006.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_007.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_008.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_009.root",
    "outputTree/Wprime-1TeV-R-lep/outputTree_Wprime-1TeV-R-lep_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_1TeV_R_lep"] = l_ntupleFile_Wprime_1TeV_R_lep


l_ntupleFile_Wprime_1TeV_R_had = [
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_001.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_002.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_003.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_004.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_005.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_006.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_007.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_008.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_009.root",
    "outputTree/Wprime-1TeV-R-had/outputTree_Wprime-1TeV-R-had_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_1TeV_R_had"] = l_ntupleFile_Wprime_1TeV_R_had


# Alternating Wprime-1TeV-lep L and R files
l_ntupleFile_Wprime_1TeV_lep = Common.mergeListsAlternating(
    l_ntupleFile_Wprime_1TeV_L_lep,
    l_ntupleFile_Wprime_1TeV_R_lep
)

d_ntupleFile["l_ntupleFile_Wprime_1TeV_lep"] = l_ntupleFile_Wprime_1TeV_lep


# Alternating Wprime-1TeV-had L and R files
l_ntupleFile_Wprime_1TeV_had = Common.mergeListsAlternating(
    l_ntupleFile_Wprime_1TeV_L_had,
    l_ntupleFile_Wprime_1TeV_R_had
)

d_ntupleFile["l_ntupleFile_Wprime_1TeV_had"] = l_ntupleFile_Wprime_1TeV_had


# Alternating Wprime-1TeV lep and had files
l_ntupleFile_Wprime_1TeV = Common.mergeListsAlternating(
    l_ntupleFile_Wprime_1TeV_lep,
    l_ntupleFile_Wprime_1TeV_had
)

d_ntupleFile["l_ntupleFile_Wprime_1TeV"] = l_ntupleFile_Wprime_1TeV


 ########## Wprime-3TeV ##########
l_ntupleFile_Wprime_3TeV_L_lep = [
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_001.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_002.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_003.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_004.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_005.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_006.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_007.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_008.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_009.root",
    "outputTree/Wprime-3TeV-L-lep/outputTree_Wprime-3TeV-L-lep_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_3TeV_L_lep"] = l_ntupleFile_Wprime_3TeV_L_lep


l_ntupleFile_Wprime_3TeV_L_had = [
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_001.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_002.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_003.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_004.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_005.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_006.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_007.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_008.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_009.root",
    "outputTree/Wprime-3TeV-L-had/outputTree_Wprime-3TeV-L-had_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_3TeV_L_had"] = l_ntupleFile_Wprime_3TeV_L_had


l_ntupleFile_Wprime_3TeV_R_lep = [
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_001.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_002.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_003.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_004.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_005.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_006.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_007.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_008.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_009.root",
    "outputTree/Wprime-3TeV-R-lep/outputTree_Wprime-3TeV-R-lep_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_3TeV_R_lep"] = l_ntupleFile_Wprime_3TeV_R_lep


l_ntupleFile_Wprime_3TeV_R_had = [
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_001.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_002.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_003.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_004.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_005.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_006.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_007.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_008.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_009.root",
    "outputTree/Wprime-3TeV-R-had/outputTree_Wprime-3TeV-R-had_010.root",
]

d_ntupleFile["l_ntupleFile_Wprime_3TeV_R_had"] = l_ntupleFile_Wprime_3TeV_R_had


# Alternating Wprime-3TeV-lep L and R files
l_ntupleFile_Wprime_3TeV_lep = Common.mergeListsAlternating(
    l_ntupleFile_Wprime_3TeV_L_lep,
    l_ntupleFile_Wprime_3TeV_R_lep
)

d_ntupleFile["l_ntupleFile_Wprime_3TeV_lep"] = l_ntupleFile_Wprime_3TeV_lep


# Alternating Wprime-3TeV-had L and R files
l_ntupleFile_Wprime_3TeV_had = Common.mergeListsAlternating(
    l_ntupleFile_Wprime_3TeV_L_had,
    l_ntupleFile_Wprime_3TeV_R_had
)

d_ntupleFile["l_ntupleFile_Wprime_3TeV_had"] = l_ntupleFile_Wprime_3TeV_had


# Alternating Wprime-3TeV lep and had files
l_ntupleFile_Wprime_3TeV = Common.mergeListsAlternating(
    l_ntupleFile_Wprime_3TeV_lep,
    l_ntupleFile_Wprime_3TeV_had
)

d_ntupleFile["l_ntupleFile_Wprime_3TeV"] = l_ntupleFile_Wprime_3TeV


 ########## ttbar ##########
l_ntupleFile_ttbar_tj = [
    "outputTree/ttbar-tj/outputTree_ttbar-tj_001.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_002.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_003.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_004.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_005.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_006.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_007.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_008.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_009.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_010.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_011.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_012.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_013.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_014.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_015.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_016.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_017.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_018.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_019.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_020.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_021.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_022.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_023.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_024.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_025.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_026.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_027.root",
    "outputTree/ttbar-tj/outputTree_ttbar-tj_028.root",
]

d_ntupleFile["l_ntupleFile_ttbar_tj"] = l_ntupleFile_ttbar_tj


l_ntupleFile_ttbar_tbarj = [
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_001.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_002.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_003.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_004.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_005.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_006.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_007.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_008.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_009.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_010.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_011.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_012.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_013.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_014.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_015.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_016.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_017.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_018.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_019.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_020.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_021.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_022.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_023.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_024.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_025.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_026.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_027.root",
    "outputTree/ttbar-tbarj/outputTree_ttbar-tbarj_028.root",
]

d_ntupleFile["l_ntupleFile_ttbar_tbarj"] = l_ntupleFile_ttbar_tbarj


# Alternating tj and tbarj files
l_ntupleFile_ttbar = Common.mergeListsAlternating(
    l_ntupleFile_ttbar_tj,
    l_ntupleFile_ttbar_tbarj
)

d_ntupleFile["l_ntupleFile_ttbar"] = l_ntupleFile_ttbar


 ########## QCD ##########
l_ntupleFile_qcd = [
    "outputTree/qcd/outputTree_qcd_001.root",
    "outputTree/qcd/outputTree_qcd_002.root",
    "outputTree/qcd/outputTree_qcd_003.root",
    "outputTree/qcd/outputTree_qcd_004.root",
    "outputTree/qcd/outputTree_qcd_005.root",
    "outputTree/qcd/outputTree_qcd_006.root",
    "outputTree/qcd/outputTree_qcd_007.root",
    "outputTree/qcd/outputTree_qcd_008.root",
]

d_ntupleFile["l_ntupleFile_qcd"] = l_ntupleFile_qcd


# Training info
d_info = {
    
    ########## LvsR (stop) ##########
    
    "stop-lep_LvsR_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_stop_L,
        
        "inputFiles_bkg": l_ntupleFile_stop_R,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "stop-lep_LvsR_nLayer-3-DetaDphi": {
        "inputFiles_sig": l_ntupleFile_stop_L,
        
        "inputFiles_bkg": l_ntupleFile_stop_R,
        
        "layerNames": l_layerName_nLayer3_DetaDphi,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "stop-had_LvsR_nLayer-3-DetaDphi": {
        "inputFiles_sig": l_ntupleFile_stop_L,
        
        "inputFiles_bkg": l_ntupleFile_stop_R,
        
        "layerNames": l_layerName_nLayer3_DetaDphi,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "stop-had_LvsR_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_stop_L,
        
        "inputFiles_bkg": l_ntupleFile_stop_R,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    ########## LvsR (Wprime-1TeV) ##########
    
    "Wprime-1TeV-lep_LvsR_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_1TeV_L_lep,
        
        "inputFiles_bkg": l_ntupleFile_Wprime_1TeV_R_lep,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "Wprime-1TeV-had_LvsR_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_1TeV_L_had,
        
        "inputFiles_bkg": l_ntupleFile_Wprime_1TeV_R_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    ########## LvsR (Wprime-3TeV) ##########
    
    "Wprime-3TeV-lep_LvsR_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_3TeV_L_lep,
        
        "inputFiles_bkg": l_ntupleFile_Wprime_3TeV_R_lep,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "Wprime-3TeV-had_LvsR_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_3TeV_L_had,
        
        "inputFiles_bkg": l_ntupleFile_Wprime_3TeV_R_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    ########## top-tagging (ttbar) ##########
    
    "ttbar-lep_vs_qcd_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-lep_vs_qcd_nLayer-3-DetaDphi": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3_DetaDphi,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-had_vs_qcd_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-had_vs_qcd_nLayer-3-DetaDphi": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3_DetaDphi,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar_lep-vs-had_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_ttbar,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    ########## top-tagging (Wprime-1TeV) ##########
    
    "Wprime-1TeV-had_vs_qcd_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_1TeV_had,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    ########## top-tagging (Wprime-3TeV) ##########
    
    "Wprime-3TeV-had_vs_qcd_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_3TeV_had,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "Wprime-3TeV-lep_vs_qcd_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_3TeV_lep,
        
        "inputFiles_bkg": l_ntupleFile_qcd,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "Wprime-3TeV_lep-vs-had_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_Wprime_3TeV_lep,
        
        "inputFiles_bkg": l_ntupleFile_Wprime_3TeV_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
}
