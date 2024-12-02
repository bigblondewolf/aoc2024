#!/usr/bin/env python3

import aoc

data_in = aoc.read_input_aslist_parseints()
#data_in = aoc.read_example_aslist_parseints()

def is_increasing(l):
    for i in range(len(l)-1):
        if l[i+1] <= l[i]:
            return False
    return True


def is_decreasing(l):
    for i in range(len(l)-1):
        if l[i+1] >= l[i]:
            return False
    return True

def is_incdec(l):
    is_inc = False
    is_dec = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            is_dec = True
        if l[i] < l[i+1]:
            is_inc = True
        if l[i] == l[i+1] or (is_inc and is_dec):
            return False
    return True

def is_incdec_diff(l):
    is_inc = False
    is_dec = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            is_dec = True
        if l[i] < l[i+1]:
            is_inc = True
        if l[i] == l[i+1] or (is_inc and is_dec) or abs(l[i]-l[i+1]) > 3 or abs(l[i]-l[i+1]) < 1:
            return False
    return True

safe = 0
for row in data_in:
    #print(f"{row} Incr: {is_increasing(row)} decr: {is_decreasing(row)}")
    #print(f"{row} IncDec: {is_incdec(row)}")
    #print(f"{row} IncDec: {is_incdec_diff(row)}")
    if is_incdec_diff(row):
        safe += 1
print(safe)
