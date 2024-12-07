import sys

def read_file(file):
    with open(file, 'r') as f:
        return [list(map(int, line.replace(":","").strip().split())) for line in f.readlines()]

def isValid(n, l, pt):
    if len(l) == 1:
        return l[0] == n
    return (
        isValid(n, [l[0] + l[1]] + l[2:], pt) or
        isValid(n, [l[0] * l[1]] + l[2:], pt) or
        (pt == 2 and isValid(n, [int(str(l[0]) + str(l[1]))] + l[2:], pt))
    )

def part(data, i):
    return sum(row[0] for row in data if isValid(row[0], row[1:], i))

print(part(read_file(sys.argv[1]), 1))
print(part(read_file(sys.argv[1]), 2))
