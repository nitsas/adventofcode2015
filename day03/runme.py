#!/usr/bin/env python3
"""
Day 3
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/3

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


# a class that represents positions (points) on the 2d grid
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, move):
        return Position(self.x + move.x, self.y + move.y)
    
    def __str__(self):
        return '{},{}'.format(self.x, self.y)


Move = Position


direction_to_move = {
    '^': Move(0, 1),
    '>': Move(1, 0),
    'v': Move(0, -1),
    '<': Move(-1, 0)
}


class Santa:
    def __init__(self, memory=None):
        # Santa's starting position
        self.current_position = Position(0, 0)
        # Santa's memory - he remembers every house (position) he's visited
        if memory is None:
            self.memory = set()
        else:
            self.memory = memory
        self.memory.add(str(self.current_position))
        # NOTE: I could do this using tuples instead of Positions, which
        #   would save me from having to store positions as strings in the
        #   memory, but I wanted to overload positions' "+" operator for fun
    
    def feed_directions(self, directions):
        for direction in directions:
            self.move(direction)
    
    def move(self, direction):
        self.current_position += direction_to_move[direction]
        self.memory.add(str(self.current_position))
    
    def number_of_distinct_houses_visited(self):
        return len(self.memory)


def solve_part_1(directions):
    santa = Santa()
    santa.feed_directions(directions)
    return santa.number_of_distinct_houses_visited()


def solve_part_2(directions):
    # each santa will use their smartphone to access a common memory-bank
    # and keep track of the visited houses there
    common_memory = set()
    santa = Santa(memory=common_memory)
    # robo-Santa works the same as Santa so we'll use the same class
    robo_santa = Santa(memory=common_memory)
    # split the directions in two parts
    # - take every other element
    directions_for_santa = directions[::2]
    # - take every other element starting from the second one
    directions_for_robo_santa = directions[1::2]
    # feed the santas directions
    santa.feed_directions(directions_for_santa)
    robo_santa.feed_directions(directions_for_robo_santa)
    return len(common_memory)


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
        directions = file_.read()
    # ... solve part 1 ...
    print('part 1:', solve_part_1(directions))
    # ... and part 2
    print('part 2:', solve_part_2(directions))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
