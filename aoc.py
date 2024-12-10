import os.path
import sys

def read_input():
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    return [r.strip() for r in data_in]

def read_example():
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt.example"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    return [r.strip() for r in data_in]

def read_input_aslist():
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    if " " in data_in[0]:
        return [x.split() for x in data_in]
    return [list(x.strip()) for x in data_in]

def read_example_aslist():
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt.example"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    if " " in data_in[0]:
        return [x.split() for x in data_in]
    return [list(x.strip()) for x in data_in]

def read_input_aslist_parseints(has_spaces=True):
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    if has_spaces:
        return [[int(y) for y in x.split()] for x in data_in]
    else:
        return [[int(y) for y in x.strip()] for x in data_in]

def read_example_aslist_parseints(has_spaces=True):
    input_fn = os.path.basename(sys.argv[0])[:5] + ".txt.example"
    with open(input_fn) as infile:
        data_in = infile.readlines()
    if has_spaces:
        return [[int(y) for y in x.split()] for x in data_in]
    else:
        return [[int(y) for y in x.strip()] for x in data_in]
