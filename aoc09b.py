#!/usr/bin/env python3

import aoc

data_in = [int(x) for x in aoc.read_input()[0]]
#data_in = [int(x) for x in aoc.read_example()[0]]
#print(data_in)

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
#print("".join([f"{x}" for x in disk_space]))
print(f"Created disk space ({len(disk_space)})")

file_idx = len(disk_space)
files_moved = []
while file_idx > 0:
    if file_idx % 100 == 0:
        print(f"findex: {file_idx}")
    if disk_space[file_idx-1] == ".":
        file_idx -= 1
        continue
    if disk_space[file_idx-1] in files_moved:
        file_idx -= 1
        continue
    file_len = 1
    #print(f"fi: {file_idx}")
    while file_idx - file_len >= 0:
        if file_len > 100:
            break
        file_contents = disk_space[file_idx-file_len:file_idx]
        #print(f" fl: {file_len}: {file_contents}")
        if len(set(disk_space[file_idx-(file_len+1):file_idx])) > 1:
            break
        else:
            file_len += 1
    #print(f"fl final: {file_len}")
    for blank_idx in range(file_idx - file_len):
        if disk_space[blank_idx:blank_idx+file_len] == file_len * ["."]:
            disk_space[blank_idx:blank_idx+file_len] = file_contents
            disk_space[file_idx-file_len:file_idx] = file_len * ["."]
            files_moved.append(file_contents[0])
            break
    file_idx -= file_len
    #print("".join([f"{x}" for x in disk_space]))

print(disk_space)
print("Sorted")


total = 0
for i in range(len(disk_space)):
    if disk_space[i] != ".":
        total += i * disk_space[i]
print(total)
