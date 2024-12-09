#!/usr/bin/env python3

import itertools
import collections

import aoc

data_in = aoc.read_input_aslist()
#data_in = aoc.read_example_aslist()

Point = collections.namedtuple("Point", ["x", "y"])

def is_ant(p):
    return data_in[p.y][p.x] != "."

antennas = {}

antinodes = set()

xmax = len(data_in[0])
ymax = len(data_in)

for y in range(ymax):
    for x in range(xmax):
        if is_ant(Point(x, y)):
            label = data_in[y][x]
            if label not in antennas:
                antennas[label] = [Point(x, y)]
                continue
            for a in antennas[label]:
                dx = x - a.x
                dy = y - a.y
                if(0 <= x + dx
                    and x + dx < xmax
                    and 0 <= y + dy
                    and y + dy < ymax
                   ):
                    antinodes.add(Point(x+dx, y+dy))
                if(0 <= a.x - dx
                    and a.x - dx < xmax
                    and 0 <= a.y - dy
                    and a.y - dy < ymax
                   ):
                    antinodes.add(Point(a.x-dx, a.y-dy))
            antennas[label].append(Point(x, y))
print(len(antinodes))

