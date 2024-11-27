"""
2020 day 2 challenge
https://adventofcode.com/2020/day/2
"""

import os

from time import time_ns
from typing import Callable

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001

class PasswordPolicy:

    def __init__(self, descriptor: str) -> None:
        
        components = descriptor.split(" ")
        requirements = components[0].split("-")

        self.REQUIRED_CHAR: str = components[1]
        self.FIRST_REQUIREMENT: int = int(requirements[0])
        self.SECOND_REQUIREMENT: int = int(requirements[1])

def get_num_valid_passwords(
        challenge_input: list[str],
        password_validator: Callable[[str, PasswordPolicy], bool]
) -> int:
    
    policies_and_passwords = list(map(
            lambda policy_and_password: (PasswordPolicy(policy_and_password[0]), policy_and_password[1]),
            [entry.split(": ") for entry in challenge_input]
    ))

    return len(list(filter(
            lambda policy_and_password: password_validator(policy_and_password[1], policy_and_password[0]),
            policies_and_passwords
    )))

def challenge_part_1(challenge_input: list[str]) -> int:
    
    def is_password_valid(password: str, policy: PasswordPolicy) -> bool:
        required_char_count = password.count(policy.REQUIRED_CHAR)
        return policy.FIRST_REQUIREMENT <= required_char_count <= policy.SECOND_REQUIREMENT

    return get_num_valid_passwords(challenge_input, is_password_valid)

def challenge_part_2(challenge_input: list[str]) -> int:
    
    def is_password_valid(password: str, policy: PasswordPolicy) -> bool:
        
        meets_first_requirement = policy.FIRST_REQUIREMENT <= len(password) and \
                password[policy.FIRST_REQUIREMENT - 1] == policy.REQUIRED_CHAR
        meets_second_requirement = policy.SECOND_REQUIREMENT <= len(password) and \
                password[policy.SECOND_REQUIREMENT - 1] == policy.REQUIRED_CHAR
        
        return meets_first_requirement != meets_second_requirement

    return get_num_valid_passwords(challenge_input, is_password_valid)

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day2.txt") as input_file:
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