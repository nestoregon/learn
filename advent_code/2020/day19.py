import os
import sys
from collections import namedtuple


def node(rule, string, rules, let):

    print(rule, string, let)
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


    elif rule.kind == "leaf":
        if string[0] == rule.x1:
            return True, 1

    print("returning False at", rule, string, let)
    return False, 0


def part_1():
    rules = []
    check_words = []

    with open("input19_1.txt") as fp:
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
            parents = rules[0][3:].split(" ")
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

    for index, string in enumerate(check_words):
        print("")
        print(index, string)
        for index2, rule in enumerate(parents):
            print("index:",index2, "rule",rule)
            next_rule = rules_dict[rule]
            ret, letters = node(next_rule, string, rules_dict, 0)
            if ret == True:
                string = string[letters:]
            else:
                print("false")
                break


    dict_rules = {}

def part_2():
    pass



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
