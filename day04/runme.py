#!/usr/bin/env python3
"""
Day 4
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/4

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
import hashlib


def md5_of(string_):
    return hashlib.md5(string_.encode('utf-8')).hexdigest()


def solve_part_1(key):
    five_zeros = '00000'
    num = 1
    while md5_of(key + str(num))[:5] != five_zeros:
        num += 1
    return num


def solve_part_2(key, start_at=1):
    six_zeros = '000000'
    num = start_at
    while md5_of(key + str(num))[:6] != six_zeros:
        num += 1
    return num


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
        secret_key = file_.read().strip()
    answer_to_part_1 = solve_part_1(secret_key)
    print('part 1:', answer_to_part_1)
    print('part 2:', solve_part_2(secret_key, start_at=answer_to_part_1))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
