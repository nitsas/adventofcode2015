#!/usr/bin/env python3
"""
Day X
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/X

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


# did this using classes just for the fun of it


class BadInstructionError(Exception):
    def __init__(self, instruction):
        self.instruction = instruction
    
    def __str__(self):
        return str(instruction)


class Instruction:
    # (a class variable)
    # regex for breaking down an instruction-string
    re_instruction = re.compile(r'(?P<command>toggle|turn on|turn off) ' +
                                r'(?P<left>\d+),(?P<down>\d+)' +
                                r' through ' +
                                r'(?P<right>\d+),(?P<up>\d+)')
    
    def __init__(self, string):
        match = self.re_instruction.match(string)
        if match:
            self.command = match.group('command')
            self.left = int(match.group('left'))
            self.right = int(match.group('right'))
            self.down = int(match.group('down'))
            self.up = int(match.group('up'))
        else:
            raise BadInstructionError(string)


class Grid:
    def __init__(self):
        self._grid = [[0] * 1000 for i in range(1000)]
    
    def toggle(self, row, col):
        self._grid[row][col] = int(not self._grid[row][col])
    
    def turn_on(self, row, col):
        self._grid[row][col] = 1
    
    def turn_off(self, row, col):
        self._grid[row][col] = 0
    
    def increase_brightness_by_1(self, row, col):
        self._grid[row][col] += 1
    
    def decrease_brightness_by_1(self, row, col):
        self._grid[row][col] = max(self._grid[row][col] - 1, 0)
    
    def increase_brightness_by_2(self, row, col):
        self._grid[row][col] += 2
    
    def total_brightness(self):
        return sum(sum(row) for row in self._grid)


class InstructionApplier:
    def __init__(self, grid, command_interpreter):
        self._grid = grid
        self.interpreter = command_interpreter
    
    def apply_all(self, instructions):
        for instruction in instructions:
            self.apply_(instruction)
    
    def apply_(self, ins):
        grid_method_name = self.interpreter(ins.command)
        for row in range(ins.down, ins.up + 1):
            for col in range(ins.left, ins.right + 1):
                getattr(self._grid, grid_method_name)(row, col)


def interpret_command_in_english(command):
    if command == 'toggle':
        grid_method_name = 'toggle'
    elif command == 'turn on':
        grid_method_name = 'turn_on'
    elif command == 'turn off':
        grid_method_name = 'turn_off'
    return grid_method_name


def interpret_command_in_elvish(command):
    if command == 'toggle':
        grid_method_name = 'increase_brightness_by_2'
    elif command == 'turn on':
        grid_method_name = 'increase_brightness_by_1'
    elif command == 'turn off':
        grid_method_name = 'decrease_brightness_by_1'
    return grid_method_name


def solve(instructions, command_interpreter):
    grid = Grid()
    instruction_applier = InstructionApplier(grid, command_interpreter)
    instruction_applier.apply_all(instructions)
    return grid.total_brightness()


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
    with open(filename, 'r') as f:
        instructions = [Instruction(line) for line in f.read().splitlines()]
    print('part 1:', solve(instructions, interpret_command_in_english))
    print('part 2:', solve(instructions, interpret_command_in_elvish))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
