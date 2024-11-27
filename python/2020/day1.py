"""
2020 day 1 challenge
https://adventofcode.com/2020/day/1
"""

import os

from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001
MAGIC_NUMBER = 2020

def challenge_part_1(challenge_input: list[str]) -> int:
    
    entries = sorted([int(entry) for entry in challenge_input])
    high_idx = len(entries) - 1
    low_idx = 0

    while True:

        result = entries[low_idx] + entries[high_idx]

        if result == MAGIC_NUMBER:
            return entries[low_idx] * entries[high_idx]

        if result > MAGIC_NUMBER:
            high_idx -= 1
        else:
            low_idx += 1

def challenge_part_2(challenge_input: list[str]) -> int:
    
    entries = sorted([int(entry) for entry in challenge_input])
    high_idx = len(entries) - 1
    mid_idx = 0
    low_idx = 0
    cutoff = MAGIC_NUMBER - entries[high_idx]

    while entries[mid_idx] < cutoff:
        mid_idx += 1

    previous_cutoff_idx = mid_idx

    while True:

        result = entries[low_idx] + entries[mid_idx] + entries[high_idx]

        if result == MAGIC_NUMBER:
            return entries[low_idx] * entries[mid_idx] * entries[high_idx]
        
        if result > MAGIC_NUMBER:
            mid_idx -= 1
        else:
            low_idx += 1

        if mid_idx <= low_idx:

            high_idx -= 1
            mid_idx = previous_cutoff_idx
            previous_cutoff_idx = mid_idx
            low_idx = 0
            cutoff = MAGIC_NUMBER - entries[high_idx]

            while entries[mid_idx] < cutoff:
                mid_idx += 1

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day1.txt") as input_file:
        challenge_input = [line.strip() for line in input_file.readlines()]

    print("Starting challenge")
    print("-------------- PART 1 --------------")

    part_1_start_time = time_ns()

    print(challenge_part_1(challenge_input[:]))

    part_1_end_time = time_ns()

    print("-------------- PART 2 --------------")

    part_2_start_time = time_ns()

    print(challenge_part_2(challenge_input[:]))

    part_2_end_time = time_ns()

    print("--------------- DONE ---------------")
    print(f"Part 1 executed in {(part_1_end_time - part_1_start_time) * NS_TO_MS} ms")
    print(f"Part 2 executed in {(part_2_end_time - part_2_start_time) * NS_TO_MS} ms")

if __name__ == "__main__":
    main()