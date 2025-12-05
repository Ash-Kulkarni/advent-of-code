def input_lines():
    with open("./input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        sep = lines.index("")
        return lines[:sep], lines[sep + 1 :]


def part_1():
    ranges, ids = input_lines()
    fresh_ranges = set()
    for r in ranges:
        low, high = r.split("-")
        fresh_ranges.add((int(low), int(high)))
    total = len([i for i in ids if any(a <= int(i) <= b for a, b in fresh_ranges)])
    print(total)


def part_2():
    ranges, _ = input_lines()
    intervals = []
    for r in ranges:
        low, high = r.split("-")
        intervals.append((int(low), int(high)))

        intervals.sort()

        merged = []
        for start, end in intervals:
            if merged and start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

    total = sum(high - low + 1 for low, high in merged)
    print(total)


if __name__ == "__main__":
    part_2()
