"""
2020 day 7 challenge
https://adventofcode.com/2020/day/7
"""

import os

from time import time_ns

BagMap = dict[str, list[tuple[str, int]]]

AOC_TOP_ENV = "AOC_TOP"
NS_TO_MS = 0.000001
MAGIC_BAG_TYPE = "shiny gold"
BAG_TYPES_TO_CONTAINABLE_BAGS: BagMap = None

def load_bag_info(challenge_input: list[str]) -> BagMap:

    bag_types_to_containable_bags = {}

    for line in challenge_input:

        bag_type_string, containable_bags_string = line.split(" contain ")
        bag_type = " ".join(bag_type_string.split(" ")[:-1])

        if containable_bags_string == "no other bags.":
            bag_types_to_containable_bags[bag_type] = []
            continue

        containable_bags = [(
                " ".join(bag.split(" ")[1:-1]),
                int(bag.split(" ")[0])
        ) for bag in containable_bags_string.split(", ")]
        bag_types_to_containable_bags[bag_type] = containable_bags
    
    return bag_types_to_containable_bags

def bag_can_contain(bag_type: str, contained_bag_type: str) -> bool:

    for containable_bag_type, _ in BAG_TYPES_TO_CONTAINABLE_BAGS[bag_type]:
        if containable_bag_type == contained_bag_type or bag_can_contain(containable_bag_type, contained_bag_type):
            return True
        
    return False

def calculate_required_num_contained_bags(bag_type: str) -> int:

    required_bags = 0

    for contained_bag_type, contained_bag_count in BAG_TYPES_TO_CONTAINABLE_BAGS[bag_type]:

        required_sub_bags = calculate_required_num_contained_bags(contained_bag_type)

        if required_sub_bags == 0:
            required_bags += contained_bag_count
        else:
            required_bags += (required_sub_bags * contained_bag_count) + contained_bag_count

    return required_bags

def challenge_part_1(challenge_input: list[str]) -> int:
    
    bag_type_count = 0

    for bag_type in BAG_TYPES_TO_CONTAINABLE_BAGS.keys():
        bag_type_count += 1 if bag_can_contain(bag_type, MAGIC_BAG_TYPE) else 0

    return bag_type_count

def challenge_part_2(challenge_input: list[str]) -> int:
    return calculate_required_num_contained_bags(MAGIC_BAG_TYPE)

def main() -> None:

    try:
        aoc_top = os.environ[AOC_TOP_ENV]
    except KeyError:
        print(f"{AOC_TOP_ENV} is not set in the environment. Did you source?")
        exit(1)

    with open(f"{aoc_top}/inputs/2020/day7.txt") as input_file:
        challenge_input = [line.strip() for line in input_file.readlines()]

    global BAG_TYPES_TO_CONTAINABLE_BAGS
    BAG_TYPES_TO_CONTAINABLE_BAGS = load_bag_info(challenge_input)

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