import os
import sys
from collections import namedtuple
import random


def node(rule, string, rules, let):
    """ This function goes through the rule and sees what kind of rule it is.
        Based on the kind of rule, we go one level deeper """

    # print(rule, string, let)
    if rule.kind == "nor1":
        ret, letters = node(rules[rule.x1], string, rules, let)
        return ret, letters

    elif rule.kind == "nor2":
        ret, l1 = node(rules[rule.x1], string, rules, let)
        if ret == True:
            ret, l2 = node(rules[rule.x2], string, rules, let+l1)
            if ret == True:
                return True, l1+l2

    elif rule.kind == "div2":
        ret1, letters = node(rules[rule.x1], string, rules, let)
        if ret1 == True:
            return True, letters
        # or
        ret1, letters = node(rules[rule.y1], string, rules, let)
        if ret1 == True:
            return True, letters

    elif rule.kind == "div3":
        solutions = {}

        ret, l1 = node(rules[rule.x1], string, rules, let)
        if ret == True:
            solutions[1] = (True, l1)
        # or
        ret, l1 = node(rules[rule.y1], string, rules, let)
        if ret == True:
            ret, l2 = node(rules[rule.y2], string, rules, let+l1)
            if ret == True:
                solutions[2] = (True, l1+l2)

        if len(solutions) == 0:
            return False, 0
        elif len(solutions) == 1:
            for key, value in solutions.items():
                return value
        else:
            number = random.randint(1,2)
            # print("div3", number)
            return solutions[number]
            # number = random.random()
            # if number < 0.5:
                # return solutions[1]
            # else:
                # return solutions[2]

    elif rule.kind == "div4":
        ret, l1 = node(rules[rule.x1], string, rules, let)
        if ret == True:
            ret, l2 = node(rules[rule.x2], string, rules, let+l1)
            if ret == True:
                return True, l1+l2

        ret, l1 = node(rules[rule.y1], string, rules, let)
        if ret == True:
            ret, l2 = node(rules[rule.y2], string, rules, let+l1)
            if ret == True:
                return True, l1+l2

    elif rule.kind == "div5":
        solutions = {}

        ret, l1 = node(rules[rule.x1], string, rules, let)
        if ret == True:
            ret, l2 = node(rules[rule.x2], string, rules, let+l1)
            if ret == True:
                solutions[1] = (True, l1+l2)
        # or
        ret, l1 = node(rules[rule.y1], string, rules, let)
        if ret == True:
            ret, l2 = node(rules[rule.y2], string, rules, let+l1)
            if ret == True:
                ret, l3 = node(rules[rule.extra], string, rules, let+l1+l2)
                if ret == True:
                    solutions[2] = (True, l1+l2+l3)

        if len(solutions) == 0:
            return False, 0
        elif len(solutions) == 1:
            for key, value in solutions.items():
                return value
        else:
            number = random.randint(1,2)
            print("div5", number)
            return solutions[number]

    elif rule.kind == "leaf":
        if len(string) > let:
            if string[let] == rule.x1:
                return True, 1
            # else:
                # print("--> no match", string, let, rule.x1)
        # else:
            # print("--> out of bounds", string, let, rule.x1)

    return False, 0


def part_1():
    rules = []
    check_words = []

    with open("input19.txt") as fp:
        what_to_append = "rules"
        for line in fp:
            line = line.strip()
            if line == "":
                what_to_append = "words"
            elif what_to_append == "rules":
                rules.append(line)

            elif what_to_append == "words":
                check_words.append(line)

    print(rules)
    print(check_words)

    # create a dictionary for the rules
    # for example rule 0: has blablabla
    # what should it contain?
    parents = []
    rule_node = namedtuple("rule_node", "x1 x2 y1 y2 kind")
    rules_dict = {}

    for rule in rules:
        print(rule)
        if rule[0] == "0":
            parents = rule[3:].split(" ")
        else:
            all = rule.split(" ")
            number = all[0][:-1]
            all.pop(0)
            kind = ""
            x1,x2,y1,y2 = 0,0,0,0

            if "|" in all:
                all.remove("|")
                length = len(all)
                if len(all) == 2:
                    kind = "div2"
                    x1 = all[0]
                    y1 = all[1]
                elif len(all) == 4:
                    kind = "div4"
                    x1 = all[0]
                    x2 = all[1]
                    y1 = all[2]
                    y2 = all[3]
            elif '"' in all[0]:
                kind = "leaf"
                x1 = all[0][1]
            else:
                if len(all) == 1:
                    kind = "nor1"
                    x1 = all[0]
                if len(all) == 2:
                    kind = "nor2"
                    x1 = all[0]
                    x2 = all[1]

            rules_dict[number] = rule_node(x1,x2,y1,y2,kind)

    for key, value in rules_dict.items():
        print(key, value)


    string = check_words[0]

    counter = 0
    for index, string in enumerate(check_words):
        print("")
        print(index, string)
        outcome = True
        for index2, rule in enumerate(parents):
            # print("index:",index2, "rule",rule)
            next_rule = rules_dict[rule]
            ret, letters = node(next_rule, string, rules_dict, 0)
            if ret == True:
                string = string[letters:]
            else:
                outcome = False
                # print("false")
                break
        print(outcome)


        if outcome == True and len(string) == 0:
            counter+=1

    print(counter)



def part_2():
    """ Part 2 was solved using probability """

    rules = []
    check_words = []

    with open("input19_2.txt") as fp:
        what_to_append = "rules"
        for line in fp:
            line = line.strip()
            if line == "":
                what_to_append = "words"
            elif what_to_append == "rules":
                rules.append(line)

            elif what_to_append == "words":
                check_words.append(line)

    print(rules)
    print(check_words)

    answer = []
    with open("input19_answers.txt") as fp:
        for line in fp:
            line = line.strip()
            answer.append(line)

    # create a dictionary for the rules
    # for example rule 0: has blablabla
    # what should it contain?
    parents = []
    rule_node = namedtuple("rule_node", "x1 x2 y1 y2 extra kind")
    rules_dict = {}

    for rule in rules:
        print(rule)
        if rule[0] == "0":
            parents = rule[3:].split(" ")
        else:
            all = rule.split(" ")
            number = all[0][:-1]
            all.pop(0)
            kind = ""
            x1,x2,y1,y2,extra = 0,0,0,0,0

            if "|" in all:
                all.remove("|")
                length = len(all)
                if len(all) == 2:
                    kind = "div2"
                    x1 = all[0]
                    y1 = all[1]
                elif len(all) == 3:
                    kind = "div3"
                    x1 = all[0]
                    y1 = all[1]
                    y2 = all[2]
                elif len(all) == 4:
                    kind = "div4"
                    x1 = all[0]
                    x2 = all[1]
                    y1 = all[2]
                    y2 = all[3]
                elif len(all) == 5:
                    kind = "div5"
                    x1 = all[0]
                    x2 = all[1]
                    y1 = all[2]
                    y2 = all[3]
                    extra = all[4]
            elif '"' in all[0]:
                kind = "leaf"
                x1 = all[0][1]
            else:
                if len(all) == 1:
                    kind = "nor1"
                    x1 = all[0]
                if len(all) == 2:
                    kind = "nor2"
                    x1 = all[0]
                    x2 = all[1]

            rules_dict[number] = rule_node(x1,x2,y1,y2,extra,kind)

    for key, value in rules_dict.items():
        print(key, value)


    string = check_words[0]

    max = 0
    for j in range(1):
        counter = 0
        for index, string in enumerate(check_words):
            original = string
            i = 0
            found = False
            while i<1000 and not found:
                i += 1
                random.seed(i)
                string = original

                outcome = True
                for index2, rule in enumerate(parents):
                    next_rule = rules_dict[rule]
                    ret, letters = node(next_rule, string, rules_dict, 0)
                    if ret == True:
                        string = string[letters:]
                    else:
                        outcome = False
                        break
                # if outcome == True and len(string) == 0:
                if outcome == True and len(string) == 0:
                    found = True
                    counter+=1
            if found:
                print(index,"True")
            else:
                print(index,"False")
            if counter > max:
                max = counter

    print("True:",max)




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

