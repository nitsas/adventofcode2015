#!/usr/bin/env python3
"""
Day 5
for Advent of Code 2015

Link to problem description:
http://adventofcode.com/day/5

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


re_three_vowels = re.compile(r'[aeiou].*?[aeiou].*?[aeiou]')
# break down
# - [aeiou] : match a vowel
# - .* : match anything (even nothing)
# - .*? : match anything (even nothing) but don't be greedy
#   (i.e. match 'xaaxexxxxu' up to the 'e' instead of up to the 'u')
# NOTE: the r before the string means this is a raw string
#   i.e. don't interpret backslashes etc as special characters


re_double_letter = re.compile(r'([a-zA-Z])\1')
# break down
# - [a-zA-Z] : match an ascii letter
# - (...) : capture (remember) string that matches the pattern in parentheses
# - \1 : match something that is equal to the 1st capture
# NOTE: the r before the string means this is a raw string
#   i.e. don't interpret backslashes etc as special characters


re_any_of_ab_cd_pq_xy = re.compile(r'ab|cd|pq|xy')
# NOTE: the r before the string means this is a raw string
#   i.e. don't interpret backslashes etc as special characters


def is_nice_string_part_1(string):
    # it should match the first two regexes but not the third one
    # NOTE: the search method searches the given string for a match
    if (re_three_vowels.search(string) and
            re_double_letter.search(string) and
            not re_any_of_ab_cd_pq_xy.search(string)):
        return True
    else:
        return False


re_letter_pair_twice_non_overlapping = re.compile(r'([a-zA-Z]{2}).*?\1')
# break down
# - [a-zA-Z]{2} : any pair of ascii letters
# - (...) : capture (remember) string that matches the pattern in parentheses
# - .*? : match anything (non-greedy)
# - \1 : match something that is equal to the 1st capture
# NOTE: the r before the string means this is a raw string
#   i.e. don't interpret backslashes etc as special characters


re_letter_repeat_with_one_letter_between = re.compile(r'([a-zA-Z])[a-zA-Z]\1')
# break down
# - ([a-zA-Z]) : match an ascii letter and capture (remember) it
# - [a-zA-Z] : match an ascii letter
# - \1 : match something that is equal to the 1st capture
# NOTE: the r before the string means this is a raw string
#   i.e. don't interpret backslashes etc as special characters


def is_nice_string_part_2(string):
    # it should match both regexes
    # NOTE: the search method searches the given string for a match
    if (re_letter_pair_twice_non_overlapping.search(string) and
            re_letter_repeat_with_one_letter_between.search(string)):
        return True
    else:
        return False


def solve(strings, is_nice_string):
    # run through all strings and count nice ones
    count = 0
    for string in strings:
        if is_nice_string(string):
            count += 1
    return count


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
        strings = file_.read().splitlines()
    print('part1:', solve(strings, is_nice_string_part_1))
    print('part2:', solve(strings, is_nice_string_part_2))
    return 0


# run function 'main' if this file is being run in the command line
# (vs being imported as a module)
if __name__ == "__main__":
    status = main()
    sys.exit(status)
