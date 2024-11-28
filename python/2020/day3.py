"""
2020 day 3 challenge
https://adventofcode.com/2020/day/3
"""

import os

from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001

def count_trees_in_slope(grid: list[str], right_step: int, down_step: int = 1) -> int:

    tree_count = 0
    current_step = 0

    for y in range(0, len(grid), down_step):
        if grid[y][(current_step * right_step) % len(grid[0])] == "#":
            tree_count += 1
        current_step += 1

    return tree_count

def challenge_part_1(challenge_input: list[str]) -> int:
    return count_trees_in_slope(challenge_input, 3)

def challenge_part_2(challenge_input: list[str]) -> int:
    
    tree_count_product = 1
    slopes_to_check = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    for slope in slopes_to_check:
        tree_count_product *= count_trees_in_slope(challenge_input, slope[0], slope[1])

    return tree_count_product

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day3.txt") as input_file:
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