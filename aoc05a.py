#!/usr/bin/env python3

import aoc
import json

data_in = aoc.read_input()
#data_in = aoc.read_example()

ORDERING = []
UPDATES = {}

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
    if update_ok:
        mid = len(UPDATES[update]) // 2
        total += int(update.split(",")[mid])
print(total)

