#!/usr/bin/env python3

import aoc

data_in_orig = aoc.read_input_aslist()
#data_in_orig = aoc.read_example_aslist()

data_in = [[(x, False) for x in y] for y in data_in_orig]
areas = []

xmax = len(data_in[0])
ymax = len(data_in)

def process_square(x, y, x_old, y_old):
    global data_in
    if data_in[y][x][1]:
        return 0, 0
    this_sym = data_in[y][x][0]
    data_in[y][x] = (this_sym, True)
    perim = 0
    area = 1
    for x1, y1 in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        if x1 < 0 or x1 >= xmax or y1 < 0 or y1 >= ymax:
            perim += 1
            continue
        if x1 == x_old and y1 == y_old:
            continue
        if data_in[y1][x1][0] == this_sym:
            child_res = process_square(x1, y1, x, y)
            area += child_res[0]
            perim += child_res[1]
        else:
            perim += 1
    return area, perim

total_cost = 0
for y in range(ymax):
    for x in range(xmax):
         sq_cost = process_square(x, y, -1, -1)
         total_cost += sq_cost[0] * sq_cost[1]
print(total_cost)
