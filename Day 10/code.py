# Caveat: only works with python version >= 3.10

import collections
import statistics

def input_data():
    lines = open("Day 10/input.txt")
    data = [[str(i) for i in line.strip()] for line in lines]
    return data


def part_one(d):
    result = 0
    q1 = collections.deque()

    for line in d:
        for i in line:
            match i:
                case '(':
                    q1.append('(')
                case '[':
                    q1.append('[')
                case '{':
                    q1.append('{')
                case '<':
                    q1.append('<')
                case ')':
                    if q1[-1] != '(':
                        result += 3
                        break
                    else:
                        q1.pop()
                case ']':
                    if q1[-1] != '[':
                        result += 57
                        break
                    else:
                        q1.pop()
                case '}':
                    if q1[-1] != '{':
                        result += 1197
                        break
                    else:
                        q1.pop()
                case '>':
                    if q1[-1] != '<':
                        result += 25137
                        break
                    else:
                        q1.pop()
    return result


def part_two(d):
    score = []

    for line in d:
        q1 = collections.deque()
        break_flag = False
        for i in line:
            # only works with python version >= 3.10
            match i:
                case '(':
                    q1.append('(')
                case '[':
                    q1.append('[')
                case '{':
                    q1.append('{')
                case '<':
                    q1.append('<')
                case ')':
                    if q1[-1] != '(':
                        break_flag = True
                        break
                    else:
                        q1.pop()
                case ']':
                    if q1[-1] != '[':
                        break_flag = True
                        break
                    else:
                        q1.pop()
                case '}':
                    if q1[-1] != '{':
                        break_flag = True
                        break
                    else:
                        q1.pop()
                case '>':
                    if q1[-1] != '<':
                        break_flag = True
                        break
                    else:
                        q1.pop()
        
        if break_flag == False:
            current_score = 0
            while q1:
                i = q1.pop()
                match i:
                    case '(':
                        current_score = current_score * 5 + 1
                    case '[':
                        current_score = current_score * 5 + 2
                    case '{':
                        current_score = current_score * 5 + 3
                    case '<':
                        current_score = current_score * 5 + 4
            
            score.append(current_score)
    return statistics.median(score)

   


if __name__ == "__main__":
    d = input_data()
    print("Solution part one:")
    print(part_one(d))
    print("Solution part two:")
    print(part_two(d))