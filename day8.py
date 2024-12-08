import sys
from itertools import permutations

def read_grid_to_dict(file_path):
    with open(file_path) as file:
        return {(x, y): char for y, line in enumerate(file) for x, char in enumerate(line.strip())}

def pt1(grid, antennas):
    return len({
        (a[0] + (a[0] - b[0]), a[1] + (a[1] - b[1]))
        for i in antennas.values()
        for a, b in permutations(i, 2)
        if (a[0] + (a[0] - b[0]), a[1] + (a[1] - b[1])) in grid
    })

def pt2(grid, antennas):
    return len({
        node
        for i in antennas.values()
        for a, b in permutations(i, 2)
        for k in range(1, len(grid) + 1)
        for node in [(a[0] + k * (b[0] - a[0]), a[1] + k * (b[1] - a[1]))]
        if node in grid
        for node in (a, b, node)
    })

grid = read_grid_to_dict(sys.argv[1])
antennas = {char: [(x, y) for (x, y), c in grid.items() if c == char] for char in set(c for c in grid.values() if c != '.')}

print(pt1(grid, antennas))
print(pt2(grid, antennas))
