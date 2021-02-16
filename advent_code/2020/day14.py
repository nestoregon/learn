import os
import sys
from collections import namedtuple

def part_1():
    mask = 0
    value = 0
    position = 0
    memory = {}
    to_save = ""

    with open("input14.txt") as fp:
        for line in fp:
            line = line.strip()
            words = line.split(" ")
            if words[0] == "mask":
                mask = words[2]
            else:
                position = words[0]
                position = int(position[4:-1])
                value = int(words[2])
                value_b = str(bin(value))
                value_b = value_b[2:]
                diff = 36 - len(value_b)
                value_b = diff*"0"+value_b
                to_save = ""
                for index, char in enumerate(value_b):
                    if mask[index] != 'X':
                        to_save+= mask[index]
                    else:
                        to_save+= value_b[index]

                # convert the binary string to int
                to_save = int(to_save, 2)
                memory[position] = to_save

    total = 0
    for key, value in memory.items():
        total += value

    print(total)


def part_2():

    mask = 0
    value = 0
    position = 0
    memory = {}
    to_save = ""

    with open("input14.txt") as fp:
        for line in fp:
            line = line.strip()
            words = line.split(" ")
            if words[0] == "mask":
                mask = words[2]
            else:
                position = words[0]
                position = int(position[4:-1])

                value = int(words[2])

                value_b = str(bin(position))
                value_b = value_b[2:]

                diff = 36 - len(value_b)
                value_b = diff*"0"+value_b
                to_save = ""

                for index, char in enumerate(value_b):

                    if mask[index] == 'X':
                        to_save+= 'X'

                    elif mask[index] == '0':
                        to_save+= value_b[index]
                    else:
                        to_save+= '1'

                count = 0
                indexes = []
                for index, char in enumerate(to_save):
                    if char == 'X':
                        indexes.append(index)
                        count += 1




                all_memories = []
                if count == 0:
                    all_memories.append(to_save)
                else:
                    for j in range(2**count):
                        j = str(bin(j))
                        j = j[2:]
                        diff = len(indexes) - len(j)
                        # make it binary with 3 things
                        j = diff*'0' + j

                        save_combintations = ""
                        index = 0

                        for char in to_save:
                            if char == "X":
                                save_combintations += j[index]
                                index += 1
                            else:
                                save_combintations+=char

                        all_memories.append(save_combintations)


                for index, memory_to in enumerate(all_memories):
                    # convert the binary string to int
                    memory_to = int(memory_to, 2)
                    memory[memory_to] = value
                    print("saving memory", memory_to, "with value", value)

    total = 0
    for key, value in memory.items():
        total += value

    print(total)



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

