"""
This file is my solution to the first day of Advent Of Code 2020.
https://adventofcode.com/2020/day/1

Licensed under MIT license.
"""
from sys import argv


def get_input(input_path) -> list:
    """
    Get the Puzzle Input from file and convert it into a list of integers for processing.
    :param input_path: The path to the puzzle input file.
    :return: The contents of the puzzle input as a list of integers.
    """
    with open(input_path) as puzzle_input:
        return [int(line) for line in puzzle_input]


def get_sum_pair(puzzle_input: list) -> int:
    """
    Goes through the list of integers to find two (or three [spoilers]) integers which add up to
    2020.
    :param puzzle_input: The list of integers to search through.
    :return: The product of the two (or three [spoilers]) integers which add up to 2020.
    """
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input)):
            for k in range(len(puzzle_input)):
                if i != j != k:
                    if puzzle_input[i] + puzzle_input[j] + puzzle_input[k] == 2020:
                        return puzzle_input[i] * puzzle_input[j] * puzzle_input[k]
    return 0


if __name__ == "__main__":
    puzzle_in = get_input(argv[1])
    print(get_sum_pair(puzzle_in))
