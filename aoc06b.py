#!/usr/bin/env python3

import collections
import json

import aoc

DEBUG = False

data_in = aoc.read_input_aslist()
#data_in = aoc.read_example_aslist()

Point = collections.namedtuple("Point", ["x", "y"])

class Guard:
    def __init__(self, pos, dir="N"):
        self.dir = dir
        self.pos = pos

    def turn(self, dir="r"):
        """Orientate according to instruction,"""
        if dir == "r":
            if self.dir== "N":
                self.dir = "E"
            elif self.dir == "E":
                self.dir = "S"
            elif self.dir == "S":
                self.dir = "W"
            elif self.dir == "W":
                self.dir = "N"
        if dir == "l":
            if self.dir== "N":
                self.dir = "W"
            elif self.dir == "W":
                self.dir = "S"
            elif self.dir == "S":
                self.dir = "E"
            elif self.dir == "E":
                self.dir = "N"

    @property
    def next_step(self):
        """Where next step will be, if done."""
        if self.dir== "N":
            return Point(self.pos.x, self.pos.y-1)
        elif self.dir == "E":
            return Point(self.pos.x+1, self.pos.y)
        elif self.dir == "S":
            return Point(self.pos.x, self.pos.y+1)
        elif self.dir == "W":
            return Point(self.pos.x-1, self.pos.y)

    def step(self):
        self.pos = self.next_step

    def __str__(self):
        return f"{self.pos.x}:{self.pos.y} {self.dir}"

def printd(what):
    if DEBUG:
        print(what)


xmax = len(data_in[0])
ymax = len(data_in)

# Find the guard.
for y in range(ymax):
    for x in range(xmax):
        if data_in[y][x] == "^":
            g = Guard(Point(x, y))
            printd(f"Found guard: {g}")
            break

occupied = []
steps = 1
maxsteps = 10000
while True:
    turns = 0
    maxturns = 5
    if steps > maxsteps:
        break
    steps += 1
    ns = g.next_step
    if ns.x < 0 or ns.x > xmax-1 or ns.y < 0 or ns.y > ymax-1:
        break
    while data_in[ns.y][ns.x] == "#":
        turns += 1
        if turns > maxturns:
            break
        g.turn()
        ns = g.next_step
        if ns.x < 0 or ns.x > xmax-1 or ns.y < 0 or ns.y > ymax-1:
            break
    g.step()
    if g.pos.x < 0 or g.pos.x > xmax-1 or g.pos.y < 0 or g.pos.y > ymax-1:
        break
    if data_in[g.pos.y][g.pos.x] != "X":
        occupied.append(g.pos)
        data_in[g.pos.y][g.pos.x] = "X"

print(f"{len(occupied)} obstacles to place")

data_in = aoc.read_input_aslist()
#data_in = aoc.read_example_aslist()

# Find the guard.
for y in range(ymax):
    for x in range(xmax):
        if data_in[y][x] == "^":
            g = Guard(Point(x, y))
            printd(f"Found guard: {g}")
            break

loops = 0
for nr, field in enumerate(occupied):
    print(f"Obstacle {nr}/{len(occupied)}")
    data_in = aoc.read_input_aslist()
    #data_in = aoc.read_example_aslist()
    printd(f"Obstacle at {field}")
    # Find the guard.
    for y in range(ymax):
        for x in range(xmax):
            if data_in[y][x] == "^":
                g = Guard(Point(x, y))
                printd(f"Found guard: {g}")
                break
    data_in[field.y][field.x] = "#"
    steps = 1
    maxsteps = 10000
    while True:
        turns = 0
        maxturns = 5
        if steps > maxsteps:
            break
        steps += 1
        printd(f"Enter loop: {g}")
        if g.dir in data_in[g.pos.y][g.pos.x]:
            print(f"Loop on {g.pos.x}:{g.pos.y} dir {g.dir}")
            loops += 1
            break
        data_in[g.pos.y][g.pos.x] += g.dir
        ns = g.next_step
        if ns.x < 0 or ns.x > xmax-1 or ns.y < 0 or ns.y > ymax-1:
            printd(f"{g}, next step {ns} will be out of field!")
            break
        while data_in[ns.y][ns.x] == "#":
            turns += 1
            if turns > maxturns:
                printd("Max turns")
                break
            printd("Turn")
            g.turn()
            ns = g.next_step
            if ns.x < 0 or ns.x > xmax-1 or ns.y < 0 or ns.y > ymax-1:
                printd(f"{g} next ste[ {ns} will be out of field, while turning.")
                break
        g.step()
        printd(f"Step, now on: {g}")
        if g.pos.x < 0 or g.pos.x > xmax-1 or g.pos.y < 0 or g.pos.y > ymax-1:
            printd(f"{g} went out of field")
            break
        printd("Loop done")

print(loops)

