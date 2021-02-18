import os
import sys
from collections import namedtuple

""" This one was one of my favorite problems! """

def part_1():
    fields = []
    my_ticket_raw = []
    nearby_tickets = []
    num_spaces = 0
    with open("input16.txt") as fp:
        for line in fp:
            line = line.strip()
            if line == "":
                num_spaces+=1
            elif num_spaces == 0:
                fields.append(line)
            elif num_spaces == 1:
                if line != "your ticket:":
                    my_ticket_raw.append(line)

            elif num_spaces == 2:
                if line != "nearby tickets:":
                    nearby_tickets.append(line)

    # it stands for processed fields
    pf = []
    ordered_data = namedtuple("ordered_data", "name n1 n2 n3 n4")
    for field in fields:
        name, condition = field.split(": ",1)
        c1, c2 = condition.split(" or ")
        n1, n2 = c1.split("-")
        n3, n4 = c2.split("-")
        print(name, n1,n2,n3,n4)
        pf.append(ordered_data(name, int(n1),int(n2),int(n3),int(n4)))
    print(pf)

    my_ticket = []
    str_my_ticket = my_ticket_raw[0]
    my_ticket = str_my_ticket.split(',')
    for index, ticket in enumerate(my_ticket):
        my_ticket[index] = int(ticket)
    print(my_ticket)

    # test my ticket
    for index, field in enumerate(my_ticket):
        n1, n2, n3, n4 = pf[index].n1, pf[index].n2, pf[index].n3, pf[index].n4
        if (field >= n1 and field <= n2) or (field >= n3 and field <= n4):
            print("okay")
        else:
            print("not okay")

    error = 0
    # test the rest of the tickets
    for ticket in nearby_tickets:
        fields = ticket.split(',')
        for index, field in enumerate(fields):
            number = int(field)
            iter = 0
            for constrain in pf:
                n1, n2, n3, n4 = constrain.n1, constrain.n2, constrain.n3, constrain.n4
                if (number >= n1 and number <= n2) or (number >= n3 and number <= n4):
                    break
                else:
                    iter += 1

            if iter == len(pf):
                error+= number

    print(error)





def part_2():
    fields = []
    my_ticket_raw = []
    nearby_tickets = []
    num_spaces = 0
    with open("input16.txt") as fp:
        for line in fp:
            line = line.strip()
            if line == "":
                num_spaces+=1
            elif num_spaces == 0:
                fields.append(line)
            elif num_spaces == 1:
                if line != "your ticket:":
                    my_ticket_raw.append(line)

            elif num_spaces == 2:
                if line != "nearby tickets:":
                    nearby_tickets.append(line)

    # it stands for processed fields
    pf = []
    ordered_data = namedtuple("ordered_data", "name n1 n2 n3 n4")
    for field in fields:
        name, condition = field.split(": ",1)
        c1, c2 = condition.split(" or ")
        n1, n2 = c1.split("-")
        n3, n4 = c2.split("-")
        pf.append(ordered_data(name, int(n1),int(n2),int(n3),int(n4)))

    my_ticket = []
    str_my_ticket = my_ticket_raw[0]
    my_ticket = str_my_ticket.split(',')
    for index, ticket in enumerate(my_ticket):
        my_ticket[index] = int(ticket)


    # remove non_valid tickets!
    error = 0
    valid_nearby = []
    for ticket in nearby_tickets:
        discard_ticket = False
        fields = ticket.split(',')
        for index, field in enumerate(fields):
            number = int(field)
            iter = 0
            for constrain in pf:
                n1, n2, n3, n4 = constrain.n1, constrain.n2, constrain.n3, constrain.n4
                if (number >= n1 and number <= n2) or (number >= n3 and number <= n4):
                    break
                else:
                    iter += 1

            if iter == len(pf):
                error+= number
                discard_ticket = True

        if not discard_ticket:
            valid_nearby.append(ticket)

    print("tickets filtered =", len(nearby_tickets) - len(valid_nearby))

    # initialize posibilities of valid_tickets
    # every column can be every single column in pf
    dict_possibilities = {}
    for i in range(len(pf)):
        array = []
        for j in range(len(pf)):
            array.append(j)
        dict_possibilities[i] = array

    print(dict_possibilities)
    print("this means that every single TICKET column can be every single ticket FIELD")


    # so for every valid ticket
    for ticket in valid_nearby:
        # get the fields. They are all the same per ticket nearby
        fields = ticket.split(",")
        # iterate through all the fields (columns)
        for index, field in enumerate(fields):
            print(index)
            # cast it so that is int of course
            field = int(field)
            iter = 0
            for index_2, constrain in enumerate(pf):
                n1, n2, n3, n4 = constrain.n1, constrain.n2, constrain.n3, constrain.n4
                if (field >= n1 and field <= n2) or (field >= n3 and field <= n4):
                    iter += 1
                else:
                    print("remove")
                    if index_2 in dict_possibilities[index]:
                        dict_possibilities[index].remove(index_2)


    # now we still have a lot of possibilities. Thankfully, we can delete them
    # to do this we need to find a spot where there is only one posiblity, and delete
    # that number from the rest of the numbers
    # do so until every column has only one number associated to it

    count = 0
    deleted = False
    while count<20 :
        count = 0
        for key, value in dict_possibilities.items():
            print(key, value)
            if len(value) == 1:
                remove_all = value[0]
                count+=1
                for key_2, value_2 in dict_possibilities.items():
                    if key_2 != key:
                        if remove_all in dict_possibilities[key_2]:
                            print("removing", remove_all, "from", dict_possibilities[key_2], "with key", key_2)
                            dict_possibilities[key_2].remove(remove_all)
                            deleted = True

    print("results")
    print("-"*20)
    for key, value in dict_possibilities.items():
        print(key, value)
    print("my ticket")
    print("-"*20)
    print(my_ticket)

    # now we need to find the sum of 
    sum = 1
    for number in range(6):
        for key, value in dict_possibilities.items():
            value = value[0]
            if value == number:
                print(key)
                sum *= my_ticket[key]

    print(sum)





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

