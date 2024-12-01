import sys

def read_file(file):
    l1 = []
    l2 = []
    with open(file, 'r') as f:
        for line in f:
            values = line.split()
            l1.append(int(values[0]))
            l2.append(int(values[1]))
        l1.sort()
        l2.sort()
    return l1, l2

def pt1(l1, l2):
    tot = 0
    for i in range(0, len(l1)):
        mx, mn = (l1[i], l2[i]) if l1[i] > l2[i] else (l2[i], l1[i])
        tot += (mx-mn)
    return tot

def pt2(l1, l2):
    freq = {item: l2.count(item) for item in l1}
    tot = sum(key * value for key, value in freq.items())
    return tot

left, right = read_file(sys.argv[1])

# part 1
total = pt1(left, right)
print(total)

# part 2
score = pt2(left, right)
print(score)
