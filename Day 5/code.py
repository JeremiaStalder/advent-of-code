import numpy as np
import re

def input_data():
    lines = open("Day 5/input.txt")
    data = [int(l) for l in (re.split(',| -> ', line) for line in lines)]

    return np.array(data)

# def part_one(d):


# def part_two(d):
 


if __name__ == "__main__":
    d = input_data()
    # print(part_one(d))
    print(part_two(d))