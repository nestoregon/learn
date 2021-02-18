import os
import sys
from collections import namedtuple


""" This problem was simple to solve. I decided to save the points into an array,
only keeping the active ones. Then I also count how many neighbours (the inactive ones)
are there (I use a dictionary to count how many times they have appeared. If its
exactly 3 I append that neigbour into the active array. Repeat the process for 6
iterations and solved.

Part 2 was literally 30 seconds, just adding w to everything. The program struggles a little

I also thought that it was not the best possible solution to include a huge grid, as you don't
know how big to make it. You could make it 15*15*15, given that the iterations are
6 and the original grid is 3*3*3 (first iter 5*5*5). This is, however, more cost eficient, given
that you only save the active cells, and you don't care about the inactives. Otherwise you could
run the algorithm for every single cell.
"""

def part_1():

    # map contains all the active points
    map = []
    point = namedtuple("point", "x y z")
    with open("input17.txt") as fp:
        x = 0
        y = 0
        for line in fp:
            line = line.strip()
            for index, char in enumerate(line):
                if char == "#":
                    add_point = point(x,index,0)
                    map.append(add_point)
            x+=1

    for i in range(6):
        print("iter",i, "active cells:", len(map))

        # a copy of the points that are occupied
        map_c = map.copy()
        map_in = {} # dictionary with the count of the empty neighbours that have
        # an active cell next to it

        # for every active cell
        for cell in map:
            count_active = 0

            # for every neighbour
            for x in range(-1,2):
                for y in range(-1,2):
                    for z in range(-1,2):
                        if x == 0 and y == 0 and z == 0:
                            continue

                        add_point = point(x+cell.x, y+cell.y, z+cell.z)

                        # if its occupied
                        if add_point in map:
                            count_active += 1

                        # if its inactive
                        else:
                            if add_point not in map_in:
                                map_in[add_point] = 1
                            else:
                                map_in[add_point] += 1


            # to still be active that cell needs exactly 2 or 3 active neighbours
            if count_active>3 or count_active < 2:
                map_c.remove(cell)

        # if inactive cells have 3 active cells next to it, add the active cell to the map
        for key, value in map_in.items():
            if value == 3:
                map_c.append(key)

        map = map_c.copy()

    print(len(map))






def part_2():

    # map contains all the active points
    map = []
    point = namedtuple("point", "x y z w")
    # read
    with open("input17.txt") as fp:
        x = 0
        y = 0
        for line in fp:
            line = line.strip()
            for index, char in enumerate(line):
                if char == "#":
                    add_point = point(x,index,0,0)
                    map.append(add_point)
            x+=1

    # 6 iterations of the problem
    for i in range(6):
        print("iter",i, "active cells:", len(map))

        # a copy of the points that are occupied
        map_c = map.copy()
        map_in = {} # dictionary with the count of the empty neighbours that have
        # an active cell next to it

        # for every active cell
        for cell in map:
            count_active = 0

            # for every neighbour
            for x in range(-1,2):
                for y in range(-1,2):
                    for z in range(-1,2):
                        for w in range(-1,2):
                            if x == 0 and y == 0 and z == 0 and w==0:
                                continue

                            add_point = point(x+cell.x, y+cell.y, z+cell.z, w+cell.w)

                            # if its occupied
                            if add_point in map:
                                count_active += 1

                            # if its inactive
                            else:
                                if add_point not in map_in:
                                    map_in[add_point] = 1
                                else:
                                    map_in[add_point] += 1


            # to still be active that cell needs exactly 2 or 3 active neighbours
            if count_active>3 or count_active < 2:
                map_c.remove(cell)

        # if inactive cells have 3 active cells next to it, add the active cell to the map
        for key, value in map_in.items():
            if value == 3:
                map_c.append(key)

        map = map_c.copy()

    print(len(map))




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

