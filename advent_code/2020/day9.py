import os
import sys
from collections import namedtuple

def part_1():
    raw_input = []
    with open('input9.txt') as fp:
        for line in fp:
            line.strip()
            number = int(line)
            raw_input.append(number)

    for i in range(len(raw_input) - 25):
        pack_25 = raw_input[i:i+25]
        pack_25.sort()
        target = raw_input[i+25]

        # find if it can be the sum of two numbers
        found = False
        for number in pack_25:
            to_find = target - number
            if to_find in pack_25:
                found = True
            if found:
                break

        if found:
            continue

        print("hit")
        print(target)

def part_2():

    raw_input = []
    invalid_n = 0
    with open('input9.txt') as fp:
        for line in fp:
            line.strip()
            number = int(line)
            raw_input.append(number)

    for i in range(len(raw_input) - 25):
        pack_25 = raw_input[i:i+25]
        pack_25.sort()
        target = raw_input[i+25]

        # find if it can be the sum of two numbers
        found = False
        for number in pack_25:
            to_find = target - number
            if to_find in pack_25:
                found = True
            if found:
                break

        if found:
            continue

        invalid_n = target

    num1, num2 = 0, 0
    final_pack = []
    # find sum of invalid
    for i in range(len(raw_input)):
        # for every number
        for j in range(len(raw_input)-i-1):
            pack = raw_input[i:i+j+1]
            s = 0
            s = sum(pack)
            if s == invalid_n:
                pack.sort()
                num1 = pack[0]
                num2 = pack[-1]
                final_pack = pack.copy()
            if s > invalid_n:
                break
        if num1 > 0:
            break

    print("- num1:", num1)
    print("- num2:", num2)
    print("solution:", num1+num2)




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

