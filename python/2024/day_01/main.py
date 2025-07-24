from collections import Counter


def get_pairs() -> list[list[int]]:
    with open("./input.txt") as f:
        return [[int(num) for num in l.split("   ")] for l in f.read().splitlines()]


def part1() -> int:
    pairs = get_pairs()
    l1, l2 = zip(*pairs)
    total_diff = sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2)))
    print(total_diff)


def part2() -> int:
    pairs = get_pairs()
    l1, l2 = zip(*pairs)
    c = Counter(l2)
    total_similarity = sum(a * c.get(a, 0) for a in l1)
    print(total_similarity)


part1()
part2()
