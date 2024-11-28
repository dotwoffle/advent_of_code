"""
2020 day 5 challenge
https://adventofcode.com/2020/day/5
"""

import os

from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001
MAX_ROW = 127
MAX_COL = 7

def locate_seat(boarding_pass: str) -> tuple[int, int]:

    row_col_low = [0, 0]
    row_col_high = [MAX_ROW, MAX_COL]

    for instruction in boarding_pass:
        match instruction:
            case "F":
                row_col_high[0] = row_col_low[0] + ((((row_col_high[0] - row_col_low[0]) + 1) / 2) - 1)
            case "B":
                row_col_low[0] = row_col_high[0] - ((((row_col_high[0] - row_col_low[0]) + 1) / 2) - 1)
            case "L":
                row_col_high[1] = row_col_low[1] + ((((row_col_high[1] - row_col_low[1]) + 1) / 2) - 1)
            case "R":
                row_col_low[1] = row_col_high[1] - ((((row_col_high[1] - row_col_low[1]) + 1) / 2) - 1)

    if row_col_high[0] != row_col_low[0] or row_col_high[1] != row_col_low[1]:
        raise ValueError(f"Rows or columns did not match for input {boarding_pass}: {row_col_low} != {row_col_high}")

    return (row_col_low[0], row_col_low[1])

def calculate_seat_id(seat: tuple[int, int]) -> int:
    return (seat[0] * 8) + seat[1]

def challenge_part_1(challenge_input: list[str]) -> int:
    
    max_seat_id = -1

    for boarding_pass in challenge_input:

        seat_id = calculate_seat_id(locate_seat(boarding_pass))

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id

def challenge_part_2(challenge_input: list[str]) -> int:
    
    seat_ids = sorted(list(map(lambda boarding_pass: calculate_seat_id(locate_seat(boarding_pass)), challenge_input)))

    for current_id, next_id in zip(seat_ids, seat_ids[1:]):
        if next_id != current_id + 1:
            return current_id + 1

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day5.txt") as input_file:
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