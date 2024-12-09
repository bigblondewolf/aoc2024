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
                antinodes.add(Point(x, y))
                antennas[label] = [Point(x, y)]
                continue
            for a in antennas[label]:
                dx = x - a.x
                dy = y - a.y
                times = 1
                while(0 <= x + (times * dx)
                    and x + (times * dx) < xmax
                    and 0 <= y + (times * dy)
                    and y + (times * dy) < ymax
                   ):
                    antinodes.add(Point(x+(times*dx), y+(times*dy)))
                    times += 1
                times = 1
                while(0 <= a.x - (times * dx)
                    and a.x - (times * dx) < xmax
                    and 0 <= a.y - (times * dy)
                    and a.y - (times * dy) < ymax
                   ):
                    antinodes.add(Point(a.x-(times*dx), a.y-(times*dy)))
                    times += 1
            antinodes.add(Point(x, y))
            antennas[label].append(Point(x, y))
print(len(antinodes))

