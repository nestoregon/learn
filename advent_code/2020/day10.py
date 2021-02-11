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

    # there are connections where we can calculate the different posibilities
    # of connecting. These "islands" are separated by 3. Everytime there is a
    # 3 we reset a counter and whenever we encounter a 3 we append that to an
    # array in order to see how many points of 1 does the island have, therefore
    # calculating the connections separatedly and then multiplying

    counter = 0
    islands = []

    for i in range(len(raw_input)-1):

        diff = raw_input[i+1] - raw_input[i]
        if diff not in differences:
            differences[diff] = 1
        else:
            differences[diff] += 1

        if diff == 3:
            if counter == 0:
                counter = 0
            else:
                islands.append(counter)
                counter = 0

        if diff == 1:
            counter += 1

    print(islands)

    # an island that has 1 connections (X*X) can only have 1 possibilities
    # so an island that has 2 islands (X*X*X) can have (2) possibilities
    # an island that has 3 islands (X*X*X*X) has 1, 2, 3, 4 (4)
    # an island that has 4 islands X*X*X*X*X has (1+1+1+1) (1+1+2), (1+2+1), (2+2), (3+1), (1+3) (5)

    match_possibilities = {1:1, 2:2, 3:4, 4:5}

    mult = 1

    for i in islands:
        mult*= match_possibilities[i]

    print(mult)





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

