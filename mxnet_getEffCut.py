from __future__ import print_function

import argparse
import array
import copy
import getpass
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot
#import mxnet
import multiprocessing
import numexpr
import numpy
import os
import pprint
import scipy
import scipy.interpolate
import scipy.special
import tabulate
import time

import Common
import mxnet_train_info

import ROOT


#matplotlib.pyplot.rc("text", usetex = True)
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{amsmath}"]
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{slashed}"]


#context = mxnet.cpu()

#username = getpass.getuser()


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


#parser.add_argument(
#    "--nEventMax",
#    help = "Number of signal and background (each) events to be used",
#    type = int,
#    required = False,
#    default = 500000,
#)

parser.add_argument(
    "--process",
    help = "Process name: \n%s" %("\n".join(sorted(mxnet_train_info.d_ntupleFile.keys()))),
    type = str,
    choices = mxnet_train_info.d_ntupleFile.keys(),
    required = True,
    metavar = "PROCESS",
)

parser.add_argument(
    "--extraDirSuffixList",
    help = "Extra directory suffix (to be added as friend trees)",
    type = str,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--effVar",
    help = "Name of the variable to be used to calculate the efficiency",
    type = str,
    required = True,
)

parser.add_argument(
    "--cutNum",
    help = "Cut to be applied to the numerator",
    type = str,
    required = True,
)

parser.add_argument(
    "--cutDen",
    help = "Cut to be applied to the denominator",
    type = str,
    required = True,
)

parser.add_argument(
    "--effList",
    help = "List of efficiencies (in %%) for which the cut values are to be obtained",
    type = float,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--relDiff",
    help = "Iteration to stop when the calculated efficiency is within RELDIFF%% within the required efficiency\nDefault: %(default)f%%",
    type = float,
    required = False,
    default = 1,
)


def getEffCut(argList = None) :
    
    # Parse arguments
    if (argList is None) :
        
        args = parser.parse_args()
    
    else :
        
        args = parser.parse_args(argList)
    
    d_args = vars(args)
    
    
    import root_numpy
    
    
    l_inFileName = mxnet_train_info.d_ntupleFile[args.process]
    
    tree = ROOT.TChain("tree")
    
    for iFile in range(0, len(l_inFileName)) :
        
        tree.Add(l_inFileName[iFile])
    
    
    l_extraTree = []
    
    
    if (args.extraDirSuffixList is not None) :
        
        for iExtra, extraDirSuffix in enumerate(args.extraDirSuffixList) :
            
            tree_extra = ROOT.TChain("tree")
            
            for iFile, iFileName in enumerate(l_inFileName) :
                
                iFileName_extra = "%s_%s%s" %(
                    iFileName[0: iFileName.rfind("/")],
                    extraDirSuffix,
                    iFileName[iFileName.rfind("/"):],
                )
                
                #l_inFileName_extra.extend([iFileName_extra])
                
                tree_extra.Add(iFileName_extra)
            
            l_extraTree.append(tree_extra)
            
            tree.AddFriend(tree_extra)
    
    
    l_varName = []
    #l_branch = ["hepTop_pT_reco", "hepTop_genHadTop_deltaR_reco", "hepTop_nExcSubJet_reco"]
    
    
    
    #tree.GetEntry(0)
    #print(getattr(tree, "hepTop_CNN_reco"))
    
    for iTree in [tree]+l_extraTree :
        
        treeBranches = iTree.GetListOfBranches()
        
        for iBr in range(0, treeBranches.GetEntries()) :
            
            brName = treeBranches.At(iBr).GetName()
            
            if (brName not in l_varName and (
                brName in args.effVar or
                brName in args.cutNum or
                brName in args.cutDen
            )) :
                
                #print(brName)
                l_varName.append(brName)
    
    print(l_varName)
    
    
    a_tree = numpy.array(root_numpy.tree2array(
        tree,
        branches = l_varName,
        #selection = args.cutNum,
        #start = 0,
        #stop = 10,
    ).tolist())
    
    #print(a_tree)
    #print(a_tree.shape)
    #print(type(a_tree))
    
    #a_var0 = numpy.concatenate(a_tree[:, 0])
    ##print(a_var0)
    #print(a_var0.shape)
    #
    #print(getattr(tree, l_branch[0]))
    #
    #print(tree.GetListOfBranches().GetEntries())
    #print(tree.GetListOfBranches().At(0).GetName())
    
    
    #print(dir(tree))
    #print(vars(tree))
    
    
    d_var = {}
    
    
    for iVar, varName in enumerate(l_varName) :
        
        d_var[varName] = numpy.concatenate(a_tree[:, iVar])
    
    
    # Can handle arrays with logival expressions
    a_eval_num = numexpr.evaluate(args.cutNum, local_dict = d_var).astype(bool)
    a_eval_den = numexpr.evaluate(args.cutDen, local_dict = d_var).astype(bool)
    
    
    d_var["a_eval_num"] = a_eval_num
    
    
    #print(a_eval_num)
    #print(numpy.sum(a_eval_num))
    
    
    den = float(numpy.sum(a_eval_den))
    
    for iEff, eff0 in enumerate(args.effList) :
        
        effVar_min = min(d_var[args.effVar])
        effVar_max = max(d_var[args.effVar])
        
        eff = 0
        eff_prev = 0
        dEff = 9999
        effCut = 9999
        
        while (abs(dEff) > args.relDiff) :
            
            effCut = float(effVar_min+effVar_max)/2.0
            
            effStr = "(a_eval_num == 1) & (%s > %f)" %(args.effVar, effCut)
            
            a_eval_eff = numexpr.evaluate(effStr, local_dict = d_var).astype(bool)
            
            num = float(numpy.sum(a_eval_eff))
            
            eff_prev = eff
            eff = num / den * 100
            dEff = abs(eff - eff0) / eff0 * 100
            dEff_prev = abs(eff - eff_prev) / eff * 100
            
            if (eff < eff0) :
                
                effVar_max = effCut
            
            elif (eff > eff0) :
                
                effVar_min = effCut
            
            
            #print(eff, eff_prev, dEff, effCut)
            
            if (dEff_prev < args.relDiff/10.0) :
                
                break
        
        
        #print(eff0, eff, effCut)
        #print("\n\n")
        
        print("Required eff.: %0.2f%%, Calculated eff. %0.2f%%, Cut: %0.4f" %(eff0, eff, effCut))
    


if (__name__ == "__main__") :
    
    getEffCut()
