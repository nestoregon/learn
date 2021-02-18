import os
import sys
from collections import namedtuple

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
    rule_node = namedtuple("rule_node", "n1 n2 n3 n4 is_leaf")
    rules_dict = {}

    print(parents)
    for rule in rules:
        print(rule)
        if rule[0] == 0:
            parents = rules[0][3:].split(" ")
        else:
            all = rule.split(" ")
            number = all[0][:-1]
            all.pop(0)
            is_leaf = False

            if '"' in rule:
                n1 = all[0]
                is_leaf = True
                rules_dict[number] = rule_node(n1,0,0,0,is_leaf)
            elif "|" in all:
                # process the rule
                all.remove("|")
                n1, n2, n3, n4 = all
                rules_dict[number] = rule_node(n1,n2,n3,n4,is_leaf)
            elif len(all) == 2:
                n1, n2 = all
                rules_dict[number] = rule_node(n1,n2,0,0,is_leaf)

            elif len(all) == 1:
                n1 = all
                rules_dict[number] = rule_node(n1,0,0,0,is_leaf)



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

