from math import prod


def read_input(strip: bool = True) -> list[str]:
    with open("./input.txt") as f:
        return [line.strip() if strip else line for line in f]


def parse_line(line: str) -> list[str]:
    return line.split()


def transpose(grid: list[list[str]]) -> list[list[str]]:
    return [list(col) for col in zip(*grid)]


def evaluate(nums: list[int], op: str) -> int:
    if op == "+":
        return sum(nums)
    elif op == "*":
        return prod(nums)
    raise ValueError(f"Unknown operation {op}")


def part_1():
    data = transpose([parse_line(row) for row in read_input()])
    total = sum(evaluate(list(map(int, nums)), op) for *nums, op in data)
    print(total)


def extract_numbers(columns: list[str]) -> list[int]:
    reversed = [col[::-1] for col in columns]
    nums = []
    for i in range(len(columns[0])):
        num = "".join(row[i] for row in reversed if row[i] != " ").strip()
        if num:
            nums.append(int(num))
    return nums


def find_op_ranges(ops_line: str) -> list[tuple[int, int, str]]:
    ranges = []
    start, current_op = None, None
    for i, char in enumerate(ops_line):
        if char in "+*":
            if start is not None:
                ranges.append((start, i, current_op))
            start, current_op = i, char
    ranges.append((start, len(ops_line), current_op))
    return ranges


def part_2():
    *data, ops = read_input(strip=False)
    total = sum(
        evaluate(extract_numbers([row[start:end] for row in data]), op)
        for start, end, op in find_op_ranges(ops)
    )
    print(total)


if __name__ == "__main__":
    part_2()
