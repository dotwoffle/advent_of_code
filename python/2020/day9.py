"""
2020 day 9 challenge
https://adventofcode.com/2020/day/9
"""

import os

from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001
WINDOW_SIZE = 25

INVALID_SEQUENCE_NUMBER: int = None

def is_sum_of_two_numbers(number: int, other_numbers: list[int]) -> bool:

    sorted_numbers = sorted(other_numbers)
    high_idx = len(sorted_numbers) - 1
    low_idx = 0

    while True:

        result = sorted_numbers[low_idx] + sorted_numbers[high_idx]

        if result == number:
            return True

        if result > number:
            high_idx -= 1
        else:
            low_idx += 1

        if high_idx <= low_idx:
            return False
        
def find_block_that_sums_to_number(number: int, other_numbers: list[int]) -> list[int]:

    high_idx = len(other_numbers) - 1

    while high_idx >= 0:

        low_idx = high_idx - 2
        current_block = other_numbers[low_idx:high_idx]

        while sum(current_block) < number:
            low_idx -= 1
            current_block = other_numbers[low_idx:high_idx]

        if sum(current_block) == number:
            return current_block
        else:
            high_idx -= 1

    return []

def challenge_part_1(challenge_input: list[str]) -> int:
    
    global INVALID_SEQUENCE_NUMBER
    sequence = [int(line) for line in challenge_input]

    for idx, number in enumerate(sequence[WINDOW_SIZE:]):

        true_idx = idx + WINDOW_SIZE

        if not is_sum_of_two_numbers(number, sequence[(true_idx - WINDOW_SIZE):true_idx]):
            INVALID_SEQUENCE_NUMBER = number
            return number

def challenge_part_2(challenge_input: list[str]) -> int:

    sequence = [int(line) for line in challenge_input]
    sum_block = sorted(find_block_that_sums_to_number(INVALID_SEQUENCE_NUMBER, sequence))

    return sum_block[0] + sum_block[-1]

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day9.txt") as input_file:
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