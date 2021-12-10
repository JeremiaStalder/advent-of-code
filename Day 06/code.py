import numpy as np

def input_data():
    lines = open("Day 06/input.txt")
    first_line = lines.readline()
    data = list(map(int, first_line.split(',')))
    return data

def part_one(d):
    days = 80
    for i in range(0, days):
        current_len = len(d)
        for j in range(0, current_len):
            if d[j] == 0:
                d[j] = 6
                d.append(8)
            else:
                d[j] = d[j] - 1
    return len(d)

def part_two(d):
    d = np.array(d)
    days = 256
    v = [0]*9
    for i in range(0, 9):
        v[i] = np.count_nonzero(d == i)
    
    for i in range(0, days):
        count_0 = v[0]
        for i in range(0, 8):
            v[i] = v[i+1]
        v[6] += count_0
        v[8] = count_0
    return sum(v)


if __name__ == "__main__":
    d = input_data() 
    print("Solution part one:")
    print(part_one(d))
    print("Solution part two:")
    print(part_two(d))