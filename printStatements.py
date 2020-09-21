import os


outfileName = "statements.txt"

toReplace = "$$$"

l_str = [
    "lepTop_pT_truth",
    "lepTop_eta_truth",
    "lepTop_phi_truth",
    "lepTop_E_truth",
    "lepTop_px_truth",
    "lepTop_py_truth",
    "lepTop_pz_truth",
    
    "lepTopB_pT_truth",
    "lepTopB_eta_truth",
    "lepTopB_phi_truth",
    "lepTopB_E_truth",
    "lepTopB_px_truth",
    "lepTopB_py_truth",
    "lepTopB_pz_truth",
    
    "lepTopW_pT_truth",
    "lepTopW_eta_truth",
    "lepTopW_phi_truth",
    "lepTopW_E_truth",
    "lepTopW_px_truth",
    "lepTopW_py_truth",
    "lepTopW_pz_truth",
    
    "Wlep_pT_truth",
    "Wlep_eta_truth",
    "Wlep_phi_truth",
    "Wlep_E_truth",
    "Wlep_px_truth",
    "Wlep_py_truth",
    "Wlep_pz_truth",
    "Wlep_pid_truth",
]


templateStr = (
    #"sprintf(name, \"%s\");\n"
    #"tree->Branch(name, &v_%s);"
    
    "tree->Branch(\"%s\", &v_%s);"
)
linegaps = 0


#templateStr = (
#    "treeOutput->v_%s.push_back();"
#)
#linegaps = 0



with open(outfileName, "w") as f :
    
    for iEntry in range(0, len(l_str)) :
        
        #temp_str = templateStr %(l_str[iEntry])
        temp_str = templateStr
        temp_str = temp_str.replace("%s", l_str[iEntry])
        
        print temp_str + "\n" * linegaps
        
        temp_str += "\n"
        temp_str += "\n" * linegaps
        
        f.write(temp_str)
        

