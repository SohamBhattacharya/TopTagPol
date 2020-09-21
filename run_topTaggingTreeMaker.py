import argparse
import numpy
import os
import subprocess


cppFileName = "topTaggingTreeMaker.cc"
cppFileName_noExt = cppFileName[: cppFileName.find(".")]


d_info = {
    "stop-L": {
        "name": "stop-L",
        "outputDir": "outputTree/stop-L",
        "inputFiles": [
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_01/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_02/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_03/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_04/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_05/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_06/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_07/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_08/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_09/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_10/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_11/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_12/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_13/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_14/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_15/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/run_16/unweighted_events.lhe.hepmc.root",
            
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L17.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L18.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L19.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L20.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L21.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L22.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L23.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L24.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L25.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L26.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L27.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L28.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L29.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L30.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L31.root",
            "/home/sobhatta/work/MCsamples/STOP/LEFT/L32.root",
        ],
    },
    
    
    "stop-R": {
        "name": "stop-R",
        "outputDir": "outputTree/stop-R",
        "inputFiles": [
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_01/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_02/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_03/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_04/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_05/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_06/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_07/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_08/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_09/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_10/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_11/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_12/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_13/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_14/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_15/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/run_16/unweighted_events.lhe.hepmc.root",
            
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R17.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R18.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R19.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R20.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R21.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R22.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R23.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R24.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R25.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R26.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R27.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R28.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R29.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R30.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R31.root",
            "/home/sobhatta/work/MCsamples/STOP/RIGHT/R32.root",
        ],
    },
    
    
    "Wprime-1TeV-L-lep": {
        "name": "Wprime-1TeV-L-lep",
        "outputDir": "outputTree/Wprime-1TeV-L-lep",
        "inputFiles": [ 
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept/Events/run_10/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "Wprime-1TeV-L-had": {
        "name": "Wprime-1TeV-L-had",
        "outputDir": "outputTree/Wprime-1TeV-L-had",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had/Events/run_10/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "Wprime-1TeV-R-lep": {
        "name": "Wprime-1TeV-R-lep",
        "outputDir": "outputTree/Wprime-1TeV-R-lep",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept/Events/run_10/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "Wprime-1TeV-R-had": {
        "name": "Wprime-1TeV-R-had",
        "outputDir": "outputTree/Wprime-1TeV-R-had",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had/Events/run_10/unweighted_events.lhe.hepmc.root",
        ]
    },
    
    
    "Wprime-3TeV-L-lep": {
        "name": "Wprime-3TeV-L-lep",
        "outputDir": "outputTree/Wprime-3TeV-L-lep",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_lept_3/Events/run_10/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "Wprime-3TeV-L-had": {
        "name": "Wprime-3TeV-L-had",
        "outputDir": "outputTree/Wprime-3TeV-L-had",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_left_had_3/Events/run_10/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "Wprime-3TeV-R-lep": {
        "name": "Wprime-3TeV-R-lep",
        "outputDir": "outputTree/Wprime-3TeV-R-lep",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_lept_3/Events/run_10/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "Wprime-3TeV-R-had": {
        "name": "Wprime-3TeV-R-had",
        "outputDir": "outputTree/Wprime-3TeV-R-had",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_01/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_02/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_03/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_04/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_05/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_06/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_07/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_08/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_09/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/wprime_right_had_3/Events/run_10/unweighted_events.lhe.hepmc.root",
        ]
    },
    
    
    "ttbar-tj": {
        "name": "ttbar-tj",
        "outputDir": "outputTree/ttbar-tj",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_01_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_02_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_03_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_04_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_05_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_06_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_07_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_08_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_09_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_10_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_11_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_12_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_13_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_14_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_15_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_16_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_17_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_18_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_19_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar/Events/run_20_decayed_1/unweighted_events.lhe.hepmc.root",
            
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_01_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_02_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_03_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_04_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_05_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_06_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_07_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TJ/run_08_decayed_1/unweighted_events.lhe.hepmc.root",
        ]
    },
    
    
    "ttbar-tbarj": {
        "name": "ttbar-tbarj",
        "outputDir": "outputTree/ttbar-tbarj",
        "inputFiles": [
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_01_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_02_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_03_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_04_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_05_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_06_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_07_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_08_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_09_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_10_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_11_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_12_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_13_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_14_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_15_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_16_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_17_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_18_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_19_decayed_1/unweighted_events.lhe.hepmc.root",
            "/grid_mnt/t3storage3/arvind/MG5_aMC_v2_6_7/ttbar2/Events/run_20_decayed_1/unweighted_events.lhe.hepmc.root",
            
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_09_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_10_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_11_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_12_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_13_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_14_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_15_decayed_1/unweighted_events.lhe.hepmc.root",
            "/home/sobhatta/work/MCsamples/TTBAR/TBARJ/run_16_decayed_1/unweighted_events.lhe.hepmc.root",
        ],
    },
    
    
    "qcd": {
        "name": "qcd",
        "outputDir": "outputTree/qcd",
        "inputFiles": [
            "/home/sobhatta/work/MCsamples/QCD/0/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/1/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/2/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/3/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/4/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/5/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/6/hepmc.fifo.root",
            "/home/sobhatta/work/MCsamples/QCD/7/hepmc.fifo.root",
        ]
    },
}


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

l_sampleInfo = ["%s (%d files)" %(key, len(d_info[key]["inputFiles"])) for key in sorted(d_info.keys())]

parser.add_argument(
    "--samples",
    #help = "List (space separated) of the samples to run: \n%s" %("\n".join(sorted(d_info.keys()))),
    help = "List (space separated) of the samples to run: \n%s" %("\n".join(l_sampleInfo)),
    nargs = "*",
    type = str,
    choices = d_info.keys(),
    required = True,
)

parser.add_argument(
    "--maxFiles",
    help = "Maximum number of files for each sample",
    type = int,
    required = False,
    default = -1,
)

parser.add_argument(
    "--suffix",
    help = "Output directory name suffix (including the leading separator, for eg. \"_suffix\")",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--extraArgs",
    help = "Extra arguments to be passed to the executable. For eg.: --extraArgs \"--maxEvents 1000\"",
    type = str,
    required = False,
    default = "",
)


# Parse arguments
args = parser.parse_args()


# Compile
#cmdStr = "g++mod.sh h %s" %(cppFileName)
#
#print("Compiling: %s \n" %(cmdStr))
#cmdReturn = os.system(cmdStr)
#
#
#if(cmdReturn) :
#    
#    print("\n")
#    print("Compilation failed. \n")
#    
#    exit(1)


for key in args.samples :
    
    print("\n\n")
    print("*"*50)
    print("*"*50)
    print("Running: %s" %(key)) 
    print("*"*50)
    print("*"*50)
    print("")
    
    l_inputFile = d_info[key]["inputFiles"]
    
    outDir = "%s%s" %(d_info[key]["outputDir"], args.suffix)
    
    if (os.path.isdir(outDir)) :
        
        outputDir_old = subprocess.check_output(["date", "+%Y-%m-%d_%H-%M-%S", "-r", outDir]).strip()
        outputDir_old = outputDir_old.decode("UTF-8") # Convert from bytes to string
        outputDir_old = "%s_%s" %(outDir, str(outputDir_old))
        
        cmdStr = "mv %s %s" %(outDir, outputDir_old)
        
        print("Output directory exists. Renaming it:")
        print(cmdStr)
        print("")
        
        cmdReturn = os.system(cmdStr)
        
    
    print("Creating output directory: %s" %(outDir))
    os.system("mkdir -p %s" %(outDir))
    
    print("Copying cpp file to output directory.")
    os.system("cp %s %s/" %(cppFileName, outDir))
    
    print("")
    
    
    # Compile
    cmdStr = "g++mod.sh h %s/%s -I./" %(outDir, cppFileName)
    
    print("Compiling: %s \n" %(cmdStr))
    cmdReturn = os.system(cmdStr)
    
    
    if(cmdReturn) :
        
        print("\n")
        print("Compilation failed. \n")
        
        exit(1)
    
    
    maxFiles = len(l_inputFile)
    
    if (args.maxFiles > 0) :
        
        maxFiles = min(args.maxFiles, maxFiles)
    
    for iFile in range(0, maxFiles) :
        
        inputFile = l_inputFile[iFile]
        outputFile = "outputTree_%s_%03d.root" %(d_info[key]["name"], iFile+1)
        
        logDir = "%s/logs" %(outDir)
        os.system("mkdir -p %s" %(logDir))
        
        logFile = "%s/%s_%s_%03d.log" %(logDir, cppFileName_noExt, d_info[key]["name"], iFile+1)
        
        cmdStr = (
            "nohup "
            "./%s/%s "
            "--inFileNames %s "
            "--outDir %s "
            "--outFileName %s "
            "%s "
            "&> %s "
            "&"
            
            %(
                outDir, cppFileName_noExt,
                inputFile,
                outDir,
                outputFile,
                args.extraArgs,
                logFile
            )
        )
        
        print("Command: %s \n" %(cmdStr))
        cmdReturn = os.system(cmdStr)

