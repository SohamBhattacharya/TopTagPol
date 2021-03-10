import os


outfileName = "statements.txt"

toReplace = "$$$"

l_str = [
    "hadZ_n_truth",
    "hadZ_pT_truth",
    "hadZ_eta_truth",
    "hadZ_phi_truth",
    "hadZ_m_truth",
    "hadZ_E_truth",
    "hadZ_px_truth",
    "hadZ_py_truth",
    "hadZ_pz_truth",
    
    "Zq1_pT_truth",
    "Zq1_eta_truth",
    "Zq1_phi_truth",
    "Zq1_E_truth",
    "Zq1_px_truth",
    "Zq1_py_truth",
    "Zq1_pz_truth",
    "Zq1_pid_truth",
    "Zq1_Zq2deltaR_truth",

    "Zq2_pT_truth",
    "Zq2_eta_truth",
    "Zq2_phi_truth",
    "Zq2_E_truth",
    "Zq2_px_truth",
    "Zq2_py_truth",
    "Zq2_pz_truth",
    "Zq2_pid_truth",
    
    "lepZ_n_truth",
    "lepZ_pT_truth",
    "lepZ_eta_truth",
    "lepZ_phi_truth",
    "lepZ_m_truth",
    "lepZ_E_truth",
    "lepZ_px_truth",
    "lepZ_py_truth",
    "lepZ_pz_truth",
    
    "Zlep1_pT_truth",
    "Zlep1_eta_truth",
    "Zlep1_phi_truth",
    "Zlep1_E_truth",
    "Zlep1_px_truth",
    "Zlep1_py_truth",
    "Zlep1_pz_truth",
    "Zlep1_pid_truth",
    "Zlep1_Zlep2deltaR_truth",
    
    "Zlep2_pT_truth",
    "Zlep2_eta_truth",
    "Zlep2_phi_truth",
    "Zlep2_E_truth",
    "Zlep2_px_truth",
    "Zlep2_py_truth",
    "Zlep2_pz_truth",
    "Zlep2_pid_truth",
]


templateStr = (
    #"sprintf(name, \"%s\")",\n"
    #"tree->Branch(name, &v_%s)","
    
    "tree->Branch(\"{name}\", &v_{name});"
)
linegaps = 0


#templateStr = (
#    "treeOutput->v_%s.push_back()","
#)
#linegaps = 0



with open(outfileName, "w") as f :
    
    for iEntry in range(0, len(l_str)) :
        
        #temp_str = templateStr %(l_str[iEntry])
        temp_str = templateStr
        temp_str = temp_str.format(name = l_str[iEntry])
        
        print temp_str + "\n" * linegaps
        
        temp_str += "\n"
        temp_str += "\n" * linegaps
        
        f.write(temp_str)
        

