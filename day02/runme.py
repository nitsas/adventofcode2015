#!/usr/bin/env python3
"""
Day 2
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/2

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


# tried to be a bit python-beginner and programming-beginner friendly in this
# one but (a) it turned out ugly, and (b) it takes me more time, so I'll
# probably stop that coming the next day-puzzle


def solve_part_1(presents):
    total_needed_wrapping_paper = 0
    for present in presents:
        l, w, h = present
        areas_of_sides = (l*w, w*h, h*l)
        surface_area = 2 * sum(areas_of_sides)
        needed_wrapping_paper = surface_area + min(areas_of_sides)
        total_needed_wrapping_paper += needed_wrapping_paper
    return total_needed_wrapping_paper


def solve_part_2(presents):
    total_needed_ribbon = 0
    for present in presents:
        l, w, h = present
        perimeters_of_sides = (2 * (l + w), 2 * (w + h), 2 * (h + l))
        ribbon_needed_for_present = min(perimeters_of_sides)
        ribbon_needed_for_bow = l * w * h
        needed_ribbon = ribbon_needed_for_present + ribbon_needed_for_bow
        total_needed_ribbon += needed_ribbon
    return total_needed_ribbon


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
    # parse the file ...
    with open(filename, 'r') as file_:
        presents = list()
        for line in file_:
            sl, sw, sh = line.strip().split('x')
            present = (int(sl), int(sw), int(sh))
            presents.append(present)
        # one-liner (for the rubyists):
        # presents = list(tuple(map(int, (line.split('x')))) for line in file_)
    # ... solve part 1 ...
    print('part 1:', solve_part_1(presents))
    # ... and then part 2
    print('part 2:', solve_part_2(presents))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
