import math

def input_data():
    lines = open("Day 2/input.txt")
    # data = [str.strip(line) for line in lines]
    data = [(l[0], int(l[1])) for l in (line.split() for line in lines)]
    return data

def part_one(data):
    horizontal, depth = 0, 0
    for command in data:
        if command[0] == "forward":
            horizontal += command[1]
        elif command[0] == "up":
            depth -= command[1]
        else:
            depth += command[1]
    return horizontal * depth

def part_two(data):
    horizontal, depth, aim = 0, 0, 0
    for command in data:
        if command[0] == "down":
            aim += command[1]
        elif command[0] == "up":
            aim -= command[1]
        else:
            horizontal += command[1]
            depth += command[1]*aim
    return horizontal * depth



if __name__ == "__main__":
    d = input_data()
    print("Solution part one:")
    print(part_one(d))
    print("Solution part two:")
    print(part_two(d))