#!/usr/bin/env python3

import collections
import json
import os
import re
import time
import sys

import aoc

#data_in = aoc.read_input()
data_in = aoc.read_example()

ANIM_DELAY = 0.01
Point = collections.namedtuple("Point", ["x", "y"])

class MapItem:
    def __init__(self,x, y, width=2):
        self.pos = Point(x, y)
        self.width = width

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def __str__(self):
        return f"{self.x}:{self.y}"

    def __repr__(self):
        return f"{self.x}:{self.y}"

    def span_at(self, coord):
        span = []
        for x in range(self.width):
            span.append(Point(coord.x+x, coord.y))
        return span

    def overlaps(self, other):
        o = False
        for c in other:
            if self.y == c.y:
                for p in range(self.width):
                    if self.x + p == c.x:
                        return True
        return False

class MovableMapItem(MapItem):
    def next_step(self, dir):
        if dir == "^":
            return Point(self.pos.x, self.pos.y-1)
        if dir == ">":
            return Point(self.pos.x+1, self.pos.y)
        if dir == "v":
            return Point(self.pos.x, self.pos.y+1)
        if dir == "<":
            return Point(self.pos.x-1, self.pos.y)
        raise ValueError(f"Unknown direction to move: {dir}")

    def move(self, dir):
        self.pos = self.next_step(dir)

class StaticMapItem(MapItem):
    pass

class Robot(MovableMapItem):
    pass

class Box(MovableMapItem):
    @property
    def gps(self):
        return self.x + (100 * self.y)

class Obstacle(StaticMapItem):
    pass

class WallBoundary(Obstacle):
    pass

class WallInside(Obstacle):
    pass

def draw_map(clear=True, dir="@"):
    field = []
    for y in range(ymax):
        row = []
        for c in range(xmax):
            row.append(".")
        field.append(row)
    for w in walls_boundary:
        field[w.y][w.x] = "#"
        field[w.y][w.x+1] = "#"
    for w in walls_inside:
        field[w.y][w.x] = "#"
        field[w.y][w.x+1] = "#"
    for b in boxes:
        field[b.y][b.x] = "["
        field[b.y][b.x+1] = "]"
    field[robot.y][robot.x] = dir
    if clear:
        os.system("clear")
    for row in field:
        print("".join(row))

def move_object(obj, dir):
    next_step = obj.next_step(dir)
    for w in walls_boundary:
        if w.overlaps(obj.span_at(next_step)):
            return False
    for w in walls_inside:
        if w.overlaps(obj.span_at(next_step)):
            return False
    for b in boxes:
        if b == obj:
            continue
        if b.overlaps(obj.span_at(next_step)):
            if not move_object(b, dir):
                return False
    obj.move(dir)
    return True

directions = []
walls_boundary = []
walls_inside = []
robot = None
boxes = []
xmax = 0
ymax = 0

map_done = False
for line_nr, line in enumerate(data_in):
    if not map_done:
        xmax = len(line)*2
    if map_done:
        for char in line:
            directions.append(char)
            continue
    for char_nr, char in enumerate (line):
        if char == "#":
            if all([c == "#" for c in line]):
                walls_boundary.append(WallBoundary(char_nr*2, line_nr))
                if line_nr > 0:
                    ymax = line_nr + 1
                    map_done = True
                continue
            if char_nr == 0 or char_nr == len(line)-1:
                walls_boundary.append(WallBoundary(char_nr*2, line_nr))
                continue
            walls_inside.append(WallInside(char_nr*2, line_nr))
            continue
        if char == "O":
            boxes.append(Box(char_nr*2, line_nr))
            continue
        if char == "@":
            if robot is None:
                robot = Robot(char_nr*2, line_nr, 1)
                continue
            raise ValueError(f"Robot already exists on {robot}")

print(f"ymax: {ymax} xmax: {xmax}")
#draw_map()
#time.sleep(ANIM_DELAY)
for d_nr, d in enumerate(directions):
    move_object(robot, d)
    d_next = "X"
    if d_nr < len(directions)-1:
        d_next = directions[d_nr+1]
    draw_map(d_next)
    if d_nr % 1000 == 0:
        print(f"{d_next} :Step {d_nr} of {len(directions)}")
gps_total = 0
for b in boxes:
    gps_total += b.gps
print(gps_total)
