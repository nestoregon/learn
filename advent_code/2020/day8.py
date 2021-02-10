import os
import sys
from collections import namedtuple

def part_1():

    instructions = []
    with open("input8.txt") as fp:
        for line in fp:
            line = line.strip()
            instructions.append(line)


    line = 0
    repeat = False
    acc = 0
    executed = []
    executed.append(line)

    while not repeat:
        instruction = instructions[line]
        operator, number = instruction.split(' ')
        number = int(number)
        if operator == 'acc':
            acc += number
            line+=1
        elif operator == 'jmp':
            line += number
        else:
            line += 1


        if line in executed:
            repeat = True
        else:
            executed.append(line)
    print("the value of acc is", acc)


def part_2():

    instructions = []
    with open("input8.txt") as fp:
        for line in fp:
            line = line.strip()
            instructions.append(line)


    answer = 0
    end_for = False

    for index, line in enumerate(instructions):
        copy_instructions = instructions.copy()
        if line[:3] == 'jmp':
            copy_instructions[index] = copy_instructions[index].replace('jmp', 'nop')
        if line[:3] == 'nop':
            copy_instructions[index] = copy_instructions[index].replace('nop', 'jmp')

        line = 0
        repeat = False
        acc = 0
        executed = []
        executed.append(line)

        while not repeat:
            instruction = copy_instructions[line]
            operator, number = instruction.split(' ')
            number = int(number)
            if operator == 'acc':
                acc += number
                line+=1
            elif operator == 'jmp':
                line += number
            else:
                line += 1

            if line in executed:
                repeat = True
            else:
                executed.append(line)

            if line == len(instructions) -1:
                answer = acc
                end_for = True

            # exit if we found the answer
            if end_for == True:
                break

        if end_for == True:
            break

    print("the value of acc is", answer)


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

