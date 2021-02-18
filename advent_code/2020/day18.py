import os
import sys
from collections import namedtuple

def part_1():

    calculations = []
    with open("input18.txt") as fp:
        for line in fp:
            line = line.strip()
            calculations.append(line)

    def solve_operation(operation):
        while " " in operation:
            all = operation.split(" ")
            n1 = int(all[0])
            sign = all[1]
            n2 = int(all[2])

            result = 0
            if sign == "+":
                result = n1 + n2
            elif sign == "*":
                result = n1 * n2

            if len(all) == 3:
                return str(result)
            else:
                operation = str(result)+" " + " ".join(all[3:])

    def solve_parenthesis(string):
        """ Solve the parenthesis """
        level = 0
        max_level = 0
        par_index = 0
        close_index = 0

        for index, char in enumerate(string):
            if char == "(":
                par_index = index
            elif char == ")":
                close_index = index
                break

        parenthesis = solve_operation(string[par_index+1:close_index])
        string = string[:par_index]+parenthesis+string[close_index+1:]
        return string

    def solve_line(equation):
        while " " in equation:
            print(equation)

            if "(" in equation:
                equation = solve_parenthesis(equation)
            else:
                equation = solve_operation(equation)

        return(int(equation))

    result = 0
    for line in calculations:
        result += solve_line(line)

    print(result)




def part_2():

    calculations = []
    with open("input18.txt") as fp:
        for line in fp:
            line = line.strip()
            calculations.append(line)

    def solve_priority(operation):
        while " " in operation:
            operation = operation.strip()
            all = operation.split(" ")
            if len(all) == 1:
                return operation

            if "+" in operation:
                for index, thing in enumerate(all):
                    if thing == "+":
                        n1 = all[index-1]
                        n2 = all[index+1]
                        result = int(n2)+int(n1)
                        if len(all) == 3:
                            return str(result)

                        if index == 1:
                            operation = str(result) + " " + " ".join(all[index+2:])
                        elif index+1 == len(all) -1:
                            operation = " ".join(all[:index-1]) + " " + str(result)
                        else:
                            operation = " ".join(all[:index-1]) + " " + str(result) +" "+ " ".join(all[index+2:])
                            break

            else:
                n1 = all[0]
                n2 = all[2]
                result = int(n1) * int(n2)
                if len(all) == 3:
                    return str(result)
                operation = str(result) + " " + " ".join(all[3:])

        print(operation)


    def solve_parenthesis(string):
        """ Solve the parenthesis """
        level = 0
        max_level = 0
        par_index = 0
        close_index = 0

        for index, char in enumerate(string):
            if char == "(":
                par_index = index
            elif char == ")":
                close_index = index
                break

        parenthesis = solve_priority(string[par_index+1:close_index])
        string = string[:par_index]+parenthesis+string[close_index+1:]
        return string

    def solve_line(equation):
        while " " in equation:
            print(equation)

            if "(" in equation:
                equation = solve_parenthesis(equation)
            else:
                equation = solve_priority(equation)

        return(int(equation))

    result = 0
    for line in calculations:
        result += solve_line(line)
    print(result)

    # print(result)
    # string = "6 * 6 + 4 + 3 * 4"
    # string = solve_line(string)



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

