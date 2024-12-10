import sys

def read_grid(file_path):
    with open(file_path) as file:
        return {(x, y): char for y, line in enumerate(file) for x, char in enumerate(line.strip())}

def check_trail(pos, trail, grid):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if grid[pos] == '9':
        return [trail]
    return [
        subtrail
        for dx, dy in directions
        if (new_pos := (pos[0] + dx, pos[1] + dy)) in grid and int(grid[new_pos]) - int(grid[pos]) == 1
        for subtrail in check_trail(new_pos, trail + [new_pos], grid)
    ]

def pt1(grid):
    return sum(len(set(trail[-1] for trail in check_trail(pos, [], grid))) for pos in [pos for pos in grid if grid[pos] == '0'])

def pt2(grid):
    return sum(len(check_trail(pos, [], grid)) for pos in [pos for pos in grid if grid[pos] == '0'])

grid = read_grid(sys.argv[1])
print(pt1(grid))
print(pt2(grid))
