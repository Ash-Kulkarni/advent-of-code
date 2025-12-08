from collections import Counter
from math import prod

from pydantic import BaseModel


def read_input(strip: bool = True) -> list[str]:
    with open("./input.txt") as f:
        return [line.strip() if strip else line for line in f]


class Box(BaseModel):
    id: int
    x: int
    y: int
    z: int


class Circuits(BaseModel):
    circuits: list[int]

    @classmethod
    def create(cls, size: int):
        return cls(circuits=list(range(size)))

    def find(self, box_id: int) -> int:
        if self.circuits[box_id] != box_id:
            self.circuits[box_id] = self.find(self.circuits[box_id])
        return self.circuits[box_id]

    def join(self, box_a: int, box_b: int) -> bool:
        root_a, root_b = self.find(box_a), self.find(box_b)
        if root_a != root_b:
            self.circuits[root_b] = root_a
            return True
        return False

    def get_sizes(self) -> list[int]:
        sizes = Counter(self.find(i) for i in range(len(self.circuits)))
        return sorted(sizes.values(), reverse=True)


def parse_line(line: str, id: int) -> Box:
    data = {}
    for k, v in zip(["x", "y", "z"], line.split(",")):
        data[k] = int(v)
    return Box(id=id, **data)


def distance_squared(b1: Box, b2: Box) -> int:
    return (b1.x - b2.x) ** 2 + (b1.y - b2.y) ** 2 + (b1.z - b2.z) ** 2


def part_1():
    num_links = 1000
    lines = read_input()
    boxes = [parse_line(line, i) for i, line in enumerate(lines)]
    distances = [
        (distance_squared(boxes[i], boxes[j]), i, j)
        for i in range(len(boxes))
        for j in range(i + 1, len(boxes))
    ]
    sorted_distances = sorted(distances, key=lambda x: x[0])

    circuits = Circuits.create(len(boxes))

    for i in range(num_links):
        _, box_a, box_b = sorted_distances[i]
        circuits.join(box_a, box_b)

    top_3 = circuits.get_sizes()[:3]
    result = prod(top_3)
    print(top_3)
    print(result)


def part_2():
    lines = read_input()
    boxes = [parse_line(line, i) for i, line in enumerate(lines)]
    distances = [
        (distance_squared(boxes[i], boxes[j]), i, j)
        for i in range(len(boxes))
        for j in range(i + 1, len(boxes))
    ]
    sorted_distances = sorted(distances, key=lambda x: x[0])

    circuits = Circuits.create(len(boxes))

    connections = 0
    last_pair = None
    for _, box_a, box_b in sorted_distances:
        if circuits.join(box_a, box_b):
            connections += 1
            last_pair = (box_a, box_b)
            if connections == len(boxes) - 1:
                break

    x1 = boxes[last_pair[0]].x
    x2 = boxes[last_pair[1]].x
    print(x1 * x2)


if __name__ == "__main__":
    part_1()
    part_2()
