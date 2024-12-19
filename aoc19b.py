#!/usr/bin/env python3

import itertools
import json
from functools import cache

import networkx as nx

import aoc

#data_in = aoc.read_input()
data_in = aoc.read_example()

DEBUG = True

def printd(msg):
    if DEBUG:
        indent = "  " * rec_lvl
        print(indent + msg)


rec_lvl = 0
@cache
def pattern_ok(pat):
    global rec_lvl
    rec_lvl += 1
    printd(f"Call {pat}")
    good_combos = 0
    for t in towels:
        printd(f"  {t}")
        if pat == t:
            printd(f"    RET {pat} {t} SAME 1")
            rec_lvl -= 1
            return 1
        if len(pat) > len(t) and pat.startswith(t):
            printd(f"    Startswith, try {pat[len(t):]}")
            ok = pattern_ok(pat[len(t):])
            printd(f"      {ok}")
            if ok > 0:
                good_combos += ok
        printd(f"  {t} {good_combos}")
    printd(f"  RET: {pat}: {good_combos}")
    rec_lvl -= 1
    return good_combos

towels = []
patterns = []
inventory_done = False
for line in data_in:
    if inventory_done:
        patterns.append(line)
        continue
    if line == "":
        inventory_done = True
        continue
    towels.extend(line.replace(" ", "").split(","))
print(towels)
print(patterns)

print(pattern_ok(patterns[3]))
total = 0
for p in patterns:
    #print(f"{p} {pattern_ok(p)}")
    this_pattern = pattern_ok(p)
    print(f" {p} {this_pattern}")
    if this_pattern > 0:
        total += this_pattern
print(f"{total} / {len(patterns)}")
