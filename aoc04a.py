#!/usr/bin/env python3

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()
data_in = [r.strip() for r in data_in]

ymax = len(data_in)
xmax = len(data_in[0])

print(f"{xmax} cols {ymax} rows")

total = 0

# Horizontal
for x in range(xmax-3):
    for y in range(ymax):
        if(
            data_in[y][x:x+4] == "XMAS"
            or data_in[y][x:x+4] == "SAMX"
            ):
            total += 1

# Vertical
for x in range(xmax):
    for y in range(ymax-3):
        if(
            (
                data_in[y][x] == "X"
                and data_in[y+1][x] == "M"
                and data_in[y+2][x] == "A"
                and data_in[y+3][x] == "S"
                )
            or(
                data_in[y][x] == "S"
                and data_in[y+1][x] == "A"
                and data_in[y+2][x] == "M"
                and data_in[y+3][x] == "X"
                )
            ):
            total += 1

# Diagonal NW-SE
for x in range(xmax-3):
    for y in range(ymax-3):
        if(
            (
                data_in[y][x] == "X"
                and data_in[y+1][x+1] == "M"
                and data_in[y+2][x+2] == "A"
                and data_in[y+3][x+3] == "S"
                )
            or(
                data_in[y][x] == "S"
                and data_in[y+1][x+1] == "A"
                and data_in[y+2][x+2] == "M"
                and data_in[y+3][x+3] == "X"
                )
            ):
            total += 1

# Diagonal NE-SW
for x in range(3, xmax):
    for y in range(ymax-3):
        if(
            (
                data_in[y][x] == "X"
                and data_in[y+1][x-1] == "M"
                and data_in[y+2][x-2] == "A"
                and data_in[y+3][x-3] == "S"
                )
            or(
                data_in[y][x] == "S"
                and data_in[y+1][x-1] == "A"
                and data_in[y+2][x-2] == "M"
                and data_in[y+3][x-3] == "X"
                )
            ):
            total += 1
print(total)
