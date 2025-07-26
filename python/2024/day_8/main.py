from itertools import combinations


def print_grid(grid: list[str], antinodes: set) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not (i, j) in antinodes:
                print(grid[i][j], end="")
            else:
                print("#", end="")
        print()


def get_input() -> list[str]:
    with open("input.txt") as file:
        return file.read().strip().splitlines()


def get_size(grid: list[str]) -> tuple[int, int]:
    return len(grid), len(grid[0]) if grid else 0


def within_bounds(y: int, x: int, size_y: int, size_x: int) -> bool:
    return 0 <= y < size_y and 0 <= x < size_x


def part_1():
    data = get_input()
    size_y, size_x = get_size(data)

    x = {}
    antinodes = set()

    for i in range(size_y):
        for j in range(size_x):
            char = data[i][j]
            if char == ".":
                continue
            if char not in x:
                x[char] = set()
            x[char].add((i, j))

    for antenna, positions in x.items():
        pairs = combinations(positions, 2)
        for a, b in pairs:
            diff_y = b[0] - a[0]
            diff_x = b[1] - a[1]

            node_1 = (a[0] - diff_y, a[1] - diff_x)
            node_2 = (b[0] + diff_y, b[1] + diff_x)

            for n in (node_1, node_2):
                if within_bounds(n[0], n[1], size_y, size_x):
                    antinodes.add(n)

    print(len(antinodes))
    # print_grid(data, antinodes)


def part_2():
    data = get_input()
    size_y, size_x = get_size(data)

    x = {}
    antinodes = set()

    for i in range(size_y):
        for j in range(size_x):
            char = data[i][j]
            if char == ".":
                continue
            if char not in x:
                x[char] = set()
            x[char].add((i, j))

    for antenna, positions in x.items():
        pairs = combinations(positions, 2)
        for a, b in pairs:
            diff_y = b[0] - a[0]
            diff_x = b[1] - a[1]

            negative = (a[0] - diff_y, a[1] - diff_x)
            positive = (b[0] + diff_y, b[1] + diff_x)

            antinodes.add(b)
            antinodes.add(a)

            while within_bounds(negative[0], negative[1], size_y, size_x):
                antinodes.add(negative)
                negative = (negative[0] - diff_y, negative[1] - diff_x)
            while within_bounds(positive[0], positive[1], size_y, size_x):
                antinodes.add(positive)
                positive = (positive[0] + diff_y, positive[1] + diff_x)

    print(len(antinodes))

    # print_grid(data, antinodes)


part_1()
part_2()
