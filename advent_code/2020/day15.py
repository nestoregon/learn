import os
import sys
from collections import namedtuple

input = [20,9,11,0,1,2]

def part_1():

    # there is a dictionary where the last time the number was spoken is saved
    # there is an array where every number said is saved
    # track of time (which is also the length of the array num_said
    last_time_spoken = {}
    numbers_said = []
    time = 0

    # initialize dict and array
    for number in input:
        time+=1
        last_time_spoken[number] = time
        numbers_said.append(number)


    # until iteration 2020
    while len(numbers_said) < 2020:

        time += 1 # update time
        # divide the array in two: last number said and the rest of the numbers
        last_num = numbers_said[-1]
        rest = numbers_said[:-1]

        # if the last number said is new, then we are going to say "0"
        if last_num not in rest:
            numbers_said.append(0) # say 0
            last_time_spoken[last_num] = time -1 # update the last time 6 was said
            # this is important, as we don't update the current number, otherwise
            # we cannot compare it to anything. Notice as well that the time is
            # substracted 1, so that it is the same as the previous number

        # if the number said is not new, we see how long ago it was said
        # the last time that number was said is updated, and we say the difference
        # out loud
        else:
            # how long ago was that number said?
            diff = time - last_time_spoken[last_num] -1
            last_time_spoken[last_num] = time-1 # update
            numbers_said.append(diff)


    # print the last number said, (position 2019), array length 2020
    print(numbers_said[-1])


def part_2():

    # in this part the code needs to be optimized, as the succession is too slow
    # we are asked to see the 30000000 number so we need to see if there is a pattern
    # turns out that you don't need the whole list of numbers, you only need the dictionary, which is less space i believe
    # could happen that the dictionary takes more space as well

    # there is a dictionary where the last time the number was spoken is saved
    # there is an array where every number said is saved
    # track of time (which is also the length of the array num_said
    last_time_spoken = {}
    time = 0

    # initialize dict and array
    for number in input:
        time+=1
        last_time_spoken[number] = time
        last_num = number


    # until iteration 2020
    while time < 30000000:

        time += 1 # update time

        # if the last num is not in dictionary
        if last_num not in last_time_spoken:
            last_time_spoken[last_num] = time -1 # update the last time prev number was said
            last_num = 0 # last number is now, duh, 0

        # if the number said is not new, we see how long ago it was said
        # the last time that number was said is updated, and we say the difference
        # out loud
        else:
            # how long ago was that number said?
            diff = time - last_time_spoken[last_num] -1
            last_time_spoken[last_num] = time-1 # update
            last_num = diff # the last num is the difference

    # print the last number said, (position 2019), array length 2020
    print(last_num)




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

