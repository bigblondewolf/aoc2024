import os.path
import sys

def read_input():
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    return data_in

def read_example():
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt.example"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    return data_in
