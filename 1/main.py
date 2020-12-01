from sys import argv
from copy import deepcopy


def get_input(input_path) -> list:
    with open(input_path) as puzzle_input:
        return [int(line) for line in puzzle_input]


def get_sum_pair(puzzle_input: list) -> int:
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input)):
            for k in range(len(puzzle_input)):
                if i != j != k:
                    if puzzle_input[i] + puzzle_input[j] + puzzle_input[k] == 2020:
                        return puzzle_input[i] * puzzle_input[j] * puzzle_input[k]


if __name__ == '__main__':
    puzzle_input = get_input(argv[1])
    print(get_sum_pair(puzzle_input))
