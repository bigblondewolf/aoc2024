#!/usr/bin/env python3

import itertools
import json
from functools import cache

import networkx as nx

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

DEBUG = False

def printd(msg):
    if DEBUG:
        print(msg)


@cache
def pattern_ok(pat):
    printd(f"Call {pat}")
    for t in towels:
        printd(f"  {t}")
        if pat == t:
            printd(f"    Same")
            return True
        if len(pat) > len(t) and pat.startswith(t):
            printd(f"    Startswith")
            ok = pattern_ok(pat[len(t):])
            if ok:
                return True
        printd(f"  {t} NO")
    return False

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

#print(pattern_ok(patterns[0]))
total = 0
for p in patterns:
    #print(f"{p} {pattern_ok(p)}")
    if pattern_ok(p):
        total += 1
print(f"{total} / {len(patterns)}")
