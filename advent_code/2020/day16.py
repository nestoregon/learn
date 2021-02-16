import os
import sys
from collections import namedtuple

def part_1():
    pass

def part_2():
    pass



if __name__ == "__main__":
    if len(sys.argv) == 2:
        which_part = sys.argv[1]
        if which_part == '1':
            part_1()
        elif which_part == '2':
            part_2()
        else:
            print("arguments can only be 1 or 2")

    else:
        print("specify a part")
        print("example:")
        print("python3 dayX.py 2")

