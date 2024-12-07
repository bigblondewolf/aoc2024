#!/usr/bin/env python3

import itertools

import aoc

data_in = aoc.read_input_aslist()
#data_in = aoc.read_example_aslist()

for r in data_in:
    r[0] = int(r[0][:-1])
    r[1:] = [int(x) for x in r[1:]]

def compute(l, r, op):
    if op == "+":
        return l+r
    if op == "*":
        return l*r


total = 0
for row in data_in:
    for ops in itertools.product(["+", "*"], repeat=len(row)-2):
        res = row[1]
        for i, v_in in enumerate(row[2:]):
            res = compute(res, v_in, ops[i])
        if res == row[0]:
            total += res
            break
print(total)
