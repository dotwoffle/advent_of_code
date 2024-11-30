"""
2020 day 8 challenge
https://adventofcode.com/2020/day/8
"""

import os

from time import time_ns

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001

class ProgramExecutor:

    def __init__(self, program: list[str]) -> None:
        self._PROGRAM: list[str] = program
        self._accumulator: int = 0
        self._program_counter: int = 0

    def execute_next_instruction(self) -> None:

        instruction, action = self._PROGRAM[self._program_counter].split(" ")
        operator = action[0]
        argument = int(action[1:]) if operator == "+" else int(action)

        match instruction:
            case "acc":
                self._accumulator += argument
                self._program_counter += 1
            case "jmp":
                self._program_counter += argument
            case "nop":
                self._program_counter += 1
    
    def program_size(self) -> int:
        return len(self._PROGRAM)

    def program_finished(self) -> bool:
        return self._program_counter >= len(self._PROGRAM)

    def get_accumulator(self) -> int:
        return self._accumulator

    def get_program_counter(self) -> int:
        return self._program_counter

def get_all_possible_programs(challenge_input: str) -> list[ProgramExecutor]:

    def flip_instruction(instruction: str) -> str:

        if instruction.startswith("jmp"):
            return "nop" + instruction[3:]
        elif instruction.startswith("nop"):
            return "jmp" + instruction[3:]

    possible_programs = []

    for idx, instruction in enumerate(challenge_input):

        if instruction.startswith("nop") or instruction.startswith("jmp"):

            program_copy = challenge_input[:]
            program_copy[idx] = flip_instruction(instruction)

            possible_programs.append(ProgramExecutor(program_copy))

    return possible_programs

def detect_infinite_loop(executor: ProgramExecutor) -> bool:

    executed_instruction_counts = [0] * executor.program_size()

    while not executor.program_finished():

        executed_instruction_counts[executor.get_program_counter()] += 1

        if executed_instruction_counts[executor.get_program_counter()] > 1:
            return True

        executor.execute_next_instruction()

    return False

def challenge_part_1(challenge_input: list[str]) -> int:

    executor = ProgramExecutor(challenge_input)
    detect_infinite_loop(executor)
    
    return executor.get_accumulator()

def challenge_part_2(challenge_input: list[str]) -> int:
    for executor in get_all_possible_programs(challenge_input):
        if not detect_infinite_loop(executor):
            return executor.get_accumulator()

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day8.txt") as input_file:
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