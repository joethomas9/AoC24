import sys, numpy as np, itertools
from scipy.signal import convolve2d

def read_file(file):
    with open(file) as f:
        lines = [line.strip() for line in f]
    return lines

def pt1(grid):
    def search(i, j, d, grid):
        dx, dy = d
        return all(
            0 <= (ii := i + k * dx) < len(grid) and 
            0 <= (jj := j + k * dy) < len(grid[0]) and 
            grid[ii][jj] == x 
            for k, x in enumerate("XMAS")
        )
    
    dd = [(dx, dy) for dx, dy in itertools.product(range(-1, 2), repeat=2) if (dx, dy) != (0, 0)]

    tot = 0
    for i, j, d in itertools.product(range(len(grid)), range(len(grid[0])), dd):
        tot += search(i, j, d, grid)

    return tot

def pt2(grid):
    grid = np.array([[ord(char) for char in line] for line in grid])
    mask = np.array([[1 / ord('M'), 0, 1 /ord('S')], [0, 1 / ord('A'), 0], [1 / ord('M'), 0, 1 / ord('S')]])
    rots = [np.rot90(mask, i) for i in range(4)]

    return sum(np.count_nonzero(convolve2d(grid, r, mode='valid') == 5) for r in rots)

mat = read_file(sys.argv[1])
print(pt1(mat))
print(pt2(mat))
