def get_reports() -> list[list[int]]:
    with open("./input.txt") as f:
        return [[int(num) for num in l.split(" ")] for l in f.read().splitlines()]


def is_all_asc_or_desc(report: list[int]) -> bool:
    if len(report) <= 2:
        return True

    return all(x > y for x, y in zip(report, report[1:])) or all(
        x < y for x, y in zip(report, report[1:])
    )


def all_diffs_between_1_and_3(report: list[int]) -> bool:
    if len(report) <= 1:
        return True

    return all(3 >= abs(x - y) >= 1 for x, y in zip(report, report[1:]))


def is_safe(report: list[int]) -> bool:
    return is_all_asc_or_desc(report) and all_diffs_between_1_and_3(report)


def part_1():
    safe_reports = [r for r in get_reports() if is_safe(r)]
    print(len(safe_reports))


def without_index(report: list[int], i: int) -> list[int]:
    if len(report) == 1:
        raise ValueError("no")

    return report[:i] + report[i + 1 :]


def permutations_skipping_a_level(report: list[int]) -> list[list[int]]:
    if len(report) == 1:
        return [report]

    return [without_index(report, i) for i in range(len(report))]


def part_2():
    safe_reports = [
        r
        for r in get_reports()
        if any(
            is_safe(report_without_a_level)
            for report_without_a_level in permutations_skipping_a_level(r)
        )
    ]
    print(len(safe_reports))


part_1()
part_2()
