from collections import namedtuple


def get_input() -> list[str]:
    with open("input.txt", "r") as file:
        return [lines.splitlines() for lines in file.read().strip().split("\n\n")]


Button = namedtuple("Button", ["x", "y"])
Prize = namedtuple("Prize", ["x", "y"])


def parse_xy(line: str) -> tuple[int, int]:
    button, xy = line.split(": ")
    x, y = xy.split(", ")
    x = int("".join(a for a in x if a.isdigit()))
    y = int("".join(a for a in y if a.isdigit()))
    return (x, y)


def parse_input(input_data: list[str]) -> tuple[Button, Button, Prize]:
    return (
        Button(*parse_xy(input_data[0])),
        Button(*parse_xy(input_data[1])),
        Prize(*parse_xy(input_data[2])),
    )


def parse_input_part_2(input_data: list[str]) -> tuple[Button, Button, Prize]:
    return (
        Button(*parse_xy(input_data[0])),
        Button(*parse_xy(input_data[1])),
        Prize(*(x + 10000000000000 for x in parse_xy(input_data[2]))),
    )


def solve(a: Button, b: Button, prize: Prize, max_presses: int | None) -> int | None:
    # 2x2 determinant
    det = a.x * b.y - a.y * b.x

    if det == 0:
        return 0  # No unique solution

    # Compute n and m using Cramer's Rule
    # i think gaussian elimination would be faster
    dx = prize.x
    dy = prize.y

    n_num = b.y * dx - b.x * dy
    m_num = -a.y * dx + a.x * dy

    if n_num % det != 0 or m_num % det != 0:
        return 0  # No integer solution

    n = n_num // det
    m = m_num // det

    if n < 0 or m < 0:
        return 0  # Presses can't be negative

    if max_presses is not None and (n > max_presses or m > max_presses):
        return 0  # Too many presses

    return 3 * n + m  # Total cost


def part_1():
    data = get_input()
    print(sum(solve(*parse_input(d), max_presses=100) for d in data))


def part_2():
    data = get_input()
    print(sum(solve(*parse_input_part_2(d), max_presses=None) for d in data))


part_1()
part_2()
