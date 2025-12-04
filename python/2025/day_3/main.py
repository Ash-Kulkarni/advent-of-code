from typing import Tuple


def input_lines():
    with open("./input.txt") as f:
        return [line.strip() for line in f.readlines()]


def leftmost_max(nums: list[int]) -> Tuple[int, int]:
    highest = 0
    index = 0
    for i, x in enumerate(nums):
        if x > highest:
            highest = x
            index = i
    return highest, index


def max_joltage(bank: list[int], num_batteries: int) -> int:
    if len(bank) < num_batteries:
        raise ValueError("Not enough batteries in bank")
    results = []

    start_index = 0

    for i in range(num_batteries):
        end_index = -num_batteries + i + 1 if i < num_batteries - 1 else None
        highest, index = leftmost_max(bank[start_index:end_index])
        results.append(highest)
        start_index += index + 1

    return int("".join(str(r) for r in results))


def main():
    banks = [[int(i) for i in l] for l in input_lines()]
    total_joltage_part_1 = sum(max_joltage(b, 2) for b in banks)
    total_joltage_part_2 = sum(max_joltage(b, 12) for b in banks)
    print(total_joltage_part_1)
    print(total_joltage_part_2)


if __name__ == "__main__":
    main()
