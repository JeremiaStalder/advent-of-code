import numpy as np
import statistics 
from statistics import mode

def input_data():
    lines = open("Day 3/input.txt")
    # data = [str.strip(line) for line in lines]
    data = [[int(i) for i in str.strip(line)] for line in lines]
    return np.vstack(data)

def part_one(data):
    binary_gamma = ''.join(map(str,np.apply_along_axis(mode, 0, data)))
    binary_epsilon = ''.join('1' if x == '0' else '0' for x in binary_gamma)
    return int('0b' + binary_gamma, 2)*int('0b' + binary_epsilon, 2)

def most_common(v):
    if np.count_nonzero(v == 0) > np.count_nonzero(v == 1):
        return 0
    else:
        return 1

def part_two(data):
    oxygen_rating, CO2_rating = 0, 0
    temp_data = data
    for i in range(0,data.shape[1]):
        temp_data = temp_data[temp_data[:,i] == most_common(temp_data[:,i]),:]
        if temp_data.shape[0] == 1:
            oxygen_rating = int('0b' + ''.join(map(str, temp_data[0,:])), 2)
            break

    temp_data = data
    for i in range(0,data.shape[1]):
        temp_data = temp_data[temp_data[:,i] != most_common(temp_data[:,i]),:]
        if temp_data.shape[0] == 1:
            CO2_rating = int('0b' + ''.join(map(str, temp_data[0,:])), 2)
            break

    return oxygen_rating * CO2_rating


if __name__ == "__main__":
    d = input_data()
    # print(d)
    # print(part_one(d))
    print(part_two(d))