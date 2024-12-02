#!/usr/bin/env python3

import copy
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
    ignores = 0
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            is_dec = True
        if l[i] < l[i+1]:
            is_inc = True
        if l[i] == l[i+1] or (is_inc and is_dec) or abs(l[i]-l[i+1]) > 3 or abs(l[i]-l[i+1]) < 1:
            return False
    return True

def is_incdec_diff_damp(l):
    for i in range(len(l)):
        l1 = copy.deepcopy(l)
        del l1[i]
        if is_incdec_diff(l1):
            return True
    return False

safe = 0
for row in data_in:
    if is_incdec_diff(row):
        safe += 1
        continue
    if is_incdec_diff_damp(row):
        safe += 1
print(safe)
