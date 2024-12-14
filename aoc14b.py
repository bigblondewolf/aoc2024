#!/usr/bin/env python3

import json
import os
import re
import time
import sys

import aoc

DEBUG = False

data_in = aoc.read_input()
xmax = 101
ymax = 103

#data_in = aoc.read_example()
#xmax = 11
#ymax = 7

def printd(msg):
    if DEBUG:
        print(msg)

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

    def __repr__(self):
        return f"{self.px}:{self.py}"



def draw_field(robots, xmax, ymax):
    os.system("clear")
    for y in range(ymax):
        for x in range(xmax):
            symbol = "."
            for r in robots:
                if r.px == x and r.py == y:
                    symbol = "X"
            sys.stdout.write(symbol)
        sys.stdout.write("\n")

def is_christmas_tree(robots, xmax, ymax):
    for y in range(ymax):
        printd("======================")
        printd(f"Line {y}")
        line_ok = True
        if y == ymax - 1:
            for r in robots:
                if r.px == xmax // 2 and r.py == y:
                    printd("Found xmid")
                    return True
        for x in range(xmax):
            printd(f"  X: {x}, mid: {xmax//2}, range {(xmax//2)-y}:{(xmax//2)+y}")
            if x >= (xmax // 2) - y and x <= (xmax // 2) + y:
                printd(f"    Search...")
                found = False
                for r in robots:
                    printd(f"    R: {r.px}:{r.py}")
                    if r.px == x and r.py == y:
                        found = True
                        printd("      Found")
                        break
                if not found:
                    return False
        printd(f"  Line OK: {line_ok}")
        if not line_ok:
            return False
    return False

def is_vertical_line(robots, xmax, ymax):
    for y in range(ymax):
        found = False
        for r in robots:
            if r.px == xmax // 2 and r.py == y:
                found = True
                break
        if not found:
            return False
    return True


def is_horiz_line(robots, xmax, ymax):
    arranged = {}
    for y in range(ymax):
        arranged[y] = [r for r in robots if r.py == y]
        row = ""
        for x in range(xmax):
            found = False
            for r in arranged[y]:
                if r.px == x:
                    found = True
            if found:
                row += "x"
            else:
                row += "o"
        if "xxxxxxxxx" in row:
            return True
    return False

robots = []
for line in data_in:
    r = Robot(line)
    robots.append(r)
for t in range(1000000):
    if t % 1000 == 0:
        print(t)
    for r in robots:
        r.move(xmax, ymax)
    if is_horiz_line(robots, xmax, ymax):
        print(t)
        sys.exit(0)

