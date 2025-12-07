def read_input(strip: bool = True) -> list[str]:
    with open("./input.txt") as f:
        return [line.strip() if strip else line for line in f]


def propagate(last_row: str, current_row: str) -> tuple[str, int]:
    res = {}
    num_splits = 0
    for i, (lr, cr) in enumerate(zip(last_row, current_row)):
        if (lr == "S" or lr == "|") and cr == ".":
            res[i] = "|"
        elif lr == "|" and cr == "^":
            num_splits += 1
            res[i] = cr
            for x in [i - 1, i + 1]:
                if x >= 0 and x < len(current_row) and current_row[x] != "^":
                    res[x] = "|"

        elif res.get(i) is None:
            res[i] = cr

    next_row = "".join(res[i] for i in range(len(current_row)))

    return next_row, num_splits


def part_1():
    lines = read_input()
    total_splits = 0
    last_row = None
    for current_row in lines:
        if last_row is None:
            last_row = current_row
            continue

        print(last_row)
        last_row, num_splits = propagate(last_row, current_row)
        total_splits += num_splits
    print(last_row)
    print(f"Total splits: {total_splits}")


def propagate_counts(last_counts: dict, current_row: str) -> dict:
    res = {}
    for i, count in last_counts.items():
        cr = current_row[i]
        if cr == ".":
            res[i] = res.get(i, 0) + count
        elif cr == "^":
            for x in [i - 1, i + 1]:
                if x >= 0 and x < len(current_row) and current_row[x] != "^":
                    res[x] = res.get(x, 0) + count
    return res


def part_2():
    lines = read_input()
    first_row = lines[0]
    counts = {i: 1 for i, c in enumerate(first_row) if c == "S"}
    print(counts)

    for current_row in lines[1:]:
        counts = propagate_counts(counts, current_row)

        total = sum(counts.values())
    print(f"Total timelines: {total}")


if __name__ == "__main__":
    part_2()
