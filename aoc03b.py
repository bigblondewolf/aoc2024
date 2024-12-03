#!/usr/bin/env python3

import re

import aoc

data_in = aoc.read_input()
#data_in = aoc.read_example()

def do_mul(mul):
    args = mul[4:-1].split(",")
    return int(args[0]) * int(args[1])


rex_a = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

total = 0
en = True
print(len(data_in))
for row in data_in:
    print(row.strip())
    allmul = rex_a.findall(row.strip())
    print(allmul)
    for mul in allmul:
        if mul == "do()":
            en = True
            print("True")
            continue
        if mul == "don't()":
            en = False
            print("False")
            continue
        if en:
            print(f"{mul}: {do_mul(mul)}")
            total += do_mul(mul)
        else:
            print(f"Skip {mul}")
print(total)
