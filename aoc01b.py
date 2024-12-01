#!/usr/bin/env python3

import json
from collections import Counter

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

l1 = [int(d.split()[0]) for d in data_in]
l2 = [int(d.split()[1]) for d in data_in]

c2 = {k:v for k, v in Counter(l2).items()}
print(json.dumps(c2, indent=2, sort_keys=True))
score = 0
for l in l1:
    score += l * c2.get(l, 0)
print(score)
