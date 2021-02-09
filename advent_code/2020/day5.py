import os
import sys

def part_1():
    boarding_passes = []
    seat_ids = []
    with open("input5.txt") as fp:
        for line in fp:
            line = line.strip()
            boarding_passes.append(line)


    # boarding_passes = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

    for boarding_pass in boarding_passes:
        rows = 128
        cols = 8
        seat_row = 0
        seat_col = 0
        row_letters = boarding_pass[:7]
        col_letters = boarding_pass[-3:]

        for letter in row_letters:
            rows = rows/2
            if letter == 'B':
                seat_row += rows

        for letter in col_letters:
            cols = cols/2
            if letter == 'R':
                seat_col += cols

        seat_row = int(seat_row)
        seat_col = int(seat_col)
        seat_id = seat_row * 8 + seat_col
        seat_ids.append(seat_id)

    seat_ids.sort()
    print("highest seat:", seat_ids[-1])

    iter_id = seat_ids[0]
    for seat_id in seat_ids:
        if seat_id != iter_id:
            row = iter_id // 8
            col = iter_id % 8
            print("-seat_id:", iter_id)
            print("-row:", row)
            print("-col:", col)
            break
        iter_id += 1


if __name__ == "__main__":
    try:
        which_part = sys.argv[1]
        if which_part == '1':
            part_1()
        elif which_part == '2':
            part_1()
        else:
            print("arguments can only be 1 or 2")

    except IndexError:
        print("specify a part")
        print("example:")
        print("python3 dayX.py 2")
