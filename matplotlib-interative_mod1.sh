#!/usr/bin/env python

# /opt/anaconda3/bin/python

import argparse
import numpy
import pickle
#import plotly
import pprint
import matplotlib



parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--input",
    help = "Input pickle file",
    required = True,
    type = str,
)

parser.add_argument(
    "-o",
    "--output",
    help = "Output pdf file",
    required = False,
    type = str,
    default = ""
)

parser.add_argument(
    "--yMin",
    help = "Y-axis lower limit",
    required = False,
    type = float,
    default = 0.0,
)

parser.add_argument(
    "--yMax",
    help = "Y-axis upper limit",
    required = False,
    type = float,
    default = 0.05,
)


args = parser.parse_args()


fig = pickle.load(open(args.input, "rb"))

axis1 = fig.axes[0]

axis1.set_yticks(numpy.arange(0, 1, 0.01))
axis1.set_yticks(numpy.arange(0, 1, 0.01/10.0), minor = True)
axis1.set_ylim([args.yMin, args.yMax])

#axis1.majorticks_on()
#axis1.minorticks_on()

axis1.grid(axis = "both", which = "major", linestyle = "--", linewidth = "0.5")


if (len(args.output)) :
    
    print("Saving: %s" %(args.output))
    fig.savefig(args.output)

matplotlib.pyplot.show(block = True)
