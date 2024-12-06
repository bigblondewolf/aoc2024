#!/usr/bin/env python3

import functools

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

ORDERING = []
UPDATES = {}

def mysort(a, b):
    for order in ORDERING:
        if (a, b) == order:
            return -1
    return 1


in_ordering = True
for row in data_in:
    if in_ordering:
        if row.strip() == "":
            in_ordering = False
            continue
        ORDERING.append(tuple([int(i) for i in row.strip().split("|")]))
        continue
    UPDATES[row.strip()] = {}
    for i, u in enumerate(row.strip().split(",")):
        UPDATES[row.strip()][int(u)] = i+1

total = 0
for update in UPDATES:
    update_ok = True
    for o in ORDERING:
        if not all([oi in UPDATES[update] for oi in o]):
            continue
        update_ok = UPDATES[update][o[0]] < UPDATES[update][o[1]]
        if not update_ok:
            break
    if not update_ok:
        u_sorted = sorted(UPDATES[update].keys(), key=functools.cmp_to_key(mysort))
        mid = len(u_sorted) // 2
        total += u_sorted[mid]
print(total)
