import os
import sys
from collections import namedtuple
from operator import attrgetter

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

    with open("input13.txt") as fp:
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
        new_bus = bus(i.number, count)
        bus_times.append(new_bus)
        count += 1
        count += i.delay

    print(bus_times)


    # calculate the times such as the next bus is one minute (or the delay is also allowed)
    # should be multiples of the first one


    # get sorted array
    bus_times = sorted(bus_times, key=attrgetter('number'))
    print(bus_times)
    bus_times = (bus_times[::-1])
    print(bus_times)

    found = False
    time = 0
    time += bus_times[0].number -bus_times[0].delay
    final_time = 0

    to_print = 10
    # 100000000582
    # 100000000000000
    # 200000000000000

    to_add = bus_times[0].number
    prev = 0

    pos_array = 1

    while not found:
        # if time > to_print:
            # to_print*= 10
            # print(time)

        repeats = 0
        for bus in bus_times[1:]:
            repeats+=1
            if (time + bus.delay) % bus.number != 0:
                break
            else:
                if pos_array == repeats:
                    if prev == 0:
                        prev = time
                    else:
                        to_add = time - prev
                        print("to add:",to_add)
                        prev = 0
                        pos_array += 1


            if bus_times[-1] == bus:
                found = True
                final_time = time

        time += to_add


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

