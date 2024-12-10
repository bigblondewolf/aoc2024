#!/usr/bin/env python3

import collections

import networkx as nx

import aoc

Point = collections.namedtuple("Point", ["x", "y"])
data_in = aoc.read_input_aslist_parseints(has_spaces=False)
#data_in = aoc.read_example_aslist_parseints(has_spaces=False)

### With NetworkX
G = nx.DiGraph()
xmax = len(data_in[0])
ymax = len(data_in)
zeroes = []
nines = []

for y in range(ymax):
    for x in range(xmax):
        p = Point(x, y)
        if data_in[y][x] == 0:
            zeroes.append(p)
        if data_in[y][x] == 9:
            nines.append(p)
        if p not in G.nodes:
            G.add_node(p)
        for (x2, y2) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if( 0 <= x2
               and x2 < xmax
               and 0 <= y2
               and y2 < ymax
               ):
                if x != x2 or y != y2:
                    p2 = Point(x2, y2)
                    if p2 not in G.nodes:
                        G.add_node(p2)
                    if data_in[y2][x2] == data_in[y][x] + 1:
                        G.add_edge(p, p2)
print(len(zeroes))
total_rank = 0
for z in zeroes:
    rank = 0
    for n in nines:
        if len(list(nx.all_simple_paths(G, z, n))):
            rank += len(list(nx.all_simple_paths(G, z, n)))
    total_rank += rank
print(total_rank)

### With recursion
def rank(x, y):
    if data_in[y][x] == 9:
        return 1
    this_rank = 0
    for (x2, y2) in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
        if( x2 < 0
            or x2 >= xmax
            or y2 < 0
            or y2 >= ymax
            ):
            continue
        if data_in[y2][x2] != data_in[y][x] + 1:
            continue
        this_rank += rank(x2, y2)
    return this_rank


xmax = len(data_in[0])
ymax = len(data_in)

total_rank = 0
for y in range(ymax):
    for x in range(xmax):
        if data_in[y][x] == 0:
            total_rank += rank(x, y)
print(total_rank)

