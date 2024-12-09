import sys

def read_file(file):
    with open(file, 'r') as f: data = f.read()
    cells, vals, empty, cur_pos = [], [], [], 0
    for i, x in enumerate(data, 1):
        cells.extend([(i // 2 + 1 if i % 2 else 0)] * int(x))
        (vals if i % 2 else empty).append([i // 2 + 1 if i % 2 else 0, int(x), cur_pos])
        cur_pos += int(x)
    return cells, vals, empty

def pt1(cells):
    tot, start, end = 0, 0, len(cells) - 1
    while start < end:
        if cells[start]: tot += (cells[start] - 1) * start
        else:
            while not cells[end]: end -= 1
            tot += (cells[end] - 1) * start; end -=1
        start += 1
    return tot

def pt2(cells, vals, empty):
    for v in reversed(vals):
        for e in empty:
            if e[2] > v[2]: break
            if e[1] >= v[1]:
                cells[e[2]:e[2] + v[1]], cells[v[2]:v[2] + v[1]] = [v[0]] * v[1], [0] * v[1]
                e[1] -= v[1]; e[2] += v[1]
                break
    return sum(max(v - 1, 0) * i for i, v in enumerate(cells))

c, v, e = read_file(sys.argv[1])
print(pt1(c)); print(pt2(c, v, e))
