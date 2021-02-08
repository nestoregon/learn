import os

def part_1():
    trees = 0
    x = 0 # this is not used given that we read per line
    y = 0
    with open("input3.txt") as fp:
        for line in fp:
            line = line.strip()
            position = y%len(line)
            print(line, position)
            if line[position] == "#":
                trees += 1
            y += 3 #update y

    print("there are", trees, "trees")

def part_2():

    paths=[[1,1],[1,3],[1,5],[1,7], [2,1]]
    trees = [0,0,0,0,0]
    map = []

    with open("input3.txt") as fp:
        for line in fp:
            line = line.strip()
            map.append(line)

    for i in range(len(paths)):
        print("This is the", i, "path")
        inc_x = paths[i][0]
        inc_y = paths[i][1]
        x = 0
        y = 0
        while x < len(map):
            new_y = y%len(map[0])
            print(new_y)
            if map[x][new_y] == "#":
               trees[i] += 1
            x += inc_x
            y += inc_y

    mult = 1
    print(trees)
    for tree in trees:
        mult*= tree

    print("there are", mult, "trees")

part_2()
