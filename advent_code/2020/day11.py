import os
import sys
from collections import namedtuple

def part_1():
    # the [] of map is the x, which is the vertical axis
    # the second [][] is the y, which is the horizontal axis

    map = []
    map_c = []
    with open("input11.txt") as fp:
        for line in fp:
            line = line.strip()
            line_array = []
            line_array_c = []
            for char in line:
                line_array.append(char)
                line_array_c.append(char)

            map.append(line_array)
            map_c.append(line_array_c)

    # lengths
    len_x = len(map)
    len_y = len(map[0])

    change_x = [1,1,0,-1,-1,-1,0,1]
    change_y = [0,1,1,1,0,-1,-1,-1]

    repeat = True
    iterations = 0

    while repeat:

        iterations += 1

        for i in range(len_x):
            for j in range(len_y):
                map_c[i][j] = map[i][j]

        changes = 0

        for iter_x in range(len_x):
            for iter_y in range(len_y):
                if map[iter_x][iter_y] == ".":
                    continue

                # iter_x, iter_y is the point
                # find count of all the points surrounding and put them in an array
                neighbours = []
                for direction in range(len(change_x)):
                    neighbour_x = change_x[direction] + iter_x
                    neighbour_y = change_y[direction] + iter_y

                    if neighbour_x >= 0 and neighbour_x < len_x and neighbour_y >= 0 and neighbour_y < len_y:
                        # if its withing reach
                        neighbours.append(map[neighbour_x][neighbour_y])

                # first rule
                if map[iter_x][iter_y] == "L" and "#" not in neighbours:
                    # print("change L -> #")
                    map_c[iter_x][iter_y] = "#"
                    changes += 1

                if map[iter_x][iter_y] == "#":
                    # count occupied
                    count = 0
                    for n in neighbours:
                        if n == "#":
                            count += 1

                    if count >= 4:
                        # print("change # -> L")
                        map_c[iter_x][iter_y] = "L"
                        changes += 1

        print("changes in iteration", iterations,":",changes)

        if changes == 0:
            repeat = False
        else:
            for i in range(len_x):
                for j in range(len_y):
                    map[i][j] = map_c[i][j]


        # copy map to map_c
        for iter_x in range(len_x):
            string = ""
            for iter_y in range(len_y):
                string += map[iter_x][iter_y]
                # map_c[iter_x][iter_y] = map[iter_x][iter_y]

            print(string)
        print()



    count_hashtags = 0
    for iter_x in range(len_x):
        for iter_y in range(len_y):
            if map[iter_x][iter_y] == "#":
                count_hashtags += 1

    print("number of hashtags", count_hashtags)
    print("iterations",iterations)


def part_2():

    # the [] of map is the x, which is the vertical axis
    # the second [][] is the y, which is the horizontal axis

    # original map & copy
    # i had problems copying the original map and the copy map
    map = []
    map_c = []
    with open("input11.txt") as fp:
        for line in fp:
            line = line.strip()
            line_array = []
            line_array_c = []
            for char in line:
                line_array.append(char)
                line_array_c.append(char)
            map.append(line_array)
            map_c.append(line_array_c)

    # lengths
    len_x = len(map)
    len_y = len(map[0])

    change_x = [1,1,0,-1,-1,-1,0,1]
    change_y = [0,1,1,1,0,-1,-1,-1]

    repeat = True
    iterations = 0

    while repeat:

        iterations += 1

        for i in range(len_x):
            for j in range(len_y):
                map_c[i][j] = map[i][j]

        changes = 0

        for iter_x in range(len_x):
            for iter_y in range(len_y):
                if map[iter_x][iter_y] == ".":
                    continue

                # iter_x, iter_y is the point
                # find count of all the points surrounding and put them in an array
                neighbours = []
                # find the neighbours in those directions!!! so if you find "." iter.
                # if "." iter
                # if out of bound do not append
                # if L or # append
                for direction in range(len(change_x)):
                    search = True
                    distance = 1

                    while search:
                        neighbour_x = distance*change_x[direction] + iter_x
                        neighbour_y = distance*change_y[direction] + iter_y

                        if neighbour_x >= 0 and neighbour_x < len_x and neighbour_y >= 0 and neighbour_y < len_y:
                            # if its withing reach
                            if map[neighbour_x][neighbour_y] == ".":
                                distance += 1
                            else:
                                neighbours.append(map[neighbour_x][neighbour_y])
                                search = False
                        else:
                            search = False

                # first rule
                if map[iter_x][iter_y] == "L" and "#" not in neighbours:
                    # print("change L -> #")
                    map_c[iter_x][iter_y] = "#"
                    changes += 1

                if map[iter_x][iter_y] == "#":
                    # count occupied
                    count = 0
                    for n in neighbours:
                        if n == "#":
                            count += 1

                    if count >= 5:
                        # print("change # -> L")
                        map_c[iter_x][iter_y] = "L"
                        changes += 1

        print("changes in iteration", iterations,":",changes)

        if changes == 0:
            repeat = False
        else:
            for i in range(len_x):
                for j in range(len_y):
                    map[i][j] = map_c[i][j]


        # print
        # for iter_x in range(len_x):
            # string = ""
            # for iter_y in range(len_y):
                # string += map[iter_x][iter_y]
                # # map_c[iter_x][iter_y] = map[iter_x][iter_y]

            # print(string)
        # print()



    count_hashtags = 0
    for iter_x in range(len_x):
        for iter_y in range(len_y):
            if map[iter_x][iter_y] == "#":
                count_hashtags += 1

    print("number of hashtags", count_hashtags)
    print("iterations",iterations)





if __name__ == "__main__":
    # try:
        which_part = sys.argv[1]
        if which_part == '1':
            part_1()
        elif which_part == '2':
            part_2()
        else:
            print("arguments can only be 1 or 2")

    # except IndexError:
        # print("specify a part")
        # print("example:")
        # print("python3 dayX.py 2")

