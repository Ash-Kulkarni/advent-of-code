from typing import Tuple


def input_lines():
    with open("./input.txt") as f:
        return [line.strip() for line in f.readlines()]


def is_accessible(x: int, y: int, grid: list[list[str]]) -> bool:
    grid_x, grid_y = len(grid[0]), len(grid)

    neighbors: list[Tuple[int, int]] = []

    for x_offset, y_offset in [
        (0, -1),
        (0, 1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (1, 0),
        (1, -1),
        (1, 1),
    ]:
        n_x, n_y = x + x_offset, y + y_offset
        if 0 <= n_x < grid_x and 0 <= n_y < grid_y:
            neighbors.append((n_x, n_y))

    return len([n for n in neighbors if grid[n[1]][n[0]] == "@"]) < 4


def process_grid(g: list[list[str]]) -> set[Tuple[int, int]]:
    accessible_paper = set()
    for y, row in enumerate(g):
        for x, char in enumerate(row):
            if char == "@" and is_accessible(x, y, g):
                accessible_paper.add((x, y))
    return accessible_paper


def main():
    grid = [[i for i in l] for l in input_lines()]
    accessible = process_grid(grid)
    total = len(accessible)
    while accessible:
        new_grid = [row.copy() for row in grid]
        for x, y in accessible:
            new_grid[y][x] = "."
        grid = new_grid
        accessible = process_grid(grid)
        total += len(accessible)
    print(total)


if __name__ == "__main__":
    main()
