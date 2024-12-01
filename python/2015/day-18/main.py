with open("input.txt", "r") as f:
    data = f.read().splitlines()


grid = []
for line in data:
    grid.append([1 if c == "#" else 0 for c in line])


def update(grid):
    grid_x = len(grid)
    grid_y = len(grid[0])

    new_grid = []

    # if on, stay on if 2 or 3 neighbors are on
    # if off, turn on if 3 neighbors are on
    for i in range(grid_x):
        new_grid.append([])
        for j in range(grid_y):
            neighbors = 0

            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= grid_x or j + y < 0 or j + y >= grid_y:
                        continue
                    neighbors += grid[i + x][j + y]

            # corners are always on
            if (i == 0 or i == grid_x - 1) and (j == 0 or j == grid_y - 1):
                new_grid[i].append(1)
                continue

            if grid[i][j] == 1:
                new_grid[i].append(1 if neighbors == 2 or neighbors == 3 else 0)
            else:
                new_grid[i].append(1 if neighbors == 3 else 0)
    return new_grid


for i in range(100):
    grid = update(grid)

print(sum([sum(row) for row in grid]))
