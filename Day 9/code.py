import numpy as np

def input_data():
    lines = open("Day 9/input.txt")
    data = [[int(i) for i in line.strip()] for line in lines]
    return np.array(data)

def is_low_point(d, i, j):
    i_len = np.size(d, 0) - 1
    j_len = np.size(d, 1) - 1
    if (i > 0) and (d[i - 1, j] <= d[i, j]): 
        return False
    if (j > 0) and (d[i, j - 1] <= d[i, j]): 
        return False
    if (i < i_len) and (d[i + 1, j] <= d[i, j]): 
        return False
    if (j < j_len) and (d[i, j + 1] <= d[i, j]): 
        return False
    return True


def part_one(d):
    risk_level_sum = 0
    for i in range(0, np.size(d,0)):
        for j in range(0, np.size(d,1)):
            if is_low_point(d, i, j):
                risk_level_sum += d[i,j] + 1
    return risk_level_sum

def part_two(d):
    i_len = np.size(d, 0) - 1
    j_len = np.size(d, 1) - 1

    def neighbour_count(i, j): 
        sum = 1
        d[i,j] = 9
        # Recursively check for all neighbours
        if (i > 0) and (d[i - 1, j] < 9): 
            sum += neighbour_count(i - 1, j)
        if (j > 0) and (d[i, j - 1] < 9): 
            sum += neighbour_count(i, j - 1)
        if (i < i_len) and (d[i + 1, j] < 9): 
            sum += neighbour_count(i + 1, j)
        if (j < j_len) and (d[i, j + 1] < 9): 
            sum += neighbour_count(i, j + 1)
        return sum

    basins = [0, 0, 0]

    for i in range(0, np.size(d,0)):
        for j in range(0, np.size(d,1)):
            if is_low_point(d, i, j):
                current_count = neighbour_count(i,j)
                if current_count >= basins[0]:
                    basins[2] = basins[1]
                    basins[1] = basins[0]
                    basins[0] = current_count
                elif current_count >= basins[1]:
                    basins[2] = basins[1]
                    basins[1] = current_count
                elif current_count >= basins[2]:
                    basins[2] = current_count

    return basins[0] * basins[1] * basins[2]


if __name__ == "__main__":
    d = input_data()
    print("Solution part one:")
    print(part_one(d))
    print("Solution part two:")
    print(part_two(d))