#!/usr/bin/env python3

import collections
import json
import os
import re
import time

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

ANIM_DELAY = 0.01
Point = collections.namedtuple("Point", ["x", "y"])

class MapItem:
    def __init__(self,x, y):
        self.pos = Point(x, y)

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

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

    def __str__(self):
        return f"{self.x}:{self.y}"

    def __repr__(self):
        return f"{self.x}:{self.y}"

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

def draw_map():
    field = []
    for y in range(ymax):
        row = []
        for c in range(xmax):
            row.append(".")
        field.append(row)
    for w in walls_boundary:
        field[w.y][w.x] = "#"
    for w in walls_inside:
        field[w.y][w.x] = "#"
    for b in boxes:
        field[b.y][b.x] = "O"
    field[robot.y][robot.x] = "@"
    os.system("clear")
    for row in field:
        print("".join(row))


def move_object(obj, dir):
    next_step = obj.next_step(dir)
    for w in walls_boundary:
        if w.pos == next_step:
            return False
    for w in walls_inside:
        if w.pos == next_step:
            return False
    for b in boxes:
        if b.pos == next_step:
            if move_object(b, dir):
                obj.move(dir)
                return True
            else:
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
        xmax = len(line)
    if map_done:
        for char in line:
            directions.append(char)
            continue
    for char_nr, char in enumerate (line):
        if char == "#":
            if all([c == "#" for c in line]):
                walls_boundary.append(WallBoundary(char_nr, line_nr))
                if line_nr > 0:
                    ymax = line_nr + 1
                    map_done = True
                continue
            if char_nr == 0 or char_nr == len(line)-1:
                walls_boundary.append(WallBoundary(char_nr, line_nr))
                continue
            walls_inside.append(WallInside(char_nr, line_nr))
            continue
        if char == "O":
            boxes.append(Box(char_nr, line_nr))
            continue
        if char == "@":
            if robot is None:
                robot = Robot(char_nr, line_nr)
                continue
            raise ValueError(f"Robot already exists on {robot}")

print(f"ymax: {ymax} xmax: {xmax}")
#draw_map()
#time.sleep(ANIM_DELAY)
for d_nr, d in enumerate(directions):
    move_object(robot, d)
    #draw_map()
    #print(f"Step {d_nr} of {len(directions)}")
    #time.sleep(ANIM_DELAY)
gps_total = 0
for b in boxes:
    gps_total += b.gps
print(gps_total)
