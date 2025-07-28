def get_input() -> list[list[str]]:
    with open("input.txt") as file:
        return file.read().strip().splitlines()


def trailheads(grid: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "0":
                yield int(i), int(j)


def get_adjacent_with_value(grid, i: int, j: int, value: int) -> list[tuple[int, int]]:
    res = []
    # up
    if i - 1 > 0:
        if int(grid[i - 1][j]) == value:
            res.append((i - 1, j))
    # down
    if i + 1 < len(grid):
        if int(grid[i + 1][j]) == value:
            res.append((i + 1, j))
    # left
    if j - 1 > 0:
        if int(grid[i][j - 1]) == value:
            res.append((i, j - 1))
    # right
    if j + 1 < len(grid[0]):
        if int(grid[i][j + 1]) == value:
            res.append((i, j + 1))
    return res


def get_trailhead_score(i: int, j: int, grid: list[list[str]]) -> int:
    next_ = [(i, j)]
    looking_for = 1
    while next_:
        n = []
        for a, b in next_:
            n.extend(get_adjacent_with_value(grid, a, b, looking_for))
        next_ = set(n)
        if looking_for == 9:
            return len(next_)
        looking_for += 1
    return 0


def part_1():
    g = get_input()
    total_score = sum(get_trailhead_score(i, j, g) for i, j in trailheads(g))
    print(total_score)


part_1()
