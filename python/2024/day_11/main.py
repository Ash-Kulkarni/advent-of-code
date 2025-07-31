def get_input() -> list[int]:
    with open("input.txt") as f:
        return [int(x) for x in f.read().strip().split(" ")]


def iterate_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        s1 = s[: len(s) // 2]
        s2 = s[len(s) // 2 :]
        return [int(s1), int(s2)]

    return [stone * 2024]


def blink(stones: dict[int, int]) -> list[int]:
    res = {}
    for s, count in stones.items():
        for new_s in iterate_stone(s):
            if new_s not in res:
                res[new_s] = 0
            res[new_s] += count
    return res


def blink_times(n):
    i = get_input()
    data = {}
    for s in i:
        if s not in data:
            data[s] = 0
        data[s] += 1
    for i in range(n):
        data = blink(data)
    print(sum(data.values()))


def part_1():
    blink_times(25)


def part_2():
    blink_times(75)


part_1()
part_2()
