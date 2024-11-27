"""
[[CHALLENGE_YEAR]] day [[CHALLENGE_DAY]] challenge
https://adventofcode.com/[[CHALLENGE_YEAR]]/day/[[CHALLENGE_DAY]]
"""

import os

from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001

def challenge_part_1(challenge_input: list[str]) -> int:
    pass

def challenge_part_2(challenge_input: list[str]) -> int:
    pass

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/[[CHALLENGE_YEAR]]/day[[CHALLENGE_DAY]].txt") as input_file:
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