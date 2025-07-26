def get_input() -> list[str]:
    with open("input.txt", "r") as file:
        return file.read().strip().split("\n")


def get_horizontal(ws: list[str]) -> int:
    res = 0
    for row in ws:
        for i in range(len(row) - 3):
            if row[i : i + 4] in ["XMAS", "SAMX"]:
                res += 1
    return res


def get_vertical(ws: list[str]) -> int:
    return get_horizontal(["".join(x) for x in zip(*ws)])


def get_diagonal(ws: list[str]) -> int:
    res = 0
    for i in range(len(ws) - 3):
        for j in range(len(ws[0]) - 3):
            word_southeast = (
                ws[i][j] + ws[i + 1][j + 1] + ws[i + 2][j + 2] + ws[i + 3][j + 3]
            )
            word_southwest = (
                ws[i][j + 3] + ws[i + 1][j + 2] + ws[i + 2][j + 1] + ws[i + 3][j]
            )
            if word_southeast in ["XMAS", "SAMX"]:
                res += 1

            if word_southwest in ["XMAS", "SAMX"]:
                res += 1

    return res


def part_1():
    input = get_input()
    h = get_horizontal(input)
    v = get_vertical(input)
    d = get_diagonal(input)
    print(h + v + d)


def part_2():
    ws = get_input()
    res = 0
    for i in range(1, len(ws) - 1):
        for j in range(1, len(ws[0]) - 1):
            word_se = ws[i - 1][j - 1] + ws[i][j] + ws[i + 1][j + 1]
            word_sw = ws[i - 1][j + 1] + ws[i][j] + ws[i + 1][j - 1]
            if word_se in ["MAS", "SAM"] and word_sw in ["MAS", "SAM"]:
                res += 1
    print(res)


part_1()
part_2()
