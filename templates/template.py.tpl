"""
[[CHALLENGE_YEAR]] day [[CHALLENGE_DAY]] challenge
https://adventofcode.com/[[CHALLENGE_YEAR]]/day/[[CHALLENGE_DAY]]
"""

import os

AOC_TOP_ENV = "AOC_TOP"

def challenge_part_1(challenge_input: list[str]) -> None:
    pass

def challenge_part_2(challenge_input: list[str]) -> None:
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
    challenge_part_1(challenge_input[:])
    print("-------------- PART 2 --------------")
    challenge_part_2(challenge_input[:])

if __name__ == "__main__":
    main()