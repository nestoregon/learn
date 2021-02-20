import os
import sys
from collections import namedtuple

calculated_results = {}

def calculate_points(bags, name):
    total_points = 0
    if name == "shiny gold":
        return 1
    if name in calculated_results:
        return calculated_results[name]

    for bag in bags:
        # find the bag with that name
        if bag[0] == name:
            dictionary = bag[1]
            if len(dictionary)==0:
                return 0

            for bag_name, value in dictionary.items():
                total_points += value * calculate_points(bags, bag_name)

    calculated_results[name] = total_points
    return total_points

def part_1():

    raw_rules = []
    bags = []
    with open("input7.txt") as fp:
        for line in fp:
            line = line.strip()
            raw_rules.append(line)

    print(raw_rules)
    bag_tuple = namedtuple("bag_tuple", "name contains")
    nary = {}

    for rule in raw_rules:
        container_dict = {}
        bag_name, content = rule.split(' bags contain ')
        content = content.split(', ')
        for bag in content:
            if bag == "no other bags.":
                continue
            words = bag.split(' ')
            number = int(words[0])
            name = words[1] + " " + words[2]
            container_dict[name] = number

        bags.append(bag_tuple(bag_name, container_dict))

    for item in bags:
        print(item)

    max = 0
    count = 0
    for bag in bags:
       score = calculate_points(bags, bag[0])
       print(bag[0], "score:", score)
       if score > 0:
           count += 1
       if score > max:
           max = score
    print("the count is", count-1)


def part_2():
    """ We need to count the nested bags withing 1 shinny bag """

    def count_bags(bags, name):
        total_count  = 0

        # just in case it was calculated before
        # calculated results is a global variable keeping track of the best results
        # already calculated
        if name in calculated_results:
            return calculated_results[name]

        for bag in bags:
            # find the bag with that name
            if bag.name == name:
                dictionary = bag.contains
                if len(dictionary)==0:
                    # this bag does not contain any other bags, so the result is just that one bag
                    return 1
                for bag_name, value in dictionary.items():
                    total_count += value * count_bags(bags, bag_name) # we have to take into account the bag that we're in

                total_count += 1 # don't forget to count the bag we're currently in!

        calculated_results[name] = total_count
        return total_count

    raw_rules = []
    bags = []
    with open("input7.txt") as fp:
        for line in fp:
            line = line.strip()
            raw_rules.append(line)

    bag_tuple = namedtuple("bag_tuple", "name contains")

    for rule in raw_rules:
        # from the raw rules create the bag_tuples and put them in an array
        container_dict = {}
        bag_name, content = rule.split(' bags contain ')
        content = content.split(', ')
        for bag in content:
            if bag == "no other bags.":
                continue
            words = bag.split(' ')
            number = int(words[0])
            name = words[1] + " " + words[2]
            container_dict[name] = number

        bags.append(bag_tuple(bag_name, container_dict))

    score = count_bags(bags, "shiny gold")
    without_shiny = score -1
    print(calculated_results)
    print("the score is", without_shiny)


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
