#!/usr/bin/env python3

import json
import re

import numpy as np

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

matrices = []
for line in data_in:
    line_l = line.split()
    if line.startswith("Button A:"):
        ma = []
        ma.append([int(line_l[2][2:-1])])
        ma.append([int(line_l[3][2:])])
        continue
    if line.startswith("Button B:"):
        ma[0].append(int(line_l[2][2:-1]))
        ma[1].append(int(line_l[3][2:]))
        continue
    if line.startswith("Prize: "):
        mb = [int(line_l[1][2:-1]), int(line_l[2][2:])]
        matrices.append((ma, mb))

cost = 0
sols = 0
for m in matrices:
    sol = np.linalg.solve(m[0], m[1])
    print(sol)
    round_nums = re.compile(r"(\d+)\. (\d+)\.")
    m = round_nums.search(np.array2string(sol))
    if m:
        print("  ROUND")
        cost += int(m.group(1)) * 3 + int(m.group(2))
        sols += 1
print(cost)
print(f"M: {len(matrices)} S: {sols}")
