"""
This file solves the third Advent of Code 2020 puzzle.
https://adventofcode.com/2020/day/3
"""
from sys import argv


def get_puzzle_input(path: str) -> list:
    """
    Parses the puzzle input, getting rid of newline characters
    :param path: The path to the input file
    :return: A str list, each element is a line from the input file.
    """
    with open(path) as inp:
        return [list(line.strip("\n")) for line in inp]


def count_collisions(right: int, down: int, aoc_map: list) -> int:
    """
    Given the trajectory, count the number of collisions (or close shaves) with trees.
    :param right: The number of spaces to the right moved in one time tick.
    :param down: The number of spaces down moved in one time tick.
    :param aoc_map: The map of the hill
    :return: The number of times one will encounter a tree on the way down.
    """
    map_length = len(aoc_map[0])
    map_height = len(aoc_map)

    count = 0
    j = right
    for i in range(down, map_height, down):
        j %= map_length
        if aoc_map[i][j] == "#":
            count += 1
        j += right

    return count


if __name__ == "__main__":
    right = int(argv[1])
    down = int(argv[2])
    in_path = argv[3]
    puzzle_input = get_puzzle_input(in_path)
    product = 1
    for i in [
        count_collisions(1, 1, puzzle_input),
        count_collisions(3, 1, puzzle_input),
        count_collisions(5, 1, puzzle_input),
        count_collisions(7, 1, puzzle_input),
        count_collisions(1, 2, puzzle_input),
    ]:
        product *= i
    print(product)
