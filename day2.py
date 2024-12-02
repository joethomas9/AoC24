import sys
import numpy as np

def read_file(file):
    with open(file, 'r') as f:
        data = [[int(i) for i in line.split()] for line in f]
    return data


def pt1(row):
    return all(1 <= abs(row[i]-row[i+1]) <= 3 for i in range(len(row)-1)) and (row == sorted(row) or row == sorted(row)[::-1])

def pt2(row):
    return any(pt1(row[:i]+row[i+1:]) for i in range(len(row)))

mat = read_file(sys.argv[1])

# part 1
safe = sum(pt1(i) for i in mat)
print(safe)

# part 2
dampened = sum(pt2(i) for i in mat)
print(dampened)