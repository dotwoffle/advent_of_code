"""
2020 day 4 challenge
https://adventofcode.com/2020/day/4
"""

import os

from time import time_ns
from typing import Callable

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001

def read_passport_info(passport_info: list[str]) -> dict[str, str]:

    passport = {}

    for line in passport_info:

        passport_components = line.split(" ")

        for component in passport_components:
            (field, value) = component.split(":")
            passport[field] = value

    return passport

def count_valid_passports(challenge_input: str, validator: Callable[[dict[str, str]], bool]) -> int:

    valid_passport_count = 0
    current_passport_info = []

    for line in challenge_input:

        if line.strip() == "":
            valid_passport_count += 1 if validator(read_passport_info(current_passport_info)) else 0
            current_passport_info = []
        else:
            current_passport_info.append(line)

    valid_passport_count += 1 if validator(read_passport_info(current_passport_info)) else 0

    return valid_passport_count

def all_passport_fields_exist(passport: dict[str, str]) -> bool:
    all_passport_fields_exist.required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([field in passport.keys() for field in all_passport_fields_exist.required_fields])

def challenge_part_1(challenge_input: list[str]) -> int:
    return count_valid_passports(challenge_input, all_passport_fields_exist)

def challenge_part_2(challenge_input: list[str]) -> int:

    def verify_passport(passport: dict[str, str]) -> int:
        
        if not all_passport_fields_exist(passport):
            return False

        try:

            birth_year = int(passport["byr"])
            issue_year = int(passport["iyr"])
            expiration_year = int(passport["eyr"])
            height = passport["hgt"]
            hair_color = passport["hcl"]
            eye_color = passport["ecl"]
            id = passport["pid"]

            if not (1920 <= birth_year <= 2002):
                return False
            if not (2010 <= issue_year <= 2020):
                return False
            if not (2020 <= expiration_year <= 2030):
                return False

            if height[-2:] == "cm" and not (150 <= int(height[:-2]) <= 193):
                return False
            elif height[-2:] == "in" and not (59 <= int(height[:-2]) <= 76):
                return False
            elif height[-2:] != "cm" and height[-2:] != "in":
                return False

            if hair_color[0] != "#":
                return False
            if len(hair_color[1:]) != 6:
                return False
            
            int(hair_color[1:], 16) #only to verify number is hex, discard result

            if eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False

            if len(id) != 9:
                return False

            int(id) #only to verify number is valid, discard result

        except ValueError:
            return False

        return True

    return count_valid_passports(challenge_input, verify_passport)

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day4.txt") as input_file:
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