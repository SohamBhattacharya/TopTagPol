from __future__ import print_function

import array
import copy
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot
import matplotlib.ticker
import mxnet
import numpy
import scipy
import os
import pprint
import tabulate
import time

#import Common

import ROOT
import ROOT.TColor


ROOT.gSystem.Load("HeaderFiles/CustomRootDict_cc.so")


ROOT.gStyle.SetOptStat(0)
#ROOT.gStyle.SetOptStat(111111111)

ROOT.gStyle.SetStatFormat("0.6e")

#ROOT.gStyle.SetPalette(ROOT.kRainBow)
#ROOT.gStyle.SetPalette(ROOT.kBlueRedYellow)
#ROOT.gStyle.SetPalette(ROOT.kCubehelix)
#ROOT.gStyle.SetPalette(ROOT.kColorPrintableOnGrey)
ROOT.gStyle.SetPalette(ROOT.kVisibleSpectrum)

ROOT.gStyle.SetNumberContours(50)

#print(ROOT.kCubehelix)

#ROOT.InvertPalette()

#l_stop = array.array("d", numpy.array(range(0, 9)) * 0.125)
#l_red   = array.array("d", numpy.array([18.0,  72.0,   5.0,  23.0,  29.0, 201.0, 200.0, 98.0, 29.0]) / 255.0)
#l_green = array.array("d", numpy.array([ 0.0,   0.0,  43.0, 167.0, 211.0, 117.0,   0.0,  0.0,  0.0]) / 255.0)
#l_blue  = array.array("d", numpy.array([51.0, 203.0, 177.0,  26.0,  10.0,   9.0,   8.0,  3.0,  0.0]) / 255.0)


#l_red   = array.array("d", numpy.array([18,  72,   5,  23,  29, 251, 201, 200, 200, 150, 98, 60, 29], dtype = "f") / 255)
#l_green = array.array("d", numpy.array([ 0,   0,  43, 167, 211, 177, 117,  50,   0,   0,  0,  0,  0], dtype = "f") / 255)
#l_blue  = array.array("d", numpy.array([51, 203, 177,  26,  10,  23,   9,   9,   8,   5,  3,  0,  0], dtype = "f") / 255)
#nStop = len(l_red)
#l_stop = array.array("d", numpy.array(range(0, nStop)) * 1.0 / (nStop-1))

#l_stop = array.array("d", numpy.array(range(0, 17)) * 0.0625)
#l_red   = array.array("d", numpy.array(range(0, 17)) / 16.0 * 255.0)
#l_green = array.array("d", numpy.array(range(0, 17)) / 16.0 * 255.0)
#l_blue  = array.array("d", numpy.array(range(0, 17)) / 16.0 * 255.0)


#Idx = ROOT.TColor.CreateGradientColorTable(len(l_stop), l_stop, l_red, l_green, l_blue, 255, 1.0);



def getImageHist(
    tree,
    varName,
    l_cutVar = [],
    cutStr = "1",
    nEvent_max = -1,
    ) :
    
    nEventSel = tree.GetEntries()
    
    l_var = []
    
    hist_sum = 0
    
    eventCount = 0
    
    for iEvent in range(0, nEventSel) :
        
        #eventNumber = eventList_temp.GetEntry(iEvent)
        eventNumber = iEvent
        
        #print("Event %d: \n" %(iEvent))
        
        tree.GetEntry(eventNumber)
        
        a_hist = getattr(tree, varName)
        
        nHist = len(a_hist)
        
        for iHist in range(0, nHist) :
            
            cutStr_eval = cutStr
            
            for iCutVar in range(0, len(l_cutVar)) :
                
                cutVarVal = getattr(tree, l_cutVar[iCutVar])[iHist]
                
                cutStr_eval = cutStr_eval.replace(l_cutVar[iCutVar], str(cutVarVal))
            
            #print(iEvent, iHist, cutStr_eval)
            
            if (not eval(cutStr_eval)) :
                
                continue
            
            #varValue = getattr(tree, varInfo.varName)
            #
            #if (varInfo.varIndex >= 0) :
            #    
            #    varValue = varValue[varInfo.varIndex]
            #
            #print varValue
            #
            #l_var.append(varValue)
            
            hist = a_hist[iHist]
            
            if (not hist_sum) :
                
                hist_sum = hist.Clone()
            
            else :
                
                hist_sum.Add(hist)
            
            #print("\t", arr.sum())
            
            eventCount += 1
            
            print("\rGot image %d/%d." %(eventCount, nEvent_max), end = "")
            
            if (eventCount == nEvent_max) :
                
                break
        
        if (eventCount == nEvent_max) :
                
                break
    
    print("")
    print("# images: %d \n" %(eventCount))
    
    hist_sum.Scale(1.0 / eventCount)
    
    return hist_sum


class Options :
    
    sample = ""
    varStr = ""
    cutStr = ""
    title = ""
    outFileName = ""


l_options = []


# ##### ttbar #####
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
#options_temp.title = "Hadronic top jet"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_boosted.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
#options_temp.title = "Hadronic top jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_boosted_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
#options_temp.title = "Hadronic top jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_boosted_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
#options_temp.title = "Hadronic top jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_boosted_neutralHad.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top jet"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_lepTop_boosted.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_lepTop_boosted_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_lepTop_boosted_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "ttbar"
#options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_ttbar_lepTop_boosted_neutralHad.pdf"
#l_options.append(options_temp)


 ##### stop-L #####

options_temp = Options()
options_temp.sample = "stop-L"
options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (left-handed) jet"
options_temp.outFileName = "plots/jetImage/jetImage_stop-L_boosted.pdf"
l_options.append(options_temp)


options_temp = Options()
options_temp.sample = "stop-L"
options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (left-handed) jet (tracks)"
options_temp.outFileName = "plots/jetImage/jetImage_stop-L_boosted_track.pdf"
l_options.append(options_temp)


options_temp = Options()
options_temp.sample = "stop-L"
options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (left-handed) jet (photons)"
options_temp.outFileName = "plots/jetImage/jetImage_stop-L_boosted_photon.pdf"
l_options.append(options_temp)


options_temp = Options()
options_temp.sample = "stop-L"
options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (left-handed) jet (neutral hadrons)"
options_temp.outFileName = "plots/jetImage/jetImage_stop-L_boosted_neutralHad.pdf"
l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_neutralHad.pdf"
#l_options.append(options_temp)



#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_rescaled.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_rescaled_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_rescaled_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (left-handed) jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_topRestFrame_rescaled_neutralHad.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (left-handed) jet"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_lepTop_boosted.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (left-handed) jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_lepTop_boosted_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (left-handed) jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_lepTop_boosted_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-L"
#options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (left-handed) jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-L_lepTop_boosted_neutralHad.pdf"
#l_options.append(options_temp)


 ##### stop-R #####

options_temp = Options()
options_temp.sample = "stop-R"
options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (right-handed) jet"
options_temp.outFileName = "plots/jetImage/jetImage_stop-R_boosted.pdf"
l_options.append(options_temp)


options_temp = Options()
options_temp.sample = "stop-R"
options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (right-handed) jet (tracks)"
options_temp.outFileName = "plots/jetImage/jetImage_stop-R_boosted_track.pdf"
l_options.append(options_temp)


options_temp = Options()
options_temp.sample = "stop-R"
options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (right-handed) jet (photons)"
options_temp.outFileName = "plots/jetImage/jetImage_stop-R_boosted_photon.pdf"
l_options.append(options_temp)


options_temp = Options()
options_temp.sample = "stop-R"
options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5"
options_temp.title = "Hadronic top (right-handed) jet (neutral hadrons)"
options_temp.outFileName = "plots/jetImage/jetImage_stop-R_boosted_neutralHad.pdf"
l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_neutralHad.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_rescaled.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_rescaled_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_rescaled_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genHadTop_deltaR_reco < 0.5 and hepTop_isMayBeTop_reco"
#options_temp.title = "Hadronic top (right-handed) jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_topRestFrame_rescaled_neutralHad.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (right-handed) jet"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_lepTop_boosted.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (right-handed) jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_lepTop_boosted_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (right-handed) jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_lepTop_boosted_photon.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "stop-R"
#options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "hepTop_genLepTop_deltaR_reco < 0.8"
#options_temp.title = "Leptonic top (right-handed) jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_stop-R_lepTop_boosted_neutralHad.pdf"
#l_options.append(options_temp)


# ##### qcd #####
#
#options_temp = Options()
#options_temp.sample = "qcd"
#options_temp.varStr = "h2_hepTop_boosted_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "1"
#options_temp.title = "QCD jet"
#options_temp.outFileName = "plots/jetImage/jetImage_qcd_boosted.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "qcd"
#options_temp.varStr = "h2_hepTop_boosted_track_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "1"
#options_temp.title = "QCD jet (tracks)"
#options_temp.outFileName = "plots/jetImage/jetImage_qcd_boosted_track.pdf"
#l_options.append(options_temp)
#
#
#options_temp = Options()
#options_temp.sample = "qcd"
#options_temp.varStr = "h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "1"
#options_temp.title = "QCD jet (photons)"
#options_temp.outFileName = "plots/jetImage/jetImage_qcd_boosted_photon.pdf"
#l_options.append(options_temp)


#options_temp = Options()
#options_temp.sample = "qcd"
#options_temp.varStr = "h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco"
#options_temp.cutStr = "1"
#options_temp.title = "QCD jet (neutral hadrons)"
#options_temp.outFileName = "plots/jetImage/jetImage_qcd_boosted_neutralHad.pdf"
#l_options.append(options_temp)


for options in l_options :
    
    if (options.sample == "ttbar") :
        
        inFileName = "outputTree_ttbar.root"
        inFile = ROOT.TFile(inFileName)
        tree = inFile.Get("tree")
    
    
    if (options.sample == "stop-L") :
        
        inFileName = "outputTree_stop-L.root"
        inFile = ROOT.TFile(inFileName)
        tree = inFile.Get("tree")
    
    
    if (options.sample == "stop-R") :
        
        inFileName = "outputTree_stop-R.root"
        inFile = ROOT.TFile(inFileName)
        tree = inFile.Get("tree")
    
    
    if (options.sample == "qcd") :
    
        inFileName = "outputTree_qcd.root"
        inFile = ROOT.TFile(inFileName)
        tree = inFile.Get("tree")
    
    
    cutStr = options.cutStr
    title = options.title
    varStr = options.varStr
    outFileName = options.outFileName
    
    
    l_cutVar = [
        "hepTop_genHadTop_deltaR_reco",
        "hepTop_genLepTop_deltaR_reco",
        "hepTop_isMayBeTop_reco",
    ]
    
    
    print("")
    print("*"*50)
    print("Input file: %s" %(inFileName))
    print("Plotting: %s" %(varStr))
    print("Cut: %s" %(cutStr))
    print("")
    
    hist = getImageHist(
        tree = tree,
        varName = varStr,
        l_cutVar = l_cutVar,
        cutStr = cutStr,
        #nEvent_max = -1,
        nEvent_max = 500000,
    )
    
    print("Integral: %0.4e" %(hist.Integral()))
    
    hist.SetTitle(title)
    
    #hist.SetMinimum(1e-7)
    hist.SetMinimum(1e-6)
    
    #hist.SetMaximum(1.0)
    hist.SetMaximum(1e-1)
    
    canvas = ROOT.TCanvas("canvas_temp", "canvas_temp")
    canvas.cd()
    
    hist.Draw("colz")
    
    canvas.SetLogz()
    
    canvas.SaveAs(outFileName)
    
    #canvas.SaveAs()
    
    canvas.Clear()
    canvas.Close()
    
    print("\n\n")
