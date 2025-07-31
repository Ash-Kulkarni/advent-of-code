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
    if i - 1 >= 0:
        if int(grid[i - 1][j]) == value:
            res.append((i - 1, j))
    # down
    if i + 1 < len(grid):
        if int(grid[i + 1][j]) == value:
            res.append((i + 1, j))
    # left
    if j - 1 >= 0:
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


def get_trailhead_rating(i: int, j: int, grid: list[list[str]]) -> int:
    paths = [[[(i, j)]]]
    looking_for = 1
    while paths:
        for p in paths:
            next_paths = p[-1]
            p_next = []
            for next_path in next_paths:
                a, b = next_path
                p_next.extend(get_adjacent_with_value(grid, a, b, looking_for))
            if p_next:
                p.append(p_next)
        looking_for += 1
        paths = [p for p in paths if len(p) == looking_for]
        if looking_for == 10:
            return sum(len(p[-1]) for p in paths)
    return 0


def part_1():
    g = get_input()
    total_score = sum(get_trailhead_score(i, j, g) for i, j in trailheads(g))
    print(total_score)


def part_2():
    g = get_input()
    total_rating = sum(get_trailhead_rating(i, j, g) for i, j in trailheads(g))
    print(total_rating)


part_1()
part_2()
