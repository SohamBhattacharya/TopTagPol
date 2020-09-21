#!/usr/bin/env python

# /opt/anaconda3/bin/python

import argparse
import pickle
import matplotlib


parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--input",
    help = "Pickle file",
    required = True,
    type = str,
)

args = parser.parse_args()


fig = pickle.load(open(args.input, "rb"))

matplotlib.pyplot.show(block = True)
