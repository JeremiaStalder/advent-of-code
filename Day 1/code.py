import math

def input_data():
    lines = open("Day 1/input.txt")
    # data = [str.strip(line) for line in lines]
    data = [int(line) for line in lines]
    return data

def part_one(data):
    sum = 0
    for idx in range(1, len(data)):
        if data[idx] > data[idx - 1]:
            sum += 1
    return sum

def part_two(data):
    sum = 0
    for idx in range(3, len(data)):
        if data[idx - 3] + data[idx - 2] + data[idx - 1] < data[idx - 2] + data[idx - 1] + data[idx]:
            sum += 1
    return sum


if __name__ == "__main__":
    d = input_data()
    print(part_one(d))
    print(part_two(d))