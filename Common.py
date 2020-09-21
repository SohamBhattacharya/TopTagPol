#from __future__ import print_function

import array
import ctypes
import gc
import matplotlib
import matplotlib.pyplot
#import multiprocessing
#import numba
import numpy
import os
import pprint
import psutil
import resource
import scipy
import scipy.interpolate
import scipy.special
import subprocess
import sys
import time
import weakref
import xml
import xml.etree.ElementTree
import xmltodict

#import pickle4reducer
import multiprocessing

import ROOT

import tdrstyle

##from numba import jit


initVal = -9999

someNonExistantString = "someNonExistantString"


_shared_np_array_image = numpy.empty(0)
_shared_np_array_other = numpy.empty(0)


_decref = ctypes.pythonapi.Py_DecRef
_decref.argtypes = [ctypes.py_object]
_decref.restype = None


class TrainingVarInfo :
    
    varStr = ""
    varName = ""
    varIndex = -1
    
    a_sig = None
    a_bkg = None
    
    a_spec_sig = None
    a_spec_bkg = None


class HistogramDetails :
    
    rootFileName = ""
    rootFile = None
    
    treeName = ""
    
    histName = ""
    histTitle = ""
    histLabel = ""
    
    titleSizeScale = 1
    titleOffsetScale = 1
    
    lineColor = 4
    lineStyle = 1
    lineWidth = 1
    
    markerStyle = 20
    markerColor = 4
    markerSize = -1
    
    fillStyle = -1
    
    hist = None
    
    xTitle = ""
    yTitle = ""
    zTitle = ""
    
    xMin = initVal
    xMax = initVal
    
    yMin = initVal
    yMax = initVal
    
    zMin = initVal
    zMax = initVal
    
    logX = False
    logY = False
    logZ = False
    
    gridX = False
    gridY = False
    
    nDivisionsX = [0, 0, 0]
    nDivisionsY = [0, 0, 0]
    
    centerLabelsX = False
    centerLabelsY = False
    centerLabelsZ = False
    
    xTitleSizeScale = 1
    yTitleSizeScale = 1
    zTitleSizeScale = 1
    
    xTitleOffsetScale = 1
    yTitleOffsetScale = 1
    zTitleOffsetScale = 1
    
    xLabelSizeScale = 1
    yLabelSizeScale = 1
    zLabelSizeScale = 1
    
    drawOption = "hist"
    drawFunctions = True
    
    addToLegend = True
    
    outFileName = ""
    outFileName_suffix = ""


def freeCTypeMemory(obj) :
    
    obj_ref = str(weakref.ref(obj))
    
    while("dead" not in obj_ref) :
        
        _decref(obj)
        
        obj_ref = str(weakref.ref(obj))


def mergeListsAlternating(list1, list2) :
    
    mergedList_len = len(list1) + len(list2)
    
    min_len = min(len(list1), len(list2))
    mergedList = [None]*(2*min_len)
    
    mergedList[0::2] = list1[0: min_len]
    mergedList[1::2] = list2[0: min_len]
    
    mergedList.extend(list1[min_len:])
    mergedList.extend(list2[min_len:])
    
    return mergedList


def renameAndBackupDir(dirName) :
    
    if (os.path.isdir(dirName)) :
        
        dirName_old = subprocess.check_output(["date", "+%Y-%m-%d_%H-%M-%S", "-r", dirName]).decode().strip()
        
        dirName_old = "%s_%s" %(dirName, dirName_old)
        
        cmdStr = "mv %s %s" %(dirName, dirName_old)
        
        print("Directory exists. Renaming it:")
        print(cmdStr)
        print("")
        
        cmdReturn = os.system(cmdStr)


def replaceIndexedVar(
    varStr,
    tree,
    ) :
    
    varStr_mod = varStr
    
    l_varTok = varStr.strip().split()
    
    #print("\n", "#"*10, varStr, "\n")
    
    for iVar, varTok in enumerate(l_varTok) :
        
        if ("[" not in varTok) :
            
            continue
        
        varName = varTok[0: varTok.find("[")]
        #print("\n", "*"*10, varTok, "\n")
        varIndex = int(float(varTok[varTok.find("[")+1: varTok.find("]")]))
        
        varVal = 0
        
        if (varIndex >= 0) :
            
            varVal = getattr(tree, varName)[varIndex]
        
        varStr_mod = varStr_mod.replace(varTok, str(varVal))
    
    
    #print(varStr_mod)
    
    return varStr_mod


def getNpassedFromTree(
    tree,
    varName,
    l_cutVar = [],
    cutStr = "1",
    nSel_max = -1,
    splitEvery = -1, # Will return the list of eventNumbers that correspond to every splitEvery-th selected object
    printProgress = True,
    ) :
    
    nEvent = tree.GetEntries()
    #print(nEvent)
    
    #tree.Print()
    
    count = 0
    
    splitEvery_count = 0
    
    d_splitEvery_info = {
        "eventIdx": [],
        "objIdx": []
    }
    
    for iEvent in range(0, nEvent) :
        
        eventNumber = iEvent
        
        tree.GetEntry(eventNumber)
        
        a_hist = getattr(tree, varName)
        
        nHist = len(a_hist)
        
        for iHist in range(0, nHist) :
            
            cutStr_eval = cutStr
            
            for iCutVar in range(0, len(l_cutVar)) :
                
                cutVar = l_cutVar[iCutVar]
                
                # Except the indexed variables
                if (cutVar in cutStr_eval and cutStr_eval[cutStr_eval.find(cutVar)+len(cutVar)] != "[") :
                    
                    cutVarVal = getattr(tree, cutVar)[iHist]
                    
                    cutStr_eval = cutStr_eval.replace(cutVar, str(cutVarVal))
            
            # Indexed variables 
            if ("[" in cutStr_eval) :
                
                cutStr_eval = replaceIndexedVar(cutStr_eval, tree)
            
            #print("\ncutStr_eval:", cutStr_eval)
            
            if (eval(cutStr_eval)) :
                
                #print("\ncutStr_eval:", cutStr_eval)
                
                count += 1
                splitEvery_count += 1
                
                if (printProgress) :
                    
                    print("\r# passed selections: %d/%d." %(count, nSel_max), end = "")
            
            # Add the first event
            if (count == 1 and not len(d_splitEvery_info["objIdx"])) :
                
                d_splitEvery_info["eventIdx"].append(iEvent)
                d_splitEvery_info["objIdx"].append(count-1)
            
            if (count == nSel_max) :
                
                break
        
        if (splitEvery_count >= splitEvery) :
            
            d_splitEvery_info["eventIdx"].append(iEvent)
            d_splitEvery_info["objIdx"].append(count-1)
            
            splitEvery_count = 0
        
        if (count == nSel_max) :
            
            break
    
    
    # Add the last event
    d_splitEvery_info["eventIdx"].append(iEvent)
    d_splitEvery_info["objIdx"].append(count)
    
    
    print("")
    
    #return count
    
    d_returnInfo = {
        "count": count,
        "d_splitInfo": d_splitEvery_info,
    }
    
    
    return d_returnInfo


def getArrayFromTBranch(
    tree,
    varName,
    l_cutVar = [],
    cutStr = "1",
    asNumpyArray = True,
    nSel_max = -1,
    ) :
    
    print("Tree: %s" %(tree.GetName()))
    print("Variable: %s" %(varName))
    print("Selection: %s" %(cutStr))
    print("Max #: %d" %(nSel_max))
    
    ##eventList_temp = ROOT.TEventList("eventList_temp", "eventList_temp")
    ##tree.Draw(">> %s" %(eventList_temp.GetName()), cutStr)
    ##
    ##nEventSel = eventList_temp.GetN()
    ##
    ##if (nEvent_max >= 0) :
    ##    
    ##    nEventSel = min(nEvent_max, nEventSel)
    #
    #nEventSel = tree.GetEntries()
    #
    ##varName_mod = varName
    ##varIndex = -1
    ##
    ##
    ##if ("[" in varName) :
    ##    
    ##    varName_mod = varName[0: varName.find("[")]
    ##    
    ##    varIndex = int(varName[varName.find("[")+1: varName.find("]")])
    #
    #
    #l_var = []
    #
    #tree.SetBranchStatus("*", 0)
    #
    #tree.SetBranchStatus(varName, 1)
    #
    #for iCutVar in range(0, len(l_cutVar)) :
    #    
    #    tree.SetBranchStatus(l_cutVar[iCutVar], 1)
    #
    #for iEvent in range(0, nEventSel) :
    #    
    #    #eventNumber = eventList_temp.GetEntry(iEvent)
    #    eventNumber = iEvent
    #    
    #    tree.GetEntry(eventNumber)
    #    
    #    a_var = getattr(tree, varName)
    #    
    #    nObj = len(a_var)
    #    
    #    #print("nObj: %d" %(nObj))
    #    
    #    for iObj in range(0, nObj) :
    #        
    #        cutStr_eval = cutStr
    #        
    #        for iCutVar in range(0, len(l_cutVar)) :
    #            
    #            cutVar = l_cutVar[iCutVar]
    #            
    #            # Except the indexed variables
    #            if (cutVar in cutStr_eval and (
    #                    cutStr_eval[min(len(cutStr_eval)-1, cutStr_eval.find(cutVar)+len(cutVar))] != "["
    #                )
    #            ) :
    #                
    #                cutVarVal = getattr(tree, cutVar)[iObj]
    #                
    #                cutStr_eval = cutStr_eval.replace(cutVar, str(cutVarVal))
    #        
    #        # Indexed variables
    #        if ("[" in cutStr_eval) :
    #            
    #            cutStr_eval = replaceIndexedVar(cutStr_eval, tree)
    #        
    #        if (not eval(cutStr_eval)) :
    #            
    #            continue
    #        
    #        l_var.append(a_var[iObj])
    #        
    #        print("\rIn getArrayFromTBranch(...). Passed selections: %d/%d." %(len(l_var), nSel_max), end = "")
    #        
    #        if (len(l_var) >= nSel_max) :
    #            
    #            break
    #        
    #    
    #    if (len(l_var) >= nSel_max) :
    #        
    #        break
    #
    #
    #print("\n")
    #
    #
    #if (asNumpyArray) :
    #    
    #    a_var = numpy.array(l_var)
    #    
    #    return a_var
    #
    #else :
    #    
    #    return l_var
    
    
    nEvent = tree.GetEntries()
    nObj = int(tree.Draw(varName, cutStr, "goff"))
    print("Read %d objects (after cuts)." %(nObj))
    
    a_var = numpy.zeros(nObj)
    
    l_eventIdx = list(range(0, nEvent, int(2e5)))
    
    if (l_eventIdx[-1] != nEvent) :
        
        l_eventIdx.append(nEvent)
    
    version_main = sys.version_info[0]
    #print(version_main)
    
    obj_idx = 0
    
    # For some strange reason things get messed up with large number of objects (> 1M)
    # Hence split things up
    for iEvent in range(0, len(l_eventIdx)-1) :
        
        idx1 = l_eventIdx[iEvent]
        idx2 = l_eventIdx[iEvent+1]
        
        nObj_temp = int(tree.Draw(varName, cutStr, "goff", idx2-idx1, idx1))
        
        a_var_temp = tree.GetV1()
        a_var_temp.SetSize(nObj_temp)
        
        if (version_main == 2) :
            
            a_var[obj_idx: obj_idx+nObj_temp] = numpy.array(a_var_temp, copy = True)
        
        elif (version_main == 3) :
            
            a_var = numpy.array(tuple(a_var_temp), copy = True)
        
        else :
            
            print("Error in Common.getArrayFromTBranch(...): Invalid python version (%s)." %(".".join(sys.version_info)))
        
        obj_idx += nObj_temp
    
    
    if (nSel_max >= 0 and nSel_max < nObj) :
        
        a_var = a_var[0: nSel_max]
    
    
    if (not asNumpyArray) :
        
        a_var = a_var.tolist()
    
    
    #print(a_var)
    
    print("\n")
    
    return a_var
    
    
    #nObj = int(tree.Draw(varName, cutStr, "goff"))
    #print("Read %d objects (after cuts)." %(nObj))
    #
    #a_var = tree.GetV1()
    ##print(a_var)
    #a_var.SetSize(nObj)
    ##print(a_var)
    #
    #version_main = sys.version_info[0]
    ##print(version_main)
    #
    ##numpy.frombuffer(a_var, count = nObj)
    #
    #if (version_main == 2) :
    #    
    #    a_var = numpy.array(a_var, copy = True)
    #
    #elif (version_main == 3) :
    #    
    #    a_var = numpy.array(tuple(a_var), copy = True)
    #
    #else :
    #    
    #    print("Error in Common.getArrayFromTBranch(...): Invalid python version (%s)." %(".".join(sys.version_info)))
    #
    ##print(len(a_var))
    #
    #if (nSel_max >= 0 and nSel_max < nObj) :
    #    
    #    a_var = a_var[0: nSel_max]
    #
    #
    #if (not asNumpyArray) :
    #    
    #    a_var = a_var.tolist()
    #
    #
    #print(a_var)
    #
    #print("\n")
    #
    #return a_var


def getArrayFromVecTH2(
    tree,
    varName,
    l_cutVar = [],
    l_spectator = [],
    cutStr = "1",
    #asNumpyArray = True,
    #asSparseArray = False,
    nSel_max = -1,
    printProgress = True,
    start = 0, # eventIndex
    end = -1, # eventIndex [including this]
    #fillIntoArray = None,
    fillIndexOffset = 0,
    
    ) :
    
    print("Start of getArrayFromVecTH2(...). Memory usage: %0.4f GB (%0.4f GB)" %(getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0))
    
    #print("\t %s start %d, end %d, nSel_max %d, fillIndexOffset %d" %("@"*10, start, end, nSel_max, fillIndexOffset))
    
    #if (asNumpyArray and asSparseArray) :
    #    
    #    print("Error in Common.getArrayFromVecTH2(...): Only ONE of [\"asNumpyArray\", \"asSparseArray\"] can be True.")
    #    exit(1)
    
    #eventList_temp = ROOT.TEventList("eventList_temp", "eventList_temp")
    #tree.Draw(">> %s" %(eventList_temp.GetName()), cutStr)
    
    #nEventSel = eventList_temp.GetN()
    nEventSel = tree.GetEntries()
    
    #if (nSel_max >= 0) :
    #    
    #    nEventSel = min(nSel_max, nEventSel)
    
    #varName_mod = varName
    #varIndex = -1
    #
    #
    #if ("[" in varName) :
    #    
    #    varName_mod = varName[0: varName.find("[")]
    #    
    #    varIndex = int(varName[varName.find("[")+1: varName.find("]")])
    
    #print("Getting #image in getArrayFromVecTH2(...). Memory usage: %0.4f GB (%0.4f GB)" %(getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0))
    #
    #nSel_max = getNpassedFromTree(
    #    tree = tree,
    #    varName = varName,
    #    l_cutVar = l_cutVar,
    #    cutStr = cutStr,
    #    nSel_max = nSel_max,
    #)
    
    l_var = []
    
    print("Tree: %s" %(tree.GetName()))
    print("Events: %d" %(nEventSel))
    print("TH2: %s" %(varName))
    print("Selection: %s" %(cutStr))
    print("Total images: %d" %(nSel_max))
    
    a_var = numpy.empty(0)
    a_spec = numpy.empty(0)
    
    if (_shared_np_array_image.shape[0]) :
        
        a_var = _shared_np_array_image
    
    if (_shared_np_array_other.shape[0]) :
        
        a_spec = _shared_np_array_other
    
    count = 0
    
    #time.sleep(5)
    #tree.Print()
    
    #pool = multiprocessing.Pool(processes = multiprocessing.cpu_count())
    #print("Loading image with %d threads. \n" %(multiprocessing.cpu_count()))
    
    if (printProgress) :
        
        print("\n")
    
    if (end >= 0) :
        
        nEventSel = end+1
    
    
    # VERY important for memory management
    tree.SetBranchStatus("*", 0)
    tree.SetBranchStatus(varName, 1)
    #tree.GetBranch(varName).SetAutoDelete(True)
    
    for iVar, iVarName in enumerate(l_cutVar+l_spectator) :
        
        tree.SetBranchStatus(iVarName, 1)
        #tree.GetBranch(l_cutVar[iCutVar]).SetAutoDelete(True)
    
    
    #tree.GetEntry(0)
    #a_hist = getattr(tree, varName)
    #l_cutVarVal = [getattr(tree, l_cutVar[iCutVar]) for iCutVar in range(0, len(l_cutVar))]
    
    print("Start of event loop in getArrayFromVecTH2(...). Memory usage: %0.4f GB (%0.4f GB)" %(getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0))
    
    for iEvent in range(start, nEventSel) :
        
        #eventNumber = eventList_temp.GetEntry(iEvent)
        eventNumber = iEvent
        
        #print("Event %d: \n" %(iEvent))
        
        tree.GetEntry(eventNumber)
        
        a_hist = getattr(tree, varName)
        
        nHist = len(a_hist)
        #print("nHist = %d" %(nHist))
        
        for iHist in range(0, nHist) :
            
            cutStr_eval = cutStr
            
            for iCutVar in range(0, len(l_cutVar)) :
                
                cutVar = l_cutVar[iCutVar]
                
                # Except the indexed variables
                if (cutVar in cutStr_eval and cutStr_eval[cutStr_eval.find(cutVar)+len(cutVar)] != "[") :
                    
                    cutVarVal = getattr(tree, cutVar)[iHist]
                    #cutVarVal = l_cutVarVal[iCutVar][iHist]
                    
                    cutStr_eval = cutStr_eval.replace(cutVar, str(cutVarVal))
            
            # Indexed variables
            if ("[" in cutStr_eval) :
                
                cutStr_eval = replaceIndexedVar(cutStr_eval, tree)
            
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
            
            nBinX = hist.GetNbinsX()
            nBinY = hist.GetNbinsY()
            
            #print("\t", hist.GetName(), hist.Integral(), nBinY, nBinX)
            
            #arr = 0
            
            #if (asSparseArray) :
            #    
            #    arr = scipy.sparse.csr_matrix((nBinY, nBinX))
            #
            #else :
            #    
            #arr = numpy.zeros((nBinY, nBinX), dtype = "float32")
            
            if (not a_var.shape[0]) :
                
                a_var = numpy.zeros((nSel_max, nBinY, nBinX), dtype = "float32")
            
            
            a_data_hist = numpy.array(hist)
            a_data_hist.shape = (nBinY+2, nBinX+2)
            
            a_var[count+fillIndexOffset, :, :] = a_data_hist[1: -1, 1: -1]
            
            for iSpec, specName in enumerate(l_spectator) :
                
                #print(specName, getattr(tree, specName))
                a_spec[count+fillIndexOffset, iSpec] = getattr(tree, specName)[iHist]
            
            
            ##for iBinX in numba.prange(0, nBinX) :
            #for iBinX in range(0, nBinX) :
            #    
            #    for iBinY in range(0, nBinY) :
            #        
            #        binContent = hist.GetBinContent(iBinX+1, iBinY+1)
            #        
            #        #if (binContent) :
            #        #    
            #        #    #print("\t", iBinX, iBinY, binContent)
            #        #    arr[iBinY, iBinX] = binContent
            #        
            #        a_var[count+fillIndexOffset, iBinY, iBinX] = binContent
            
            count += 1
            
            #print("\t", a_var.sum(), a_var.mean())
            
            #l_var.append(arr)
            
            #if (not (len(l_var) % 10000)) :
            
            if (printProgress) :
                
                print("\rLoaded %d/%d image(s). Memory usage: %0.4f GB (%0.4f GB)." %(count, nSel_max, getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0), end = "")
            
            #print("Loaded %d/%d image(s). Memory usage: (%0.4f GB)." %(count, nSel_max, getMemoryMB()/1024.0)
            
            #hist.Delete()
            #gc.collect()
            
            if (count >= nSel_max) :
                
                break
        
        #a_hist = None
        
        if (not ((iEvent+1)%1000)) :
            
            gc.collect()
        
        if (count >= nSel_max) :
            
            break
    
    gc.collect()
    
    #print("$"*50, numpy.mean(a_var), numpy.mean(_shared_np_array_image))
    
    print("")
    
    #print("End of getArrayFromVecTH2(...). Size of l_var: %0.4f GB" %(float(sys.getsizeof(l_var)) / 1024.0**3))
    #print("End of getArrayFromVecTH2(...). Size of l_var: %d" %(sys.getsizeof(l_var)))
    
    print("End of getArrayFromVecTH2(...). Memory usage: %0.4f GB (%0.4f GB)" %(getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0))
    
    #return numpy.array(l_var, dtype = "float32")
    
    #print(a_spec)
    
    if (_shared_np_array_image.shape[0]) :
        
        return 0
    
    return a_var[0: count]
    
    #if (asNumpyArray) :
    #    
    #    return numpy.array(l_var, dtype = "float32")
    #
    #else :
    #    
    #    return l_var


def getHistShape(tree, branchName) :
    
    nBinX = 0
    nBinY = 0
    
    for iEntry in range(0, tree.GetEntries()) :
        
        tree.GetEntry(iEntry)
        
        a_hist = getattr(tree, branchName)
        
        if (len(a_hist)) :
            
            nBinX = a_hist[0].GetNbinsX()
            nBinY = a_hist[0].GetNbinsY()
            
            break
    
    return (nBinY, nBinX)


def init_pool(
    shared_array_image,
    shared_array_image_shape,
    shared_array_other = None,
    shared_array_other_shape = None,
    ) :
    
    global _shared_np_array_image
    global _shared_np_array_other
    
    _shared_np_array_image = numpy.frombuffer(shared_array_image.get_obj(), dtype = "float32")#.reshape(shared_array_image_shape)
    _shared_np_array_image.shape = shared_array_image_shape
    
    if (
        shared_array_other is not None and
        shared_array_other_shape is not None
        ) :
        
        _shared_np_array_other = numpy.frombuffer(shared_array_other.get_obj(), dtype = "float32")#.reshape(shared_array_other_shape)
        _shared_np_array_other.shape = shared_array_other_shape


def getActiveJobNum(l_job) :
    
    nActive = 0
    
    for iJob in range(0, len(l_job)) :
        
        if (type(l_job[iJob]) == type([])) :
            
            nActive += getActiveJobNum(l_job[iJob])
        
        else :
            
            nActive += int(not l_job[iJob].ready())
    
    return nActive


def waitForJobs(l_job, maxJobN) :
    
    while (1) :
        
        time.sleep(1)
        
        nActiveJobs = getActiveJobNum(l_job)
        
        if (nActiveJobs < maxJobN) :
            
            return
        
        print("\r# active jobs: %d. Waiting..." %(nActiveJobs), end = "")


def getVarInfoFromTree(
    l_varStr,
    tree_sig,
    tree_bkg,
    l_cutVar,
    cutStr_sig,
    cutStr_bkg,
    nEventTotal_sig,
    nEventTotal_bkg,
    l_spectator = [],
    splitEvery = -1,
    nCPUfraction = 0.8,
    includeBkg = True,
    ) :
    
    
    nVar = len(l_varStr)
    
    d_varInfo = {}
    
    
    # Some variable info formatting
    for iVar in range(0, nVar) :
        
        varInfo_temp = TrainingVarInfo()
        
        varStr = l_varStr[iVar]
        varName = varStr
        
        varInfo_temp.varStr = varStr
        varInfo_temp.varName = varName
        
        d_varInfo[varStr] = varInfo_temp
    
    
    pool = multiprocessing.Pool(processes = 2)
    
    print("\n")
    print("Getting #image (sig) in getVarInfoFromTree(...). Memory usage: %0.4f GB (%0.4f GB)" %(getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0))
    
    d_passInfo_sig = pool.apply_async(
        getNpassedFromTree,
        (),
        dict(
            tree = tree_sig,
            varName = d_varInfo[l_varStr[0]].varName,
            l_cutVar = l_cutVar,
            cutStr = cutStr_sig,
            nSel_max = nEventTotal_sig,
            splitEvery = splitEvery,
            printProgress = False,
        ),
        #callback = collect_result,
    )#.get()
    
    
    if (includeBkg) :
        
        print("\n")
        print("Getting #image (bkg) in getVarInfoFromTree(...). Memory usage: %0.4f GB (%0.4f GB)" %(getMemoryMB()/1024.0, getMaxMemoryMB()/1024.0))
        
        d_passInfo_bkg = pool.apply_async(
            getNpassedFromTree,
            (),
            dict(
                tree = tree_bkg,
                varName = d_varInfo[l_varStr[0]].varName,
                l_cutVar = l_cutVar,
                cutStr = cutStr_bkg,
                nSel_max = nEventTotal_bkg,
                splitEvery = splitEvery,
                printProgress = True,
            ),
            #callback = collect_result,
        )#.get()
    
    
    # Wait for all the processes to complete
    pool.close()
    pool.join()
    
    
    d_passInfo_sig = d_passInfo_sig.get()
    
    if (includeBkg) :
        
        d_passInfo_bkg = d_passInfo_bkg.get()
    
    
    print("\n")
    
    nEventTotal_sig = d_passInfo_sig["count"]
    d_splitInfo_sig = d_passInfo_sig["d_splitInfo"]
    #pprint.pprint(d_splitInfo_sig)
    
    print("Total #image (sig): %d \n" %(nEventTotal_sig))
    
    nJob_sig = len(d_splitInfo_sig["eventIdx"])-1
    #print(d_splitInfo_sig)
    #print("nJob_sig", nJob_sig)
    
    d_pool_sig = {
        "pools": [],
        "jobs": [],
    }
    
    
    if (includeBkg) :
        
        nEventTotal_bkg = d_passInfo_bkg["count"]
        d_splitInfo_bkg = d_passInfo_bkg["d_splitInfo"]
        #pprint.pprint(d_splitInfo_bkg)
        
        print("Total #image (bkg): %d \n" %(nEventTotal_bkg))
        
        nJob_bkg = len(d_splitInfo_bkg["eventIdx"])-1
        #print(d_splitInfo_bkg)
        #print("nJob_bkg", nJob_bkg)
        
        d_pool_bkg = {
            "pools": [],
            "jobs": [],
        }
    
    
    # Get the histogram shape
    histShape = getHistShape(tree_sig, d_varInfo[l_varStr[0]].varName)
    nBinX = histShape[0]
    nBinY = histShape[1]
    
    
    for iVar in range(0, nVar) :
        
        #l_pool_sig.append([])
        #l_pool_bkg.append([])
        
        varStr = l_varStr[iVar]
        
        varInfo = d_varInfo[varStr]
        
        
        print("\n\n%s Loading image: %s %s \n" %("*"*10, varInfo.varName, "*"*10))
        
        
        varInfo.a_sig = multiprocessing.Array(typecode_or_type = "f", size_or_initializer = nEventTotal_sig*nBinX*nBinY)
        
        # Store the spectators only for the 1st variable
        if (len(l_spectator) and not iVar) :
            
            varInfo.a_spec_sig = multiprocessing.Array(typecode_or_type = "f", size_or_initializer = nEventTotal_sig*len(l_spectator))
        
        pool = multiprocessing.Pool(
            processes = nJob_sig,
            initializer = init_pool,
            initargs = (
                varInfo.a_sig,
                (nEventTotal_sig, nBinY, nBinX),
                varInfo.a_spec_sig,
                (nEventTotal_sig, len(l_spectator))
            ),
            maxtasksperchild = 1
        )
        
        d_pool_sig["pools"].append(pool)
        d_pool_sig["jobs"].append([])
        
        for iJob in range(0, nJob_sig) :
            
            start = d_splitInfo_sig["eventIdx"][iJob]
            end = d_splitInfo_sig["eventIdx"][iJob+1] - 1
            offset = d_splitInfo_sig["objIdx"][iJob]
            nSel_max = d_splitInfo_sig["objIdx"][iJob+1] - d_splitInfo_sig["objIdx"][iJob]
            
            d_pool_sig["jobs"][iVar].append(pool.apply_async(
                getArrayFromVecTH2,
                (),
                dict(
                    tree = tree_sig,
                    varName = varInfo.varName,
                    l_cutVar = l_cutVar,
                    cutStr = cutStr_sig,
                    l_spectator = l_spectator * (not iVar),
                    nSel_max = nSel_max,
                    printProgress = (iJob == nJob_sig-1),
                    start = start, # eventIndex
                    end = -1, # eventIndex [including this]
                    fillIndexOffset = offset,
                ),
                #callback = collect_result,
            ))#.get())
            
            waitForJobs(d_pool_sig["jobs"]+d_pool_bkg["jobs"], int(nCPUfraction * multiprocessing.cpu_count()))
        
        pool.close()
        
        
        # Load background variables
        if (includeBkg) :
            
            varInfo.a_bkg = multiprocessing.Array(typecode_or_type = "f", size_or_initializer = nEventTotal_bkg*nBinX*nBinY)
            
            # Store the spectators only for the 1st variable
            if (len(l_spectator) and not iVar) :
                
                varInfo.a_spec_bkg = multiprocessing.Array(typecode_or_type = "f", size_or_initializer = nEventTotal_bkg*len(l_spectator))
            
            pool = multiprocessing.Pool(
                processes = nJob_bkg,
                initializer = init_pool,
                initargs = (
                    varInfo.a_bkg,
                    (nEventTotal_bkg, nBinY, nBinX),
                    varInfo.a_spec_bkg,
                    (nEventTotal_bkg, len(l_spectator))
                ),
                maxtasksperchild = 1
            )
            
            d_pool_bkg["pools"].append(pool)
            d_pool_bkg["jobs"].append([])
            
            for iJob in range(0, nJob_bkg) :
                
                start = d_splitInfo_bkg["eventIdx"][iJob]
                end = d_splitInfo_bkg["eventIdx"][iJob+1] - 1
                offset = d_splitInfo_bkg["objIdx"][iJob]
                nSel_max = d_splitInfo_bkg["objIdx"][iJob+1] - d_splitInfo_bkg["objIdx"][iJob]
                
                d_pool_bkg["jobs"][iVar].append(pool.apply_async(
                    getArrayFromVecTH2,
                    (),
                    dict(
                        tree = tree_bkg,
                        varName = varInfo.varName,
                        l_cutVar = l_cutVar,
                        cutStr = cutStr_bkg,
                        l_spectator = l_spectator * (not iVar),
                        nSel_max = nSel_max,
                        printProgress = (iJob == nJob_bkg-1),
                        start = start, # eventIndex
                        end = -1, # eventIndex [including this]
                        fillIndexOffset = offset,
                    ),
                    #callback = collect_result,
                ))#.get())
                
                waitForJobs(d_pool_sig["jobs"]+d_pool_bkg["jobs"], int(nCPUfraction * multiprocessing.cpu_count()))
            
            pool.close()
    
    
    # Wait for all the processes to complete
    for iPool, pool in enumerate(d_pool_sig["pools"]) :
        
        #pool.close()
        pool.join()
        gc.collect()
        
        # Get the results
        for iJobList, l_job in enumerate(d_pool_sig["jobs"]) :
            
            for iJob, job in enumerate(l_job) :
                
                job.get()
    
    if (includeBkg) :
        
        for iPool, pool in enumerate(d_pool_bkg["pools"]) :
            
            #pool.close()
            pool.join()
            gc.collect()
            
            # Get the results
            for iJobList, l_job in enumerate(d_pool_bkg["jobs"]) :
                
                for iJob, job in enumerate(l_job) :
                    
                    job.get()
    
    
    # Store the results
    for iVar in range(0, nVar) :
        
        varStr = l_varStr[iVar]
        
        varInfo = d_varInfo[varStr]
        
        varInfo.a_sig = numpy.frombuffer(varInfo.a_sig.get_obj(), dtype = "float32")
        varInfo.a_sig.shape = (nEventTotal_sig, nBinY, nBinX)
        
        # Store the spectators with the 1st variable
        if (len(l_spectator) and not iVar) :
            
            varInfo.a_spec_sig = numpy.frombuffer(varInfo.a_spec_sig.get_obj(), dtype = "float32")
            varInfo.a_spec_sig.shape = (nEventTotal_sig, len(l_spectator))
        
        if (includeBkg) :
            
            varInfo.a_bkg = numpy.frombuffer(varInfo.a_bkg.get_obj(), dtype = "float32")
            varInfo.a_bkg.shape = (nEventTotal_bkg, nBinY, nBinX)
            
            # Store the spectators with the 1st variable
            if (len(l_spectator) and not iVar) :
                
                varInfo.a_spec_bkg = numpy.frombuffer(varInfo.a_spec_bkg.get_obj(), dtype = "float32")
                varInfo.a_spec_bkg.shape = (nEventTotal_bkg, len(l_spectator))
    
    print("\n")
    
    return d_varInfo


#def evaluateTMVAandGetDiscr(
#    methodName,
#    weightFileName,
#    tree,
#    l_variable,
#    l_spectator = [],
#    l_cutVariable = [],
#    l_returnVariable = [],
#    treeCutStr= "1",
#    cutStr = "1",
#    nEventSel_max = -1,
#    ) :
#    
#    eventList = ROOT.TEventList("eventList", "eventList")
#    tree.Draw(">> %s" %(eventList.GetName()), treeCutStr)
#    
#    tree_nEvent = eventList.GetN()
#    
#    d_varData = {}
#    d_specData = {}
#    
#    d_retVarData = {}
#    
#    tmvaReader = ROOT.TMVA.Reader("!Silent")
#    
#    
#    for iVar, varName in enumerate(l_variable) :
#        
#        d_varData[varName] = array.array("f", [0])
#        
#        tmvaReader.AddVariable(varName, d_varData[varName])
#    
#    
#    for iSpec, specName in enumerate(l_spectator) :
#        
#        d_specData[specName] = array.array("f", [0])
#        
#        tmvaReader.AddSpectator(specName, d_specData[specName])
#    
#    
#    for iRetVar, retVarName in enumerate(l_returnVariable) :
#        
#        d_retVarData[retVarName] = []
#    
#    
#    tmvaReader.BookMVA(methodName, weightFileName)
#    
#    nSelected = 0
#    
#    l_discrVal = []
#    
#    print("Evaluating %s discriminator using: %s" %(methodName, weightFileName))
#    
#    for iEvent in range(0, tree_nEvent) :
#        
#        eventNumber = eventList.GetEntry(iEvent)
#        
#        tree.GetEntry(eventNumber)
#        
#        nHepTop = getattr(tree, l_variable[0]).size()
#        
#        for iHepTop in range(0, nHepTop) :
#            
#            cutStr_eval = cutStr
#            
#            
#            for iVar, varName in enumerate(l_variable) :
#                
#                varVal = getattr(tree, varName)[iHepTop]
#                
#                d_varData[varName][0] = varVal
#                
#                cutStr_eval = cutStr_eval.replace(varName, str(varVal))
#            
#            
#            for iVar, varName in enumerate(l_cutVariable) :
#                
#                varVal = getattr(tree, varName)[iHepTop]
#                
#                cutStr_eval = cutStr_eval.replace(varName, str(varVal))
#            
#            
#            if (not eval(cutStr_eval)) :
#                
#                continue
#            
#            
#            for iVar, varName in enumerate(l_returnVariable) :
#                
#                varVal = getattr(tree, varName)[iHepTop]
#                
#                d_retVarData[varName].append(varVal)
#            
#            
#            discrVal = tmvaReader.EvaluateMVA(methodName)
#            
#            l_discrVal.append(discrVal)
#            
#            nSelected += 1
#            
#            print("\r[%d/%d] Evaluated %d/%d." %(iEvent+1, tree_nEvent, nSelected, nEventSel_max), end = "")
#            
#            if (nEventSel_max > 0 and nSelected == nEventSel_max) :
#                
#                break
#        
#        if (nEventSel_max > 0 and nSelected == nEventSel_max) :
#            
#            break
#    
#    #matplotlib.pyplot.hist(l_discrVal, bins = 100, range = (-1, 1))
#    #matplotlib.pyplot.show()
#    
#    #print nSelected
#    
#    #d_result = {}
#    #
#    #d_result["nSelected"] = nSelected
#    #d_result["l_discrVal"] = l_discrVal
#    #
#    #return d_result
#    
#    #return l_discrVal
#    
#    d_result = d_retVarData
#    
#    d_result["l_discrVal"] = l_discrVal
#    
#    print("\n")
#    
#    return d_result


def evaluateTMVAandGetDiscr(
    xmlFileName,
    tree,
    cutStr = "1",
    nSel_max = -1,
    ) :
    
    # import here; otherwise argparse options are not displayed for some reason
    import root_numpy
    import root_numpy.tmva
    
    d_xmlInfo = xmltodict.parse(xml.etree.ElementTree.tostring(xml.etree.ElementTree.parse(xmlFileName).getroot()))
    
    methodName = d_xmlInfo["MethodSetup"]["@Method"]
    methodName = methodName.split("::")[-1]
    
    l_varName = d_xmlInfo["MethodSetup"]["Variables"]["Variable"]
    l_varName = [ele["@Expression"] for ele in l_varName]
    #print(l_varName)
    
    l_specName = d_xmlInfo["MethodSetup"]["Spectators"]
    
    if ("Spectator" not in l_specName) :
        
        l_specName = []
    
    else :
    
        l_specName = l_spec["Spectator"]
        l_specName = [ele["@Expression"] for ele in l_specName]
    
    
    tmvaReader = ROOT.TMVA.Reader("!Silent")
    
    
    a_trainVar = None
    
    for iVar, varName in enumerate(l_varName) :
        
        tmvaReader.AddVariable(varName, array.array("f", [0]))
        
        a_temp =  getArrayFromTBranch(
            tree = tree,
            varName = varName,
            cutStr = cutStr,
            nSel_max = nSel_max,
        )
        
        if (a_trainVar is None) :
            
            a_trainVar = numpy.zeros((len(a_temp), len(l_varName)))
        
        a_trainVar[:, iVar] = a_temp
    
    
    for iSpec, specName in enumerate(l_specName) :
        
        tmvaReader.AddSpectator(specName, array.array("f", [0]))
    
    
    tmvaReader.BookMVA(methodName, xmlFileName)
    
    print("Evaluating %s discriminator using: %s" %(methodName, xmlFileName))
    
    a_discrVal = root_numpy.tmva.evaluate_reader(
        reader = tmvaReader,
        name = methodName,
        events = a_trainVar,
    )
    
    #print(a_discrVal)
    
    return a_discrVal


def getMemoryMB(process = -1) :
    
    if (process < 0) :
        
        process = psutil.Process(os.getpid())
    
    mem = process.memory_info().rss / 1024.0**2
    
    return mem


def getMaxMemoryMB() :
    
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    
    return mem


def clearArray(arr) :
    
    while (len(arr)) :
        
        arr.pop()


def TGraphToTH1(graph, setError = True) :
    
    hist = graph.GetHistogram().Clone()
    hist.SetDirectory(0)
    
    nPoint = graph.GetN()
    
    for iPoint in range(0, nPoint) :
        
        pointValX = ROOT.Double(0)
        pointValY = ROOT.Double(0)
        
        graph.GetPoint(iPoint, pointValX, pointValY)
        
        #print(iPoint, pointValX, pointValY)
        
        pointErrX = graph.GetErrorX(iPoint)
        pointErrY = graph.GetErrorY(iPoint)
        
        binNum = hist.FindBin(pointValX)
        
        hist.SetBinContent(binNum, pointValY)
        
        if (setError) :
            
            hist.SetBinError(binNum, pointErrY)
    
    return hist


def getNDC(pad, pos, axis = "X") :
    
    pad.Update();
    
    if (axis == "X") :
        
        if (pad.GetLogx()) :
            
            pos = numpy.log10(pos)
        
        #print("X", pos, pad.GetX1(), pad.GetX2())
        pos_NDC = (pos - pad.GetX1()) / (pad.GetX2()-pad.GetX1())
    
    elif (axis == "Y") :
        
        y1 = pad.GetY1()
        y2 = pad.GetY2()
        
        if (pad.GetLogy()) :
            
            #y1 = 10.0**pad.GetUymin()
            #y2 = 10.0**pad.GetUymax()
            
            pos = numpy.log10(pos)
        
        #print("Y", pos, pad.GetY1(), pad.GetY2())
        #print("Y", pos, y1, y2)
        pos_NDC = (pos - y1) / (y2-y1)
    
    else :
        
        print("Error in Common.getNDC(...): Invalid axis option.")
        exit(1)
    
    return pos_NDC


def plot1D(
    list_histDetails,
    stackDrawOption = "nostack",
    title = "",
    titleSizeScale = 1,
    xTitle = "", yTitle = "",
    xMin = initVal, xMax = initVal,
    yMin = initVal, yMax = initVal,
    logX = False, logY = False,
    gridX = False, gridY = False,
    moreLogGridsX = True,
    moreLogGridsY = True,
    nDivisionsX = [0, 0, 0],
    nDivisionsY = [0, 0, 0],
    xTitleSizeScale = 1.0,
    yTitleSizeScale = 1.0,
    xTitleOffsetScale = 1.0,
    yTitleOffsetScale = 1.0,
    xLabelSizeScale = 1.0,
    yLabelSizeScale = 1.0,
    centerLabelsX = False,
    centerLabelsY = False,
    axisLabelMaxDigits = 3,
    drawLegend = True,
    legendDrawOption = "",
    legendNcol = 1,
    legendWidthScale = 1,
    legendHeightScale = 1,
    transparentLegend = False,
    legendTextSize = -1,
    legendBorderSize = 0,
    legendPos = "UR",
    legendTitle = "",
    l_extraText = [], #[[x, y, text], ...]
    sampleText = "",
    fixAlphanumericBinLabels = False,
    outFileName = "outFile",
    outFileName_suffix = "",
    ) :
    
    tdrstyle.setTDRStyle()
    
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptFit(0)
    
    ROOT.gStyle.SetGridColor(15)
    
    ROOT.TGaxis.SetMaxDigits(axisLabelMaxDigits)
    ROOT.TGaxis.SetExponentOffset(0.0, -0.004, "y")
    
    canvas = ROOT.TCanvas("canvas", "canvas")
    
    #canvas.SetPadTopMargin(0.05)
    #canvas.SetBottomMargin(0.13)
    #canvas.SetLeftMargin(0.16)
    canvas.SetRightMargin(0.05)
    
    if (len(title)) :
        
        canvas.SetTopMargin(0.1)
    
    legend = 0
    
    legendHeight = legendHeightScale * 0.05 * len(list_histDetails)
    legendWidth = legendWidthScale * 0.65
    
    padTop = 1 - canvas.GetTopMargin() - 0.6*ROOT.gStyle.GetTickLength("y")
    padRight = 1 - canvas.GetRightMargin() - 0.6*ROOT.gStyle.GetTickLength("x")
    padBottom = canvas.GetBottomMargin() + 0.6*ROOT.gStyle.GetTickLength("y")
    padLeft = canvas.GetLeftMargin() + 0.6*ROOT.gStyle.GetTickLength("x")
    
    if(legendPos == "UR") :
        
        legend = ROOT.TLegend(padRight-legendWidth, padTop-legendHeight, padRight, padTop)
    
    elif(legendPos == "LR") :
        
        legend = ROOT.TLegend(padRight-legendWidth, padBottom, padRight, padBottom+legendHeight)
    
    elif(legendPos == "LL") :
        
        legend = ROOT.TLegend(padLeft, padBottom, padLeft+legendWidth, padBottom+legendHeight)
    
    elif(legendPos == "UL") :
        
        legend = ROOT.TLegend(padLeft, padTop-legendHeight, padLeft+legendWidth, padTop)
    
    else :
        
        print("Wrong legend position option:", legendPos)
        exit(1)
    
    legend.SetNColumns(legendNcol)
    
    if (legendTextSize > 0) :
        
        legend.SetTextSize(legendTextSize)
    
    if (transparentLegend) :
        
        legend.SetFillStyle(0)
    
    if (legendBorderSize >= 0) :
        
        legend.SetBorderSize(legendBorderSize)
    
    
    ROOT.SetOwnership(legend, 0)
    
    if (len(legendTitle)) :
        
        legend.SetHeader(legendTitle)
        legendHeader = legend.GetListOfPrimitives().First()
        legendHeader.SetTextAlign(23)
        
        # For whatever reason, SetHeader("Header", "C") does not accept the second argument in python
        # So, center the header this way
        # EVEN THIS DOESN'T WORK! Gives a seg-fault when calling the plot1D(...) function for the second time
        #legend.GetListOfPrimitives().First().SetTextAlign(22)
    
    #legend.SetLegendBorderMode(0)
    
    stack = ROOT.THStack()
    
    if (fixAlphanumericBinLabels) :
        
        h1_temp = TH1F("temp", "temp", list_histDetails[0].hist.GetXaxis().GetNbins(), list_histDetails[0].hist.GetXaxis().GetXmin(), list_histDetails[0].hist.GetXaxis().GetXmax())
        stack.Add(h1_temp)
    
    for iHist in range(0, len(list_histDetails)) :
        
        list_histDetails[iHist].hist.SetLineColor(list_histDetails[iHist].lineColor)
        list_histDetails[iHist].hist.SetLineStyle(list_histDetails[iHist].lineStyle)
        list_histDetails[iHist].hist.SetLineWidth(list_histDetails[iHist].lineWidth)
        
        list_histDetails[iHist].hist.SetMarkerStyle(list_histDetails[iHist].markerStyle)
        list_histDetails[iHist].hist.SetMarkerColor(list_histDetails[iHist].markerColor)
        
        if (list_histDetails[iHist].fillStyle >= 0) :
            
            list_histDetails[iHist].hist.SetFillStyle(list_histDetails[iHist].fillStyle)
        
        if (list_histDetails[iHist].markerSize >= 0) :
            
            list_histDetails[iHist].hist.SetMarkerSize(list_histDetails[iHist].markerSize)
        
        if (list_histDetails[iHist].drawOption == "hist") :
            
            list_histDetails[iHist].hist.SetMarkerSize(0)
        
        stack.Add(list_histDetails[iHist].hist, list_histDetails[iHist].drawOption)
        
        if (list_histDetails[iHist].addToLegend) :
            
            if (len(legendDrawOption)) :
                
                legend.AddEntry(list_histDetails[iHist].hist, list_histDetails[iHist].histLabel, legendDrawOption)
            
            else :
                
                legend.AddEntry(list_histDetails[iHist].hist, list_histDetails[iHist].histLabel)
        
    
    
    # Add a dummy histogram so that the X-axis range can be beyond the histogram range
    h1_xRange = ROOT.TH1F("h1_xRange", "h1_xRange", 1, xMin, xMax)
    stack.Add(h1_xRange)
    
    stack.Draw(stackDrawOption)
    
    # Draw the associated (fit) functions
    for iHist in range(0, len(list_histDetails)) :
        
        if (list_histDetails[iHist].drawFunctions) :
            
            funcList = list_histDetails[iHist].hist.GetListOfFunctions()
            
            if (not funcList.GetSize()) :
                
                continue
            
            for iFunc in range(0, funcList.GetEntries()) :
                
                f1_temp = funcList.At(iFunc)
                
                # For some reason the list also contains the stat box at times
                if (type(f1_temp) is ROOT.TF1) :
                    
                    f1_temp.GetHistogram().SetStats(0)
                    f1_temp.Draw("L same")
    
    if (drawLegend) :
        
        legend.Draw()
    
    if (fixAlphanumericBinLabels) :
        
        for iBin in range(0, stack.GetXaxis().GetNbins()) :
            
            stack.GetXaxis().SetBinLabel(iBin, list_histDetails[0].hist.GetXaxis().GetBinLabel(iBin))
        
        #stack.GetXaxis().SetLabelSize(0.025)
        stack.GetXaxis().LabelsOption("v")
    
    stack.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("X") * xLabelSizeScale)
    stack.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Y") * yLabelSizeScale)
    
    stack.GetXaxis().SetTitle(xTitle)
    stack.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * xTitleSizeScale)
    
    #if (xTitleOffset != 1) :
    #    
    #    stack.GetXaxis().SetTitleOffset(xTitleOffset)
    
    stack.GetXaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("X") * xTitleOffsetScale)
    
    stack.GetYaxis().SetTitle(yTitle)
    stack.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * yTitleSizeScale)
    #stack.GetYaxis().SetTitleOffset(1 + 3*(1-yTitleSizeScale))
    
    #if (yTitleOffset != 1) :
    #    
    #    stack.GetYaxis().SetTitleOffset(yTitleOffset)
    
    stack.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("Y") * yTitleOffsetScale)
    
    #print(ROOT.gStyle.GetTitleOffset("X") * xTitleOffsetScale)
    #print(ROOT.gStyle.GetTitleOffset("Y") * yTitleOffsetScale)
    
    stack.SetTitle(title)
    
    # X range
    if (xMin != initVal and xMax != initVal) :
        
        stack.GetXaxis().SetRangeUser(
            xMin,
            xMax
        )
    
    elif (xMin != initVal) :
        
        stack.GetXaxis().SetRangeUser(
            xMin,
            stack.GetXaxis().GetXmax()
        )
    
    elif (xMax != initVal) :
        
        stack.GetXaxis().SetRangeUser(
            stack.GetXaxis().GetXmin(),
            xMax
        )
    
    # Y range
    if (yMin != initVal) :
        
        stack.SetMinimum(yMin)
    
    if (yMax != initVal) :
        
        stack.SetMaximum(yMax)
    
    stack.GetXaxis().CenterTitle(True)
    stack.GetYaxis().CenterTitle(True)
    
    #if (gridX) :
    #    
    #    stack.GetXaxis().SetAxisColor(15)
    #
    #if (gridY) :
    #    
    #    stack.GetYaxis().SetAxisColor(15)
    
    #ROOT.TGaxis.SetMaxDigits(3)
    #stack.GetXaxis().SetMaxDigits(3)
    
    # Axis divisions
    if (abs(sum(nDivisionsX)) > 0) :
        
        stack.GetXaxis().SetNdivisions(nDivisionsX[0], nDivisionsX[1], nDivisionsX[2], False)
        
    else :
        
        stack.GetXaxis().SetNdivisions(5, 5, 0)
    
    if (abs(sum(nDivisionsY)) > 0) :
        
        stack.GetYaxis().SetNdivisions(nDivisionsY[0], nDivisionsY[1], nDivisionsY[2], False)
    
    else :
        
        stack.GetYaxis().SetNdivisions(5, 5, 0)
    
    # Bin label position
    if (centerLabelsX) :
        
        stack.GetXaxis().CenterLabels()
    
    if (centerLabelsY) :
        
        stack.GetYaxis().CenterLabels()
    
    
    canvas.SetLogx(logX)
    canvas.SetLogy(logY)
    
    canvas.SetGridx(gridX)
    canvas.SetGridy(gridY)
    
    # Log axis grid
    if (logX and not moreLogGridsX) :
        
        stack.GetXaxis().SetNdivisions(10)
    
    if (logY and not moreLogGridsY) :
        
        stack.GetYaxis().SetNdivisions(10)
    
    
    if (len(title)) :
        
        #tpavetext_title = ROOT.TPaveText(0.0, 0.91, 1.0, 0.995, "NDC")
        tpavetext_title = ROOT.TPaveText(padLeft, 0.91, padRight, 0.995, "NDC")
        tpavetext_title.AddText(title)
        
        tpavetext_title.SetMargin(0)
        tpavetext_title.SetFillStyle(0)
        tpavetext_title.SetBorderSize(0)
        tpavetext_title.SetTextFont(ROOT.gStyle.GetTitleFont())
        tpavetext_title.SetTextColor(1)
        tpavetext_title.SetTextAlign(21)
        tpavetext_title.SetTextSize(0.045 * titleSizeScale)
        
        tpavetext_title.Draw()
    
    
    l_textBox = []
    
    # Extra text
    for iText in range(0, len(l_extraText)) :
        
        textX = l_extraText[iText][0]
        textY = l_extraText[iText][1]
        text = l_extraText[iText][2]
        
        if (len(text)) :
            
            latex = ROOT.TLatex(textX, textY, text)
            #latex.SetTextFont(62);
            latex.SetTextSize(0.03);
            latex.SetTextAlign(13);
            
            #latex.Draw()
            
            textXsize = latex.GetXsize()
            textYsize = latex.GetYsize()
            textBoxMargin = 0
            #textBoxMargin = 0.1 * min(textXsize, textYsize)
            #print(textXsize, textYsize, textBoxMargin, latex.GetX(), latex.GetY())
            
            boxX1_NDC = getNDC(canvas, textX, axis = "X")
            boxY1_NDC = getNDC(canvas, textY, axis = "Y")
            
            #print(getNDC(canvas, 0.1, axis = "Y"), getNDC(canvas, 0.01, axis = "Y"), getNDC(canvas, 0.001, axis = "Y"))
            #print(textX, textY)
            #print(textX_NDC, textY_NDC, textX_NDC+textXsize+2*textBoxMargin, textY_NDC+textYsize+2*textBoxMargin)
            
            boxX2_NDC = min(1-canvas.GetRightMargin(), boxX1_NDC+textXsize+2*textBoxMargin)
            #boxY2_NDC = min(1-canvas.GetTopMargin(), textY_NDC+textYsize+2*textBoxMargin)
            
            boxXsize = boxX2_NDC - boxX1_NDC
            #boxYsize = boxY2_NDC - boxY1_NDC
            boxYsize = textYsize * (boxXsize / textXsize)
            
            boxY2_NDC = boxY1_NDC + boxYsize
            
            textBox = ROOT.TPaveText(
                boxX1_NDC,
                boxY1_NDC,
                boxX2_NDC,
                boxY2_NDC,
                "NDC"
            )
            
            l_textBox.append(textBox)
            
            textBox.AddText(text)
            
            textBox.SetMargin(0)
            textBox.SetFillStyle(0)
            #textBox.SetFillStyle(1001)
            textBox.SetBorderSize(0)
            textBox.SetTextFont(62)
            textBox.SetTextColor(1)
            textBox.SetTextAlign(12)
            textBox.SetTextSize(min(0.03, textBox.GetTextSize()))
            #textBox.SetFillColorAlpha(ROOT.kWhite, 0.6)
            
            textBox.Draw()
    
    canvas.Update()
    
    outFileName = outFileName + ("_"*(outFileName_suffix != "")) + outFileName_suffix + ".pdf"
    print("Output:", outFileName)
    
    canvas.SaveAs(outFileName)
    canvas.SaveAs(outFileName.replace(".pdf", ".png"))
    
    print("\n")


def plot2D(
    histDetails,
    l_extraText = [], #[[x, y, text], ...]
    palette = None,
    nContour = -1,
    axisLabelMaxDigits = 4,
    ) :
    
    #gStyle_mod =  ROOT.gStyle.Clone()
    #gStyle_mod.cd()
    #ROOT.gROOT.ForceStyle()
    
    #ROOT.gStyle.Reset("Plain")
    #ROOT.gStyle.cd()
    
    tdrstyle.setTDRStyle()
    ROOT.gROOT.ForceStyle()
    
    histDetails.hist.UseCurrentStyle()
    
    #ROOT.gStyle.SetTitleOffset(0.9 * histDetails.zTitleOffsetScale, "Z")
    
    ROOT.TGaxis.SetMaxDigits(axisLabelMaxDigits)
    #ROOT.TGaxis.SetExponentOffset(ROOT.gStyle.GetTitleOffset("Z") * histDetails.zTitleOffsetScale, -0.5, "z")
    
    #ROOT.gStyle.SetTitleFont(62, "T")
    #ROOT.gStyle.SetTitleW(1)
    #ROOT.gStyle.SetTitleW(ROOT.gStyle.GetTitleW() * histDetails.titleSizeScale)
    #ROOT.gStyle.SetTitleY(0.985 * histDetails.titleOffsetScale)
    #
    #ROOT.gStyle.SetTitleFont(62, "XYZ")
    
    if (palette is not None) :
        
        ROOT.gStyle.SetPalette(palette)
    
    if (nContour > 0) :
        
        ROOT.gStyle.SetNumberContours(nContour)
    
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptFit(0)
    
    canvas = ROOT.TCanvas("canvas", "canvas")
    canvas.SetCanvasSize(800, 600)
    
    canvas.SetLeftMargin(0.15)
    canvas.SetRightMargin(0.21)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    
    padTop = 1 - canvas.GetTopMargin()
    padRight = 1 - canvas.GetRightMargin()
    padBottom = canvas.GetBottomMargin()
    padLeft = canvas.GetLeftMargin()
    
    # X range
    if (histDetails.xMin != initVal and histDetails.xMax != initVal) :
        
        histDetails.hist.GetXaxis().SetRangeUser(
            histDetails.xMin,
            histDetails.xMax
        )
    
    elif (histDetails.xMin != initVal) :
        
        histDetails.hist.GetXaxis().SetRangeUser(
            histDetails.xMin,
            histDetails.hist.GetXaxis().GetXmax()
        )
    
    elif (histDetails.xMax != initVal) :
        
        histDetails.hist.GetXaxis().SetRangeUser(
            histDetails.hist.GetXaxis().GetXmin(),
            histDetails.xMax
        )
    
    # Y range
    if (histDetails.yMin != initVal and histDetails.yMax != initVal) :
        
        histDetails.hist.GetYaxis().SetRangeUser(
            histDetails.yMin,
            histDetails.yMax
        )
    
    elif (histDetails.yMin != initVal) :
        
        histDetails.hist.GetYaxis().SetRangeUser(
            histDetails.yMin,
            histDetails.hist.GetYaxis().GetXmax()
        )
    
    elif (histDetails.yMax != initVal) :
        
        histDetails.hist.GetYaxis().SetRangeUser(
            histDetails.hist.GetYaxis().GetXmin(),
            histDetails.yMax
        )
    
    # Z range
    if (histDetails.zMin != initVal) :
        
        histDetails.hist.SetMinimum(histDetails.zMin)
    
    if (histDetails.zMax != initVal) :
        
        histDetails.hist.SetMaximum(histDetails.zMax)
    
    # Axis divisions
    if (abs(sum(histDetails.nDivisionsX)) > 0) :
        
        histDetails.hist.GetXaxis().SetNdivisions(histDetails.nDivisionsX[0], histDetails.nDivisionsX[1], histDetails.nDivisionsX[2])
    
    if (abs(sum(histDetails.nDivisionsY)) > 0) :
        
        histDetails.hist.GetYaxis().SetNdivisions(histDetails.nDivisionsY[0], histDetails.nDivisionsY[1], histDetails.nDivisionsY[2])
    
    # Bin label position
    if (histDetails.centerLabelsX) :
        
        histDetails.hist.GetXaxis().CenterLabels()
    
    if (histDetails.centerLabelsY) :
        
        histDetails.hist.GetYaxis().CenterLabels()
    
    
    # Draw
    #histDetails.hist.Draw()
    #histDetails.hist.Draw("nostack")
    #histDetails.hist.Draw("colz")
    histDetails.hist.Draw("%s goff" %(histDetails.drawOption))
    
    
    histDetails.hist.GetXaxis().SetTitle(histDetails.xTitle)
    histDetails.hist.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * histDetails.xTitleSizeScale)
    histDetails.hist.GetXaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("X") * histDetails.xTitleOffsetScale)
    histDetails.hist.GetXaxis().CenterTitle(True)
    
    histDetails.hist.GetYaxis().SetTitle(histDetails.yTitle)
    histDetails.hist.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * histDetails.yTitleSizeScale)
    histDetails.hist.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("Y") * histDetails.yTitleOffsetScale)
    histDetails.hist.GetYaxis().CenterTitle(True)
    
    histDetails.hist.GetZaxis().SetTitle(histDetails.zTitle)
    histDetails.hist.GetZaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Z") * histDetails.zTitleSizeScale)
    histDetails.hist.GetZaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("Z") * histDetails.zTitleOffsetScale)
    histDetails.hist.GetZaxis().CenterTitle(True)
    
    #histDetails.hist.GetListOfFunctions().FindObject("palette").GetAxis().SetExponentOffset(ROOT.gStyle.GetTitleOffset("Z") * histDetails.zTitleOffsetScale, -0.5)
    
    #print("*"*50, histDetails.hist.GetMaximum(), histDetails.hist.GetMinimum())
    
    #title = ROOT.TPaveText(0.0, 0.89, 1.0, 0.995, "NDC")
    title = ROOT.TPaveText(padLeft, 0.89, padRight, 0.995, "NDC")
    title.AddText(histDetails.histTitle)
    
    title.SetMargin(0)
    title.SetFillStyle(0)
    title.SetBorderSize(0)
    title.SetTextFont(ROOT.gStyle.GetTitleFont())
    title.SetTextColor(1)
    title.SetTextAlign(21)
    title.SetTextSize(0.05 * histDetails.titleSizeScale)
    
    title.Draw()
    
    canvas.SetLogx(histDetails.logX)
    canvas.SetLogy(histDetails.logY)
    canvas.SetLogz(histDetails.logZ)
    
    canvas.SetGridx(histDetails.gridX)
    canvas.SetGridy(histDetails.gridY)
    
    # Extra text
    for iText in range(0, len(l_extraText)) :
        
        textX = l_extraText[iText][0]
        textY = l_extraText[iText][1]
        text = l_extraText[iText][2]
        
        if (len(text)) :
            
            latex = ROOT.TLatex(textX, textY, text)
            #latex.SetTextFont(62);
            latex.SetTextSize(0.0425);
            latex.SetTextAlign(13);
            
            #latex.Draw()
            
            textXsize = latex.GetXsize()
            textYsize = latex.GetYsize()
            textBoxMargin = 0.1 * min(textXsize, textYsize)
            print(textXsize, textYsize, textBoxMargin, latex.GetX(), latex.GetY())
            
            textX_NDC = getNDC(canvas, textX, axis = "X")
            textY_NDC = getNDC(canvas, textY, axis = "Y")
            
            textBox = ROOT.TPaveText(textX_NDC, textY_NDC, textX_NDC+textXsize+2*textBoxMargin, textY_NDC-textYsize-2*textBoxMargin, "NDC")
            textBox.AddText(text)
            
            textBox.SetMargin(0)
            textBox.SetFillStyle(1001)
            textBox.SetBorderSize(1)
            textBox.SetTextFont(62)
            textBox.SetTextColor(1)
            textBox.SetTextAlign(22)
            textBox.SetTextSize(0.0425)
            textBox.SetFillColorAlpha(ROOT.kWhite, 0.6)
            
            textBox.Draw()
    
    #ROOT.gPad.Modified()
    canvas.Update()
    
    #outFileName = histDetails.outFileName + ("_"*(histDetails.outFileName_suffix != "")) + histDetails.outFileName_suffix + ".pdf"
    print("Output: %s" %(histDetails.outFileName))
    
    #canvas.SaveAs(histDetails.outFileName + ".pdf")
    #canvas.SaveAs(histDetails.outFileName + ".png")
    
    canvas.SaveAs(histDetails.outFileName)
    canvas.SaveAs(histDetails.outFileName.replace(".pdf", ".png"))
    
    print("\n")
