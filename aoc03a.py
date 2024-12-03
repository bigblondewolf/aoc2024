#!/usr/bin/env python3

import re

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

rex_a = re.compile(r"mul\(\d+,\d+\)")

def do_mul(mul):
    args = mul[4:-1].split(",")
    return int(args[0]) * int(args[1])


total = 0
for row in data_in:
    allmul = rex_a.findall(row.strip())
    print(allmul)
    for mul in allmul:
        total += do_mul(mul)
print(total)

