import os
import sys
from collections import namedtuple

def part_1():

    raw_instructions = []
    with open("input12.txt") as fp:
        for line in fp:
            line = line.strip()
            raw_instructions.append(line)

    # MAP
    # 
    #   N
    # W . E
    #   S
    # 
    # North-South will be the coordinate Y
    # West-East will be the coordinate X

    x = 0
    y = 0
    direction = 0

    # the direction stands for a regular circle
    # it should always be in absolute value
    # 0 -> East (x)
    # 90 -> North (y)
    # 180 -> West (-x)
    # 360 -> South (-y)

    for instruction in raw_instructions:
        task = instruction[0]
        number = int(instruction[1:])

        if task == "E":
            x += number
        elif task == "W":
            x -= number
        elif task == "N":
            y += number
        elif task == "S":
            y -= number
        elif task == "F":
            if direction == 0:
                x+= number
            elif direction == 90:
                y+= number
            elif direction == 180:
                x-= number
            elif direction == 270:
                y-= number
        elif task == "L":
            direction += number
            direction = direction%360
        elif task == "R":
            direction -= number
            direction += 360
            direction = direction%360

    print(x,y)
    print("answer", abs(x)+abs(y))


def part_2():

    raw_instructions = []
    with open("input12.txt") as fp:
        for line in fp:
            line = line.strip()
            raw_instructions.append(line)

    # MAP
    # 
    #   N
    # W . E
    #   S
    # 
    # North-South will be the coordinate Y
    # West-East will be the coordinate X

    x = 0
    y = 0
    direction = 0

    x_way = 10
    y_way = 1

    # the direction stands for a regular circle
    # it should always be in absolute value
    # 0 -> East (x)
    # 90 -> North (y)
    # 180 -> West (-x)
    # 360 -> South (-y)

    for instruction in raw_instructions:
        task = instruction[0]
        number = int(instruction[1:])

        if task == "E":
            x_way += number
        elif task == "W":
            x_way -= number
        elif task == "N":
            y_way += number
        elif task == "S":
            y_way -= number

        elif task == "F":
            x += x_way*number
            y += y_way*number

        elif task == "L" or task=="R":
            direction = number
            if task=="R":
                direction = -number + 360
            direction = direction%360

            if direction == 90:
                # print("rotate 90")
                cx = x_way
                cy = y_way
                x_way = -cy
                y_way = cx
            elif direction == 180:
                # print("rotate 180")
                y_way = -y_way
                x_way = -x_way
            elif direction == 270:
                # print("rotate 270")
                cx = x_way
                cy = y_way
                x_way = cy
                y_way = -cx

        print("------------")
        print("position x",x)
        print("position y",y)
        print("x_way, y_way",x_way, y_way)

    print(x,y)
    print("answer", abs(x)+abs(y))




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

