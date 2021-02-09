import os
import re

def part_1():
    all_lines = []
    valid_passports = 0
    n_passports = 0
    # required_fields = { 'byr':'', 'iyr':'', 'eyr':'', 'hgt':'', 'hcl':'', 'ecl':'', 'pid':'', 'cid':''}
    required_fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    dict_data = {}

    with open("input4.txt") as fp:
        for line in fp:
            line = line.strip()
            all_lines.append(line)

    for index, line in enumerate(all_lines):

        # it's a new passport now, gotta assess the previous one
        if line == '':
            n_passports+=1
            invalid = False
            print("passport number", n_passports)
            for field in required_fields:
                if field not in dict_data:
                    invalid = True

            if invalid == False:
                valid_passports+=1

            dict_data = {}

        # update dict
        else:
            pair_of_words = line.split(' ')
            for pair in pair_of_words:
                key, value = pair.split(':')
                dict_data[key] = value

    n_passports+=1
    invalid = False
    print("passport number", n_passports)
    for field in required_fields:
        if field not in dict_data:
            invalid = True

    if invalid == False:
        valid_passports+=1

    print("there are", valid_passports, "good passports")
    print("there are", n_passports, "total passports")


def part_2():
    all_lines = []
    valid_passports = 0
    n_passports = 0
    required_fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    dict_data = {}
    all_dicts = []

    with open("input4.txt") as fp:
        for line in fp:
            line = line.strip()
            all_lines.append(line)

    for line in all_lines:
        if line == '':
            n_passports+=1
            valid = True
            for field in required_fields:
                if field not in dict_data:
                    valid = False
            if valid:
                all_dicts.append(dict_data)
            # update!
            dict_data={}

        else:
            pairs = line.split(' ')
            for pair in pairs:
                key, value = pair.split(':')
                dict_data[key] = value

    valid = True
    n_passports+=1
    for field in required_fields:
        if field not in dict_data:
            valid = False
    if valid:
        all_dicts.append(dict_data)

    # now is time to test the restrictions
    for passport in all_dicts:
        # do a bunch of checks, otherwise, continue
        byr = passport['byr']
        iyr = passport['iyr']
        eyr = passport['eyr']
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']
        if len(byr) != 4 or int(byr) < 1920 or int(byr)> 2002:
            continue
        if len(iyr) != 4 or int(iyr) < 2010 or int(iyr)> 2020:
            continue
        if len(eyr) != 4 or int(eyr) < 2020 or int(eyr)> 2030:
            continue


        if hgt[-2:] != 'cm' and hgt[-2:] != 'in':
            continue
        if hgt[-2:] == 'cm':
            if int(hgt[:-2]) <150 or int(hgt[:-2]) > 193:
                continue
        if hgt[-2:] == 'in':
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                continue

        if hcl[0] != '#' or len(hcl) != 7:
            continue
        valid_characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
        for char in hcl[1:]:
            if char not in valid_characters:
                continue

        valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if ecl not in valid_eye_color:
            continue

        if len(pid) != 9 or not(pid.isnumeric()):
            continue

        # if it has reached the end it complies with all the criteria
        valid_passports+=1

    print("there are", valid_passports, "good passports")
    print("there are", n_passports, "total passports")


part_2()
