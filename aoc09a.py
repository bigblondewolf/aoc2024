#!/usr/bin/env python3

import aoc

data_in = [int(x) for x in aoc.read_input()[0]]
#data_in = [int(x) for x in aoc.read_example()[0]]
print(data_in)

is_in_file = True
disk_space = []
file_id = 0
for entry in data_in:
    if is_in_file:
        for i in range(entry):
            disk_space.append(file_id)
        file_id += 1
    else:
        for i in range(entry):
            disk_space.append(".")
    is_in_file = not is_in_file
print("".join([f"{x}" for x in disk_space]))

blank_idx = 0
file_idx = len(disk_space) - 1
disk_space_new = []
while blank_idx < len(disk_space):
    print(f"b: {blank_idx} f: {file_idx}")
    if blank_idx > file_idx:
        break
    while disk_space[blank_idx] != ".":
        if blank_idx == file_idx:
            break
        disk_space_new.append(disk_space[blank_idx])
        blank_idx += 1
        if blank_idx == len(disk_space):
            break
    while disk_space[file_idx] == ".":
        file_idx -= 1
        if file_idx < 0:
            break
    if disk_space[file_idx] != ".":
        disk_space_new.append(disk_space[file_idx])
    blank_idx += 1
    file_idx -= 1
    #print("".join([f"{x}" for x in disk_space_new]))
#print("".join([f"{x}" for x in disk_space_new]))

total = 0
for i in range(len(disk_space_new)):
    total += i * disk_space_new[i]
print(total)
