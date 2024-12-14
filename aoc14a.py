#!/usr/bin/env python3

import json
import re

import aoc

data_in = aoc.read_input()
xmax = 101
ymax = 103

#data_in = aoc.read_example()
#xmax = 11
#ymax = 7

class Robot:
    def __init__(self, line):
        p, v = line.split()
        self.px, self.py = [int(x) for x in p[2:].split(",")]
        self.vx, self.vy = [int(x) for x in v[2:].split(",")]

    def move(self, xmax, ymax):
        self.px += self.vx
        if self.px >= xmax:
            self.px = self.px - xmax
        if self.px < 0:
            self.px = xmax + self.px
        self.py += self.vy
        if self.py >= ymax:
            self.py = self.py - ymax
        if self.py < 0:
            self.py = ymax + self.py

robots = []
for line in data_in:
    robots.append(Robot(line))
for t in range(100):
    for r in robots:
        r.move(xmax, ymax)

quadrants = {"NW": 0, "NE": 0, "SE": 0, "SW": 0}
for r in robots:
    print(f"{r.px}:{r.py}")
    lat = None
    lon = None
    if r.px < xmax // 2:
        lon = "W"
    if r.px > xmax // 2:
        lon = "E"
    if r.py < ymax // 2:
        lat = "N"
    if r.py > ymax // 2:
        lat = "S"
    if lat is None or lon is None:
        continue
    print(f"{lat}{lon}")
    quadrants[f"{lat}{lon}"] += 1
total = 1
for n in quadrants.values():
    print(n)
    total *= n
print(total)
