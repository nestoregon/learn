import os

numbers = []

with open("input1.txt") as fp:
    for line in fp:
        line = line.strip()
        numbers.append(int(line))

numbers.sort()
length_num = len(numbers)
mult = 0

def find_multiplication(numbers):
    for index, number_1 in enumerate(numbers):
        for i in range(length_num-index-1):
            number_2 = numbers[i+1]
            number_3 = 2020 - number_1 - number_2
            if number_3 in numbers:
                print("found!")
                mult = number_1 * number_2 * number_3
                print(number_1,  "*",  number_2,  "*",  number_3,"=", mult)
                return mult

find_multiplication(numbers)
