#!/usr/bin/env python3
"""
Day 8
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/8

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
import re


def clean_up(line):
    # remove leading and trailing quotes
    line = line[1:-1]
    # convert escaped backslash character to 'a'
    line = line.replace(r'\\', 'a')
    # convert escaped double quote character to 'a'
    line = line.replace(r'\"', 'a')
    # convert any valid ascii code to 'a'
    line = re.sub(r'\\x[0-9a-fA-F]{2}', 'a', line)
    return line


def unclean_up(line):
    # replace leading and trailing quotes with 'aa' each
    line = 'aa' + line[1:-1] + 'aa'
    # add more a's to account for the extra leading and trailing quotes
    line = 'a' + line + 'a'
    # replace backslashes with 'aa'
    line = line.replace('\\', 'aa')
    # replace double quote characters with 'aa'
    line = line.replace('"', 'aa')
    return line


def solve_part_1(lines):
    total_code_length = sum(len(line) for line in lines)
    total_in_memory_length = sum(len(clean_up(line)) for line in lines)
    return total_code_length - total_in_memory_length


def solve_part_2(lines):
    total_code_length = sum(len(line) for line in lines)
    total_escaped_length = sum(len(unclean_up(line)) for line in lines)
    return total_escaped_length - total_code_length


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
        lines = file_.read().splitlines()
    print('part 1:', solve_part_1(lines))
    print('part 2:', solve_part_2(lines))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
