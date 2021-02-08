import os

def part_1():
    n_lines = 0
    counter = 0
    with open("input2.txt") as fp:
        for line in fp:
            n_lines += 1
            line = line.strip()
            constrains, password = line.split(':')
            numbers, letter = constrains.split(' ')
            num1, num2 = numbers.split('-')
            count_letter = password.count(letter)
            if count_letter >= int(num1) and count_letter<=int(num2):
                counter += 1

    print("there are", counter, "good passwords")

def part_2():
    n_lines = 0
    counter = 0
    with open("input2.txt") as fp:
        for line in fp:
            n_lines += 1
            line = line.strip()
            constrains, password = line.split(':')
            numbers, letter = constrains.split(' ')
            num1, num2 = numbers.split('-')
            password = password.strip()
            let1=password[int(num1)-1]
            let2=password[int(num2)-1]
            if (let1 == letter) ^ (let2 == letter):
                # if they are different it returns 1
                counter+=1

    print("there are", counter, "good passwords")

part_2()
