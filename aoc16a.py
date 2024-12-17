#!/usr/bin/env python3

import itertools
import json

import networkx as nx

import aoc

#data_in = aoc.read_input()
data_in = aoc.read_example()

def turn_right(dir):
    if dir == ">":
        return "v"
    if dir == "v":
        return "<"
    if dir == "<":
        return "^"
    if dir == "^":
        return ">"


def turn_left(dir):
    if dir == ">":
        return "^"
    if dir == "^":
        return "<"
    if dir == "<":
        return "v"
    if dir == "v":
        return ">"


def get_next_coord(x, y, dir):
    if dir == ">":
        xnew = x+1
        ynew = y
    if dir == "<":
        xnew = x-1
        ynew = y
    if dir == "^":
        xnew = x
        ynew = y-1
    if dir == "v":
        xnew = x
        ynew = y+1
    return (xnew, ynew)


G = nx.Graph()
iter=0
for y, row in enumerate(data_in):
    for x, char in enumerate(row):
        iter+=1
        if data_in[y][x] == "#":
            continue
        if char == "S":
            start = (x, y, ">")
        if char == "E":
            end = (x, y, ">")
        for d in "<>v^":
            G.add_node((x, y, d))
            for d1 in "><v^":
                y1 = y
                x1 = x-1
                if x1 >= 0 and x1 < len(row) and data_in[y1][x1] != "#":
                    G.add_node((x1, y1, d1))
                    if d == ">" and d1 == ">":
                        G.add_edge((x, y, d), (x1, y1, d1), weight=1)
                    else:
                        if (d == "v" or d == "^") and d1 == "<":
                            G.add_edge((x, y, d), (x1, y1, d1), weight=1001)
                y1 = y
                x1 = x+1
                if x1 >= 0 and x1 < len(row) and data_in[y1][x1] != "#":
                    G.add_node((x1, y1, d1))
                    if d == "<" and d1 == "<":
                        G.add_edge((x, y, d), (x1, y1, d1), weight=1)
                    else:
                        if (d == "v" or d == "^") and d1 == ">":
                            G.add_edge((x, y, d), (x1, y1, d1), weight=1001)
                y1 = y-1
                x1 = x
                if y1 >= 0 and y1 < len(row) and data_in[y1][x1] != "#":
                    G.add_node((x1, y1, d1))
                    if d == "^" and d1 == "^":
                        G.add_edge((x, y, d), (x1, y1, d1), weight=1)
                    else:
                        if (d == "<" or d == ">") and d1 == "^":
                            G.add_edge((x, y, d), (x1, y1, d1), weight=1001)
                y1 = y+1
                x1 = x
                if y1 >= 0 and y1 < len(row) and data_in[y1][x1] != "#":
                    G.add_node((x1, y1, d1))
                    if d == "v" and d1 == "v":
                        G.add_edge((x, y, d), (x1, y1, d1), weight=1)
                    else:
                        if (d == "v" or d == "^") and d1 == "v":
                            G.add_edge((x, y, d), (x1, y1, d1), weight=1001)

dp = nx.dijkstra_path(G, start, (13, 1, ">"))
print(dp)
print(nx.path_weight(G, dp, "weight"))
