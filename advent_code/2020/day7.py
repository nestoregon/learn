import os
import sys

def part_1():

    raw_answers = []
    unique_answers_group=[]
    n_yes_total=0

    with open("input6.txt") as fp:
        string = ""
        for line in fp:
            line = line.strip()
            if line == "":
                raw_answers.append(string)
                string = ""
            else:
                string += line
        raw_answers.append(string)

    for group in raw_answers:
        for letter in group:
            if letter not in unique_answers_group:
                unique_answers_group.append(letter)

        n_yes_total+=len(unique_answers_group)
        unique_answers_group=[]

    print("total answers:", n_yes_total)

def part_2():
    groups = []
    group = []
    total_yes = 0

    with open("input6.txt") as fp:
        string = ""
        for line in fp:
            line = line.strip()
            if line == '':
                groups.append(group)
                group = []
            else:
                group.append(line)

    groups.append(group)
    group = []

    for group in groups:
        common_letters = group[0]
        for person in group:
            new_common = ""
            for letter in common_letters:
                if letter in person:
                    new_common += letter
            common_letters = new_common
        total_yes += len(common_letters)

    print(total_yes)


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
