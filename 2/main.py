"""
This file solves the seond Advent of Code 2020 puzzle.
https://adventofcode.com/2020/day/2
"""


def parse_line(line: str) -> dict:
    """
    This function inelegantly gets all the parts of the password policy and password and stores
    them in a dictionary.
    :param line: The line containing the password policy and password to parse through.
    :return: A dict with all the parts of the line with specific keys.
    """
    ret_val = {}
    line = line.split(':')
    min_max = line[0][:-2].split('-')
    ret_val['min'] = int(min_max[0])
    ret_val['max'] = int(min_max[1])
    ret_val['char'] = line[0][-1]
    ret_val['data'] = line[1]

    return ret_val


def check_compliance(password: dict) -> bool:
    """
    Takes a line as returned by 'parse_line' and returns a boolean value for if the
    password is compliant with the policy.
    :param password: A line, freshly parsed by the 'parse_line' function.
    :return: True if the password is compliant.
    """
    # The following two (commented) lines solve part one of the day's puzzle.
    # n = password['data'].count(password['char'])
    # return password['min'] <= n <= password['max']
    interest = password['data'][password['min']] + password['data'][password['max']]
    return interest.count(password['char']) == 1


def parse_input(path: str) -> int:
    """
    Parses the puzzle input file and calculates how many lines are compliant with the policy.
    :param path: The path to the input puzzle file.
    :return:
    """
    with open(path) as inp:
        compliance_list = [check_compliance(parse_line(line)) for line in inp]
        return sum(compliance_list)


input_path = "puzzle_input.py"
print(parse_input(input_path))
