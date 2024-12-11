#!/usr/bin/env python3

import aoc

data_in = aoc.read_input_aslist()[0]
#data_in = aoc.read_example_aslist()[0]

all_new_stones = []
def do_stone(stone, blinks_left):
    global all_new_stones
    stones_out = []
    if stone == "0":
        stones_out = ["1"]
    elif len(stone) % 2 == 0:
        stones_out = [f"{int(stone[:len(stone)//2])}",
                      f"{int(stone[len(stone)//2:])}"
                      ]
    else:
        stones_out = [f"{int(stone) * 2024}"]
    if blinks_left > 1:
        for new_stone in stones_out:
            do_stone(new_stone, blinks_left-1)
    else:
        all_new_stones.extend(stones_out)

for s in data_in:
    do_stone(s, 25)
print(len(all_new_stones))

