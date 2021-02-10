import os
import sys
from collections import namedtuple

def part_1():

    raw_input = []
    with open("input10.txt") as fp:
        for line in fp:
            line.strip()
            line = int(line)
            raw_input.append(line)

    raw_input.sort()
    print(raw_input)
    differences = {}
    number = 0
    # add +3 for the last one
    raw_input.append(raw_input[-1]+3)

    for i in raw_input:
        diff = i - number
        if diff not in differences:
            differences[diff] = 1
        else:
            differences[diff] += 1
        number = i # update

    print(differences)

    mult = differences[1] * differences[3]
    print(mult)


def part_2():

    raw_input = []
    with open("input10.txt") as fp:
        for line in fp:
            line.strip()
            line = int(line)
            raw_input.append(line)

    raw_input.sort()
    differences = {}
    number = 0
    # add +3 for the last one
    raw_input.append(raw_input[-1]+3)
    raw_input.insert(0, 0)
    print(raw_input)
    valid_jumps = [1,2,3]




if __name__ == "__main__":
    try:
        which_part = sys.argv[1]
        if which_part == '1':
            part_1()
        elif which_part == '2':
            part_2()
        else:
            print("arguments can only be 1 or 2")

    except IndexError:
        print("specify a part")
        print("example:")
        print("python3 dayX.py 2")

