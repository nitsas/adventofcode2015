#!/usr/bin/env python3
"""
Day 7
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/7

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


# bitwise operators we'll use:
# - a & b : a AND b
# - a | b : a OR b
# - ~ a : NOT a
# - a >> b : a RSHIFT b (places)
# - a << b : a LSHIFT b (places)


class BadInstructionError(Exception):
    def __init__(self, instruction):
        self.instruction = instruction
    
    def __str__(self):
        return str(instruction)


re_parts = {
    'not':   r'(?P<not>NOT)',
    'and':   r'(?P<and>AND)',
    'or':    r'(?P<or>OR)',
    'rshift': r'(?P<rshift>RSHIFT)',
    'lshift': r'(?P<lshift>LSHIFT)',
    'var_l':  r'(?P<var_l>[a-z]+)',
    'num_l':  r'(?P<num_l>[0-9]+)',
    'var_r':  r'(?P<var_r>[a-z]+)',
    'num_r':  r'(?P<num_r>[0-9]+)',
    'out':    r'(?P<out>[a-zA-Z]+)',
}

# more complex regex parts that build on top of the previous parts
re_parts['l_arg']  = r'(?P<l_arg>({var_l}|{num_l}))'.format(**re_parts)
re_parts['r_arg']  = r'(?P<r_arg>({var_r}|{num_r}))'.format(**re_parts)
re_parts['oper']   = r'({not}|{and}|{or}|{rshift}|{lshift})'.format(**re_parts)


class Instruction:
    matcher = re.compile(
        r'({l_arg} )?({oper} )?{r_arg} -> {out}'.format(**re_parts))
    
    def __init__(self, string):
        self.string = string
        match = self.matcher.match(string)
        if match:
            self.matches = self.get = match.group
            # - now `self.get('out')` will contain what's captured in the
            #   'out' group
            # - also, `self.match('and')` will be truthy if it's an AND
            #   instruction
        else:
            raise BadInstructionError()
    
    def is_not(self):
        return True if self.matches('not') else False
    
    def is_and(self):
        return True if self.matches('and') else False
    
    def is_or(self):
        return True if self.matches('or') else False
    
    def is_rshift(self):
        return True if self.matches('rshift') else False
    
    def is_lshift(self):
        return True if self.matches('lshift') else False
    
    def is_val_set(self):
        if (self.is_not() or self.is_and() or self.is_or() or
                self.is_lshift() or self.is_rshift()):
            return False
        else:
            return True
    
    def l_arg(self):
        return self.get('l_arg')
    
    def r_arg(self):
        return self.get('r_arg')
    
    def out(self):
        return self.get('out')


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


class InstructionResolver:
    def __init__(self, instructions):
        self.instructions = instructions
        self.ins_for = { ins.out(): ins for ins in self.instructions }
        self.val_for = {}
    
    def resolve(self, target):
        # if the target is actually a number in string format return it as int
        try:
            return int(target)
        except ValueError:
            pass
        # return the memoized value if one exists
        try:
            return self.val_for[target]
        except KeyError:
            pass
        # compute the result of the instruction
        ins = self.ins_for[target]
        if ins.is_val_set():
            result = self.resolve(ins.r_arg())
        elif ins.is_not():
            result = to_16_bit(~ self.resolve(ins.r_arg()))
        elif ins.is_and():
            result = to_16_bit(self.resolve(ins.l_arg()) &
                               self.resolve(ins.r_arg()))
        elif ins.is_or():
            result = to_16_bit(self.resolve(ins.l_arg()) |
                               self.resolve(ins.r_arg()))
        elif ins.is_lshift():
            result = to_16_bit(self.resolve(ins.l_arg()) <<
                               self.resolve(ins.r_arg()))
        elif ins.is_rshift():
            result = to_16_bit(self.resolve(ins.l_arg()) >>
                               self.resolve(ins.r_arg()))
        self.val_for[target] = result
        return result

# mask used to limit numbers to 16bit
mask = int('1111111111111111', 2)


def to_16_bit(number):
    # the bitwise AND limits `number` to have 1's at most where `mask` has 1's
    return number & mask


def solve(instructions, target='a'):
    instruction_resolver = InstructionResolver(instructions)
    result = instruction_resolver.resolve(target)
    return result


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
    # read the instructions
    with open(filename, 'r') as f:
        instructions = [Instruction(line) for line in f.read().splitlines()]
    # solve part 1
    signal_from_part_1 = solve(instructions, target='a')
    print('part 1:', signal_from_part_1)
    # alter the input of wire b to equal the signal we got on part 1
    for index, instruction in enumerate(instructions):
        if instruction.out() == 'b':
            break
    instructions[index] = Instruction('{} -> b'.format(signal_from_part_1))
    # solve part 2
    print('part 2:', solve(instructions, target='a'))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
