#!/usr/bin/env python3

from collections import Counter
import aoc

data_in = aoc.read_input()

l1 = sorted([int(d.split()[0]) for d in data_in])
l2 = sorted([int(d.split()[1]) for d in data_in])

dist = 0
for i in range(len(l2)):
    dist += abs(l1[i] - l2[i])
print(dist)
