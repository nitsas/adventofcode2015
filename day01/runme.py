#!/usr/bin/env python3
"""
Day 1
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/1

author:
Chris Nitsas
(nitsas)

language:
Python 3.4.2

date:
December, 2015

usage:
$ python3 runme.py input.txt
or
$ runme.py input.txt
(where input.txt is the input file and $ the prompt)
"""


import sys


char_to_floor_change = { '(': 1, ')': -1 }


def solve_part_1(input_):
    num_left_parentheses = input_.count('(')
    num_right_parentheses = input_.count(')')
    return num_left_parentheses - num_right_parentheses


def solve_part_2(input_):
    current_floor = 0
    for char_position, char in enumerate(input_, start=1):
        current_floor += char_to_floor_change[char]
        if current_floor == -1:
            return char_position


def main(filename=None):
    # get the input file
    if filename is None:
        if len(sys.argv) == 2:
            # get the filename from the command line
            filename = sys.argv[1]
        else:
            # no filename given
            print('Usage: runme.py input_file')
            return 1
    with open(filename, 'r') as file_:
        # read the file ...
        input_ = file_.read()
        # ... solve part 1 ...
        print('part 1:', solve_part_1(input_))
        # ... and part 2
        print('part 2:', solve_part_2(input_))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == '__main__':
    status = main()
    sys.exit(status)
