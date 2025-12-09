from pydantic import BaseModel


def read_input(strip: bool = True) -> list[str]:
    with open("./input.txt") as f:
        return [line.strip() if strip else line for line in f]


class Point(BaseModel):
    x: int
    y: int


def area_within(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x + 1) * abs(p1.y - p2.y + 1)


def part_1():
    lines = read_input()
    coords = [Point(x=int(x), y=int(y)) for l in lines for x, y in [l.split(",")]]
    pairs = [[p1, p2] for i, p1 in enumerate(coords) for p2 in coords[i + 1 :]]
    largest_area = max(area_within(p1, p2) for p1, p2 in pairs)
    print(f"Largest area: {largest_area}")


if __name__ == "__main__":
    part_1()
