import argparse
import numpy
import os
import subprocess

import sampleInfo


cppFileName = "topTaggingTreeMaker.cc"
cppFileName_noExt = cppFileName[: cppFileName.find(".")]


d_info = sampleInfo.d_info


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

l_sampleInfo = ["%s (%d files)" %(key, len(d_info[key]["inputFiles"])) for key in d_info.keys()]

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
        
        #if (iFile+1 < 46) : continue
        
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

