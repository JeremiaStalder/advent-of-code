import numpy as np

def input_data():
    lines = open("Day 11/input.txt")
    data = [[int(i) for i in line.strip()] for line in lines]
    return np.array(data)
    


def part_one(d):
    flashes = 0
    steps = 100
    for i in range(0, steps):
        already_calculated = np.zeros((10, 10))
        d = d + 1
        run_again = True
        while run_again:
            run_again = False
            for m in range(0, 10): # iterate through grid
                for n in range(0, 10):
                    if (d[m, n] > 9) and (already_calculated[m, n] == 0):
                        already_calculated[m, n] = 1
                        for i_m in range(-1, 2): # iterate through neighbours
                            for i_n in range(-1, 2):
                                if (-1 < (m + i_m) < 10) and (-1 < (n + i_n) < 10):
                                    d[m + i_m, n + i_n] = d[m + i_m, n + i_n] + 1
                                    if (d[m + i_m, n + i_n] > 9) and (already_calculated[m + i_m, n + i_n] == 0):
                                        run_again = True
        d[d > 9] = 0
        flashes += (d == 0).sum()
    return flashes
        

def part_two(d):
    steps = 0
    while True:
        steps += 1
        already_calculated = np.zeros((10, 10))
        d = d + 1
        run_again = True
        while run_again:
            run_again = False
            for m in range(0, 10): # iterate through grid
                for n in range(0, 10):
                    if (d[m, n] > 9) and (already_calculated[m, n] == 0):
                        already_calculated[m, n] = 1
                        for i_m in range(-1, 2): # iterate through neighbours
                            for i_n in range(-1, 2):
                                if (-1 < (m + i_m) < 10) and (-1 < (n + i_n) < 10):
                                    d[m + i_m, n + i_n] = d[m + i_m, n + i_n] + 1
                                    if (d[m + i_m, n + i_n] > 9) and (already_calculated[m + i_m, n + i_n] == 0):
                                        run_again = True
        d[d > 9] = 0
        if (d == 0).sum() == 100:
            break
        print(d)
    return steps

if __name__ == "__main__":
    d = input_data()
    print("Solution part one:")
    print(part_one(d))
    print("Solution part two:")
    print(part_two(d))