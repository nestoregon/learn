import os
import sys
from collections import namedtuple

def part_1():
    time = 0
    bus_ids = []

    with open("input13.txt") as fp:
        count = 0
        for line in fp:
            count += 1
            line = line.strip()

            if count == 1:
                time = int(line)
            else:
                raw_ids = line.split(',')
                for ids in raw_ids:
                    if ids != 'x':
                        ids = int(ids)
                        bus_ids.append(ids)
    print(bus_ids)

    # calculate earliest D
    times_to_d = []
    time_aux = time

    for index, bus in enumerate(bus_ids):

        time_aux = time
        departed = False

        while not departed:
            departs = time_aux % bus
            if departs == 0:
                times_to_d.append(time_aux-time)
                departed = True
            else:
                time_aux += 1

    quickest_bus = times_to_d.index(min(times_to_d))
    print(times_to_d)
    print(bus_ids[quickest_bus] * times_to_d[quickest_bus])


def part_2():
    time = 0
    bus_info = []
    bus = namedtuple("bus", ("number delay"))
    print(bus)

    with open("input13_2.txt") as fp:
        count = 0
        counter = 0
        prev_id = 0

        # read the file and save everything as a named tuple
        for line in fp:
            count += 1
            line = line.strip()

            if count == 1:
                time = int(line)
            else:
                raw_ids = line.split(',')
                for ids in raw_ids:
                    if ids != 'x':
                        if prev_id != 0:
                            the_bus = bus(int(prev_id), counter)
                            bus_info.append(the_bus)
                            prev_id = int(ids)
                            counter = 0
                        else:
                            prev_id = ids
                    else:
                        counter += 1

                the_bus = bus(int(prev_id), counter)
                bus_info.append(the_bus)

        print(bus_info)

    bus_times = []
    count  = 0
    for i in bus_info:
        count += i.delay
        new_bus = bus(i.number, count)
        bus_times.append(new_bus)
        count += 1

    print(bus_times)


    # calculate the times such as the next bus is one minute (or the delay is also allowed)
    # should be multiples of the first one

    found = False


    max = 0
    max_i =0
    for index, i in enumerate(bus_times):
        if i.number >= max:
            max = i.number
            max_i = index
    print(max)

    time = 0
    time += bus_times[max_i].number -bus_times[max_i].delay
    final_time = 0

    print(time)
    print(max)

    # earliest time
    # number = 100_000_000_000_000
    # division = number // time
    # time = division * time
    # print(time)

    # cycle the biggest number, for example the place in which the biggest number and the second
    # biggest are the same, you'll go quicker
    print(bus_times)

    while not found:
        for bus in bus_times:
            new_time = time + bus.delay
            number = bus.number
            rest = new_time % number

            if rest != 0:
                break

            if bus_info[-1] == bus:
                found = True
                final_time = time

        time += bus_times[max_i].number

    print(final_time)















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

