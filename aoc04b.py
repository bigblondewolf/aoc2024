#!/usr/bin/env python3

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()
data_in = [r.strip() for r in data_in]

total = 0

for x in range(1, xmax-1):
    for y in range(1, xmax-1):
        if data_in[y][x] == "A":
            nwse = data_in[y-1][x-1] + data_in[y][x] +data_in[y+1][x+1]
            nesw = data_in[y-1][x+1] + data_in[y][x] +data_in[y+1][x-1]
            if nwse in ["MAS", "SAM"] and nesw in ["MAS", "SAM"]:
                total += 1
print(total)

