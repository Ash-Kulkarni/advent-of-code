import itertools
from enum import Enum
from typing import Dict, NamedTuple, Tuple, Set, List


def get_input() -> List[str]:
    with open("./input.txt") as f:
        return f.readlines()

class LGInstruction(Enum):
    toggle = "toggle"
    turn_on = "on"
    turn_off = "off"

class Point(NamedTuple):
    x: int
    y: int
    brightness: int = 1

TwoPoints = Tuple[Point, Point]

class Instruction(NamedTuple):
    type: LGInstruction
    points: TwoPoints

class LightGrid:
    def __init__(self) -> None:
        self.grid: Dict[Point, int] = {}

    def get_inclusive_square(self, points: TwoPoints) -> itertools.product:
        p1, p2 = points
        left_low = Point(min(p1.x, p2.x), min(p1.y, p2.y))
        right_high = Point(max(p1.x, p2.x) +1, max(p1.y, p2.y) +1)
        return itertools.product(range(left_low.x, right_high.x), range(left_low.y, right_high.y))

    def toggle(self, points):
        for p in self.get_inclusive_square(points):
            if p in self.grid:
                self.grid[p] += 2
            else:
                self.grid[p] = 2

    def turn_on(self, points):
        for p in self.get_inclusive_square(points):
            if p in self.grid:
                self.grid[p] += 1
            else:
                self.grid[p] = 1

    def turn_off(self,points):
        for p in self.get_inclusive_square(points):
            if p in self.grid:
                if self.grid[p] > 0:
                    self.grid[p] -= 1

def parse_command(s: str) -> LGInstruction:
    if s.startswith("toggle"):
        return LGInstruction.toggle
    if s.startswith("turn on"):
        return LGInstruction.turn_on
    if s.startswith("turn off"):
        return LGInstruction.turn_off
    raise ValueError("unknown instruction type")

def parse_points(s: str) -> TwoPoints:
    p1, p2 = [Point(*[int(n) for n in word.split(",")]) for word in s.split(" ") if "," in word]
    return (p1, p2)

def parse_instruction(s: str) -> Instruction:
    command_type = parse_command(s)
    points = parse_points(s)
    return Instruction(command_type, points)

def main():
    input = get_input()
    lg = LightGrid()
    for line in input:
        i = parse_instruction(line)
        match i.type:
            case LGInstruction.toggle:
                lg.toggle(i.points)
            case LGInstruction.turn_on:
                lg.turn_on(i.points)
            case LGInstruction.turn_off:
                lg.turn_off(i.points)

    print(sum(lg.grid.values()))


if __name__ == "__main__":
    main()
