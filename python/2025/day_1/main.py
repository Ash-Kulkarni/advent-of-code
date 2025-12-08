from enum import Enum

from pydantic import BaseModel


def left(i: int) -> int:
    if i == 0:
        return 99
    return i - 1


def right(i: int) -> int:
    if i == 99:
        return 0
    return i + 1


class Direction(Enum):
    left = "L"
    right = "R"


class Command(BaseModel):
    direction: Direction
    value: int

    def execute(self, value: int) -> tuple[int, int]:
        fn = left if self.direction == Direction.left else right
        num_zeroes = 0
        for _ in range(self.value):
            value = fn(value)
            if value == 0:
                num_zeroes += 1

        return value, num_zeroes


def input_lines():
    with open("./input.txt") as f:
        return [line.strip() for line in f.readlines()]


def parse_line(l: str) -> Command:
    return Command(direction=Direction(l[0]), value=int(l[1:]))


def main():
    value = 50
    num_zeroes = 0
    for l in input_lines():
        cmd = parse_line(l)
        value, _num_zeroes = cmd.execute(value)
        num_zeroes += _num_zeroes

        # if value == 0:
        #     num_zeroes += 1
    print(f"Final value: {value}, number of zeroes: {num_zeroes}")


if __name__ == "__main__":
    main()
