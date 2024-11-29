"""
2020 day 6 challenge
https://adventofcode.com/2020/day/6
"""

import os

from common.aocutil import split_input_groups
from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001
ASCII_LOWER_A = 97
NUM_QUESTIONS = 26

def challenge_part_1(challenge_input: list[str]) -> int:
    
    answer_sum = 0

    for group in split_input_groups(challenge_input):

        group_answer_count = [0] * NUM_QUESTIONS

        for answer in "".join(group):
            group_answer_count[ord(answer) - ASCII_LOWER_A] += 1

        answer_sum += len(list(filter(lambda count: count > 0, group_answer_count)))

    return answer_sum

def challenge_part_2(challenge_input: list[str]) -> int:
    
    answer_sum = 0

    for group in split_input_groups(challenge_input):

        group_answer_count = [0] * NUM_QUESTIONS

        for answer in "".join(group):
            group_answer_count[ord(answer) - ASCII_LOWER_A] += 1

        answer_sum += len(list(filter(lambda count: count == len(group), group_answer_count)))

    return answer_sum

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day6.txt") as input_file:
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