from itertools import product
import sys

def read_grid_to_dict(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
        return {(x, y): char for y, line in enumerate(lines) for x, char in enumerate(line)}

def search(grid, position, direction):
    while grid.get(position) != '#':
        prev_position = position
        grid[position] = 'X'
        position = (position[0] + direction[0], position[1] + direction[1])
        if position not in grid:
            return position
    return prev_position

def pt1(grid, directions, position, face):
    while position in grid:
        position = search(grid, position, directions[face])
        if position not in grid:
            break
        face = (face + 1) % 4
    return sum(1 for value in grid.values() if value == 'X')

def check_for_loop(grid, pos, face, obstacle):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    path = {}
    
    while True:
        next_pos = (pos[0] + directions[face][0], pos[1] + directions[face][1])
        if next_pos not in grid:
            return False
        if grid.get(next_pos) == '#' or next_pos == obstacle:
            face = (face + 1) % 4
            continue
        if next_pos in path and face in path[next_pos]:
            return path
        path.setdefault(next_pos, []).append(face)
        pos = next_pos

def pt2(grid, directions, position, face):
    result, visited = {}, []
    
    while True:
        next_pos = (position[0] + directions[face][0], position[1] + directions[face][1])
        if next_pos not in grid:
            break
        if grid.get(next_pos) == '#':
            face = (face + 1) % 4
            continue
        
        if next_pos not in result and next_pos not in visited:
            found_loop = check_for_loop(grid, position, (face + 1) % 4, next_pos)
            if found_loop:
                result[next_pos] = True
        position = next_pos
        visited.append(position)
    
    return len(result)

grid = read_grid_to_dict(sys.argv[1])
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
pos = next(coords for coords, value in grid.items() if value == '^')
fce = 0  

print(pt1(grid.copy(), dirs, pos, fce))
print(pt2(grid, dirs, pos, fce))
