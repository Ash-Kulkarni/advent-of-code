import re


def get_input() -> str:
    with open("./input.txt") as f:
        return f.read().strip()


def part1():
    input = get_input()
    x = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(x, input)
    total = sum([int(a) * int(b) for a, b in matches])
    print(total)


def part2():
    input = get_input()
    x = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))"
    matches = re.findall(x, input)

    total = 0
    doing = True
    for a, b, do, dont in matches:
        if do:
            doing = True
        if dont:
            doing = False
        if a and b and doing:
            total += int(a) * int(b)
    print(total)


part1()
part2()
