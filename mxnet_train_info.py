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
    "hepTop_nExcSubJet_reco",
    
    "Whad_n_truth",
    "Wlep_n_truth",
    "Whad_pid_truth",
    "Wlep_pid_truth",
    "hepTop_nearestGenHadW_index",
    "hepTop_nearestGenLepW_index",
    "hepTop_genHadW_deltaR_reco",
    "hepTop_genLepW_deltaR_reco",
    
    "Zlep_pid_truth",
    "Zhad_pid_truth",
    "hepTop_nearestGenHadZ_index",
    "hepTop_nearestGenLepZ_index",
    "hepTop_genHadZ_deltaR_reco",
    "hepTop_genLepZ_deltaR_reco",
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


 ########## W ##########
l_ntupleFile_W_lep = [
    "outputTree/W-lep/outputTree_W-lep_001.root",
    "outputTree/W-lep/outputTree_W-lep_002.root",
    "outputTree/W-lep/outputTree_W-lep_003.root",
    "outputTree/W-lep/outputTree_W-lep_004.root",
    "outputTree/W-lep/outputTree_W-lep_005.root",
    "outputTree/W-lep/outputTree_W-lep_006.root",
    "outputTree/W-lep/outputTree_W-lep_007.root",
    "outputTree/W-lep/outputTree_W-lep_008.root",
    "outputTree/W-lep/outputTree_W-lep_009.root",
    "outputTree/W-lep/outputTree_W-lep_010.root",
    "outputTree/W-lep/outputTree_W-lep_011.root",
    "outputTree/W-lep/outputTree_W-lep_012.root",
    "outputTree/W-lep/outputTree_W-lep_013.root",
    "outputTree/W-lep/outputTree_W-lep_014.root",
    "outputTree/W-lep/outputTree_W-lep_015.root",
    "outputTree/W-lep/outputTree_W-lep_016.root",
    "outputTree/W-lep/outputTree_W-lep_017.root",
    "outputTree/W-lep/outputTree_W-lep_018.root",
    "outputTree/W-lep/outputTree_W-lep_019.root",
    "outputTree/W-lep/outputTree_W-lep_020.root",
    "outputTree/W-lep/outputTree_W-lep_021.root",
    "outputTree/W-lep/outputTree_W-lep_022.root",
    "outputTree/W-lep/outputTree_W-lep_023.root",
    "outputTree/W-lep/outputTree_W-lep_024.root",
    "outputTree/W-lep/outputTree_W-lep_025.root",
    "outputTree/W-lep/outputTree_W-lep_026.root",
    "outputTree/W-lep/outputTree_W-lep_027.root",
    "outputTree/W-lep/outputTree_W-lep_028.root",
    "outputTree/W-lep/outputTree_W-lep_029.root",
    "outputTree/W-lep/outputTree_W-lep_030.root",
    "outputTree/W-lep/outputTree_W-lep_031.root",
    "outputTree/W-lep/outputTree_W-lep_032.root",
    "outputTree/W-lep/outputTree_W-lep_033.root",
    "outputTree/W-lep/outputTree_W-lep_034.root",
    "outputTree/W-lep/outputTree_W-lep_035.root",
    "outputTree/W-lep/outputTree_W-lep_036.root",
    "outputTree/W-lep/outputTree_W-lep_037.root",
    "outputTree/W-lep/outputTree_W-lep_038.root",
    "outputTree/W-lep/outputTree_W-lep_039.root",
    "outputTree/W-lep/outputTree_W-lep_040.root",
    "outputTree/W-lep/outputTree_W-lep_041.root",
    "outputTree/W-lep/outputTree_W-lep_042.root",
    "outputTree/W-lep/outputTree_W-lep_043.root",
    "outputTree/W-lep/outputTree_W-lep_044.root",
    "outputTree/W-lep/outputTree_W-lep_045.root",
    "outputTree/W-lep/outputTree_W-lep_046.root",
    "outputTree/W-lep/outputTree_W-lep_047.root",
    "outputTree/W-lep/outputTree_W-lep_048.root",
    "outputTree/W-lep/outputTree_W-lep_049.root",
    "outputTree/W-lep/outputTree_W-lep_050.root",
    "outputTree/W-lep/outputTree_W-lep_051.root",
    "outputTree/W-lep/outputTree_W-lep_052.root",
    "outputTree/W-lep/outputTree_W-lep_053.root",
    "outputTree/W-lep/outputTree_W-lep_054.root",
    "outputTree/W-lep/outputTree_W-lep_055.root",
    "outputTree/W-lep/outputTree_W-lep_056.root",
    "outputTree/W-lep/outputTree_W-lep_057.root",
    "outputTree/W-lep/outputTree_W-lep_058.root",
    "outputTree/W-lep/outputTree_W-lep_059.root",
    "outputTree/W-lep/outputTree_W-lep_060.root",
    "outputTree/W-lep/outputTree_W-lep_061.root",
    "outputTree/W-lep/outputTree_W-lep_062.root",
    "outputTree/W-lep/outputTree_W-lep_063.root",
    "outputTree/W-lep/outputTree_W-lep_064.root",
    "outputTree/W-lep/outputTree_W-lep_065.root",
    "outputTree/W-lep/outputTree_W-lep_066.root",
    "outputTree/W-lep/outputTree_W-lep_067.root",
    "outputTree/W-lep/outputTree_W-lep_068.root",
    "outputTree/W-lep/outputTree_W-lep_069.root",
    "outputTree/W-lep/outputTree_W-lep_070.root",
    "outputTree/W-lep/outputTree_W-lep_071.root",
    "outputTree/W-lep/outputTree_W-lep_072.root",
    "outputTree/W-lep/outputTree_W-lep_073.root",
    "outputTree/W-lep/outputTree_W-lep_074.root",
    "outputTree/W-lep/outputTree_W-lep_075.root",
    "outputTree/W-lep/outputTree_W-lep_076.root",
    "outputTree/W-lep/outputTree_W-lep_077.root",
    "outputTree/W-lep/outputTree_W-lep_078.root",
    "outputTree/W-lep/outputTree_W-lep_079.root",
    "outputTree/W-lep/outputTree_W-lep_080.root",
    "outputTree/W-lep/outputTree_W-lep_081.root",
    "outputTree/W-lep/outputTree_W-lep_082.root",
    "outputTree/W-lep/outputTree_W-lep_083.root",
    "outputTree/W-lep/outputTree_W-lep_084.root",
    "outputTree/W-lep/outputTree_W-lep_085.root",
    "outputTree/W-lep/outputTree_W-lep_086.root",
    "outputTree/W-lep/outputTree_W-lep_087.root",
    "outputTree/W-lep/outputTree_W-lep_088.root",
    "outputTree/W-lep/outputTree_W-lep_089.root",
]

d_ntupleFile["l_ntupleFile_W_lep"] = l_ntupleFile_W_lep


l_ntupleFile_W_had = [
    "outputTree/W-had/outputTree_W-had_001.root",
    "outputTree/W-had/outputTree_W-had_002.root",
    "outputTree/W-had/outputTree_W-had_003.root",
    "outputTree/W-had/outputTree_W-had_004.root",
    "outputTree/W-had/outputTree_W-had_005.root",
    "outputTree/W-had/outputTree_W-had_006.root",
    "outputTree/W-had/outputTree_W-had_007.root",
    "outputTree/W-had/outputTree_W-had_008.root",
    "outputTree/W-had/outputTree_W-had_009.root",
    "outputTree/W-had/outputTree_W-had_010.root",
    "outputTree/W-had/outputTree_W-had_011.root",
    "outputTree/W-had/outputTree_W-had_012.root",
    "outputTree/W-had/outputTree_W-had_013.root",
    "outputTree/W-had/outputTree_W-had_014.root",
    "outputTree/W-had/outputTree_W-had_015.root",
    "outputTree/W-had/outputTree_W-had_016.root",
    "outputTree/W-had/outputTree_W-had_017.root",
    "outputTree/W-had/outputTree_W-had_018.root",
    "outputTree/W-had/outputTree_W-had_019.root",
    "outputTree/W-had/outputTree_W-had_020.root",
    "outputTree/W-had/outputTree_W-had_021.root",
    "outputTree/W-had/outputTree_W-had_022.root",
    "outputTree/W-had/outputTree_W-had_023.root",
    "outputTree/W-had/outputTree_W-had_024.root",
    "outputTree/W-had/outputTree_W-had_025.root",
    "outputTree/W-had/outputTree_W-had_026.root",
    "outputTree/W-had/outputTree_W-had_027.root",
    "outputTree/W-had/outputTree_W-had_028.root",
    "outputTree/W-had/outputTree_W-had_029.root",
    "outputTree/W-had/outputTree_W-had_030.root",
    "outputTree/W-had/outputTree_W-had_031.root",
    "outputTree/W-had/outputTree_W-had_032.root",
    "outputTree/W-had/outputTree_W-had_033.root",
    "outputTree/W-had/outputTree_W-had_034.root",
    "outputTree/W-had/outputTree_W-had_035.root",
    "outputTree/W-had/outputTree_W-had_036.root",
    "outputTree/W-had/outputTree_W-had_037.root",
    "outputTree/W-had/outputTree_W-had_038.root",
    "outputTree/W-had/outputTree_W-had_039.root",
    "outputTree/W-had/outputTree_W-had_040.root",
    "outputTree/W-had/outputTree_W-had_041.root",
    "outputTree/W-had/outputTree_W-had_042.root",
    "outputTree/W-had/outputTree_W-had_043.root",
    "outputTree/W-had/outputTree_W-had_044.root",
]

d_ntupleFile["l_ntupleFile_W_had"] = l_ntupleFile_W_had



 ########## Z ##########
l_ntupleFile_Z_lep = [
    "outputTree/Z-lep/outputTree_Z-lep_001.root",
    "outputTree/Z-lep/outputTree_Z-lep_002.root",
    "outputTree/Z-lep/outputTree_Z-lep_003.root",
    "outputTree/Z-lep/outputTree_Z-lep_004.root",
    "outputTree/Z-lep/outputTree_Z-lep_005.root",
    "outputTree/Z-lep/outputTree_Z-lep_006.root",
    "outputTree/Z-lep/outputTree_Z-lep_007.root",
    "outputTree/Z-lep/outputTree_Z-lep_008.root",
    "outputTree/Z-lep/outputTree_Z-lep_009.root",
    "outputTree/Z-lep/outputTree_Z-lep_010.root",
    "outputTree/Z-lep/outputTree_Z-lep_011.root",
    "outputTree/Z-lep/outputTree_Z-lep_012.root",
    "outputTree/Z-lep/outputTree_Z-lep_013.root",
    "outputTree/Z-lep/outputTree_Z-lep_014.root",
    "outputTree/Z-lep/outputTree_Z-lep_015.root",
    "outputTree/Z-lep/outputTree_Z-lep_016.root",
    "outputTree/Z-lep/outputTree_Z-lep_017.root",
    "outputTree/Z-lep/outputTree_Z-lep_018.root",
    "outputTree/Z-lep/outputTree_Z-lep_019.root",
    "outputTree/Z-lep/outputTree_Z-lep_020.root",
    "outputTree/Z-lep/outputTree_Z-lep_021.root",
    "outputTree/Z-lep/outputTree_Z-lep_022.root",
    "outputTree/Z-lep/outputTree_Z-lep_023.root",
    "outputTree/Z-lep/outputTree_Z-lep_024.root",
    "outputTree/Z-lep/outputTree_Z-lep_025.root",
    "outputTree/Z-lep/outputTree_Z-lep_026.root",
    "outputTree/Z-lep/outputTree_Z-lep_027.root",
    "outputTree/Z-lep/outputTree_Z-lep_028.root",
    "outputTree/Z-lep/outputTree_Z-lep_029.root",
    "outputTree/Z-lep/outputTree_Z-lep_030.root",
    "outputTree/Z-lep/outputTree_Z-lep_031.root",
    "outputTree/Z-lep/outputTree_Z-lep_032.root",
    "outputTree/Z-lep/outputTree_Z-lep_033.root",
    "outputTree/Z-lep/outputTree_Z-lep_034.root",
    "outputTree/Z-lep/outputTree_Z-lep_035.root",
    "outputTree/Z-lep/outputTree_Z-lep_036.root",
    "outputTree/Z-lep/outputTree_Z-lep_037.root",
    "outputTree/Z-lep/outputTree_Z-lep_038.root",
    "outputTree/Z-lep/outputTree_Z-lep_039.root",
    "outputTree/Z-lep/outputTree_Z-lep_040.root",
    "outputTree/Z-lep/outputTree_Z-lep_041.root",
]

d_ntupleFile["l_ntupleFile_Z_lep"] = l_ntupleFile_Z_lep


l_ntupleFile_Z_had = [
    "outputTree/Z-had/outputTree_Z-had_001.root",
    "outputTree/Z-had/outputTree_Z-had_002.root",
    "outputTree/Z-had/outputTree_Z-had_003.root",
    "outputTree/Z-had/outputTree_Z-had_004.root",
    "outputTree/Z-had/outputTree_Z-had_005.root",
    "outputTree/Z-had/outputTree_Z-had_006.root",
    "outputTree/Z-had/outputTree_Z-had_007.root",
    "outputTree/Z-had/outputTree_Z-had_008.root",
    "outputTree/Z-had/outputTree_Z-had_009.root",
    "outputTree/Z-had/outputTree_Z-had_010.root",
    "outputTree/Z-had/outputTree_Z-had_011.root",
    "outputTree/Z-had/outputTree_Z-had_012.root",
    "outputTree/Z-had/outputTree_Z-had_013.root",
    "outputTree/Z-had/outputTree_Z-had_014.root",
    "outputTree/Z-had/outputTree_Z-had_015.root",
    "outputTree/Z-had/outputTree_Z-had_016.root",
    "outputTree/Z-had/outputTree_Z-had_017.root",
    "outputTree/Z-had/outputTree_Z-had_018.root",
    "outputTree/Z-had/outputTree_Z-had_019.root",
    "outputTree/Z-had/outputTree_Z-had_020.root",
    "outputTree/Z-had/outputTree_Z-had_021.root",
    "outputTree/Z-had/outputTree_Z-had_022.root",
    "outputTree/Z-had/outputTree_Z-had_023.root",
    "outputTree/Z-had/outputTree_Z-had_024.root",
    "outputTree/Z-had/outputTree_Z-had_025.root",
    "outputTree/Z-had/outputTree_Z-had_026.root",
    "outputTree/Z-had/outputTree_Z-had_027.root",
    "outputTree/Z-had/outputTree_Z-had_028.root",
    "outputTree/Z-had/outputTree_Z-had_029.root",
    "outputTree/Z-had/outputTree_Z-had_030.root",
    "outputTree/Z-had/outputTree_Z-had_031.root",
    "outputTree/Z-had/outputTree_Z-had_032.root",
    "outputTree/Z-had/outputTree_Z-had_033.root",
    "outputTree/Z-had/outputTree_Z-had_034.root",
    "outputTree/Z-had/outputTree_Z-had_035.root",
    "outputTree/Z-had/outputTree_Z-had_036.root",
    "outputTree/Z-had/outputTree_Z-had_037.root",
    "outputTree/Z-had/outputTree_Z-had_038.root",
    "outputTree/Z-had/outputTree_Z-had_039.root",
    "outputTree/Z-had/outputTree_Z-had_040.root",
    "outputTree/Z-had/outputTree_Z-had_041.root",
    "outputTree/Z-had/outputTree_Z-had_042.root",
]

d_ntupleFile["l_ntupleFile_Z_had"] = l_ntupleFile_Z_had


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
    
    
    "ttbar-had_vs_W-had_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_W_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadW_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-had_vs_Z-had_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_Z_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genHadTop_deltaR_reco < 1 and hepTop_genHadTop_deltaR_reco < hepTop_genLepTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadZ_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
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
    
    
    "ttbar-lep_vs_W-lep_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_W_lep,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genLepW_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-lep_vs_W-had_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_W_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadW_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-lep_vs_Z-lep_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_Z_lep,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genLepZ_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "varNames": l_varName_common,
    },
    
    
    "ttbar-lep_vs_Z-had_nLayer-3": {
        "inputFiles_sig": l_ntupleFile_ttbar,
        
        "inputFiles_bkg": l_ntupleFile_Z_had,
        
        "layerNames": l_layerName_nLayer3,
        
        "cutStr_sig": "hepTop_genLepTop_deltaR_reco < 1 and hepTop_genLepTop_deltaR_reco < hepTop_genHadTop_deltaR_reco and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
        "cutStr_bkg": "hepTop_genHadZ_deltaR_reco < 1 and hepTop_pT_reco > 200 and hepTop_nExcSubJet_reco >= 3",
        
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
