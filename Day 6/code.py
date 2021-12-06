import numpy as np

def input_data():
    lines = open("Day 6/input.txt")
    first_line = lines.readline()
    data = list(map(int, first_line.split(',')))
    return np.array(data)

def part_one(d):
    days = 256
    for i in range(0, days):
        current_len = len(d)
        for j in range(0, current_len):
            if d[j] == 0:
                d[j] = 6
                d.append(8)
            else:
                d[j] = d[j] - 1
        print(d)
    return len(d)

def part_two(d):
    days = 256
    v = [0]*9
    print(d)
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
    # print(part_one(d))
    print(part_two(d))