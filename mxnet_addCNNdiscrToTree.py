from __future__ import print_function

import argparse
import array
import copy
import matplotlib
import matplotlib.pyplot
import mxnet
import numpy
import os
import scipy
import scipy.interpolate
import scipy.special
import tabulate
import time

import Common

import ROOT


context = mxnet.cpu()


# Argument parser
parser = argparse.ArgumentParser()

parser.add_argument(
    "--sample",
    help = "Sample",
    choices = ["ttbar", "qcd"],
    required = True,
)

parser.add_argument(
    "--nEventMax",
    help = "Maximum number of events",
    default = -1,
    type = int,
)

# Parse arguments
args = parser.parse_args()
print(args)
print()


inFileName = ""
cutStr = ""


networkSymbolFile = "mxnetNetworkInfo/network_oneLayer_relu/network_epoch020-symbol.json"
networkParamFile = "mxnetNetworkInfo/network_oneLayer_relu/network_epoch020-0000.params"
outFileName_suffix = "_oneLayer_relu_epoch020"


print("Using network symbol file: %s" %(networkSymbolFile))
print("Using network param file : %s" %(networkParamFile))
print("")


if (args.sample == "ttbar") :
    
    inFileName = "outputTree_ttbar.root"
    cutStr = "hepTop_genTop_deltaR_reco < 0.5"

elif (args.sample == "qcd") :
    
    inFileName = "outputTree_qcd.root"
    cutStr = "1"

inFile = ROOT.TFile(inFileName, "READ")

outFileName = inFileName.replace(".root", "_withCNNdiscr%s.root" %(outFileName_suffix))
outFile = ROOT.TFile(outFileName, "RECREATE")


print("Getting tree...")
tree = inFile.Get("tree").CloneTree(args.nEventMax)
#tree = inFile.Get("tree")
print("Got tree. \n")



l_varStr = [
    #"h2_hepTop_fracE_phiEtaPlane_reco",
    #"h2_hepTop_track_fracE_phiEtaPlane_reco",
    #"h2_hepTop_photon_fracE_phiEtaPlane_reco",
    #"h2_hepTop_neutralHad_fracE_phiEtaPlane_reco",
    
    "h2_hepTop_boosted_fracE_phiEtaPlane_reco",
]

l_cutVar = [
    "hepTop_genTop_deltaR_reco",
    #"hepTop_isMayBeTop_reco",
]

nVar = len(l_varStr)


neuralNetwork = mxnet.gluon.nn.SymbolBlock.imports(
    symbol_file = networkSymbolFile,
    param_file  = networkParamFile,
    input_names = ["data"],
    ctx = context,
)


v_discr = ROOT.std.vector("double")()
tree.Branch("hepTop_boosted_CNNdiscr_reco", v_discr)


if (args.nEventMax < 0) :
    
    args.nEventMax = tree.GetEntries()

else :
    
    args.nEventMax = min(args.nEventMax, tree.GetEntries())


#print(tree.GetEntries())


print("")
print("Input file: %s" %(inFileName))
print("Cut: %s" %(cutStr))
print("Events to fill: %s" %(args.nEventMax))
print("Output file: %s" %(outFileName))
print("")


for iEvent in range(0, args.nEventMax) :
    
    v_discr.clear()
    
    eventNumber = iEvent
    
    tree.GetEntry(eventNumber)
    
    a_var = numpy.empty(0)
    
    l_isValid = []
    
    nObj = len(getattr(tree, l_varStr[0]))
    
    for iObj in range(0, nObj) :
        
        cutStr_eval = cutStr
        
        for iCutVar in range(0, len(l_cutVar)) :
            
            cutVarVal = getattr(tree, l_cutVar[iCutVar])[iObj]
            
            cutStr_eval = cutStr_eval.replace(l_cutVar[iCutVar], str(cutVarVal))
        
        
        discr = -2.0
        
        
        if (eval(cutStr_eval)) :
            
            nVar = len(l_varStr)
            
            a_var = numpy.empty(0)
            
            for iVar in range(0, nVar) :
                
                varName = l_varStr[iVar]
                
                a_hist = getattr(tree, varName)
                
                hist = a_hist[iObj]
                
                nBinX = hist.GetNbinsX()
                nBinY = hist.GetNbinsY()
                
                if (not a_var.shape[0]) :
                    
                    a_var = numpy.zeros((1, nVar, nBinY, nBinX), dtype = "float32")
                
                for iBinX in range(0, nBinX) :
                    
                    for iBinY in range(0, nBinY) :
                        
                        binContent = hist.GetBinContent(iBinX+1, iBinY+1)
                        
                        a_var[0, iVar, iBinY, iBinX] = binContent
            
            
            discr = neuralNetwork(mxnet.nd.array(a_var))
            discr = discr.asnumpy().flatten()[0]
        
        
        v_discr.push_back(discr)
    
    tree.FindBranch("hepTop_boosted_CNNdiscr_reco").Fill()
    
    print("\rProcessed event %d/%d." %(iEvent+1, args.nEventMax), end = "")

print()

outFile.cd()

tree.Write()


#matplotlib.pyplot.hist(l_discr, bins = 50, histtype = "step")
#matplotlib.pyplot.show()
