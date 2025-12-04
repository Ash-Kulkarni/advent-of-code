def input_lines():
    with open("./input.txt") as f:
        return [line.strip() for line in f.readlines()]


def is_invalid(n: int) -> bool:
    s = str(n)
    num_digits = len(s)
    if num_digits % 2 == 0:
        left = s[: num_digits // 2]
        right = s[num_digits // 2 :]

        if left == right:
            return True
    return False


def divisors(n: int):
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            yield i


def is_invalid_part_2(n: int) -> bool:
    s = str(n)
    num_digits = len(s)
    for d in divisors(num_digits):
        if all(s[i] == s[i + d] for i in range(num_digits - d)):
            return True
    return False


def get_invalid_ids(start: int, finish: int) -> list[int]:
    return [i for i in range(start, finish + 1) if is_invalid_part_2(i)]


def main():
    [l] = input_lines()
    ranges = l.split(",")
    total = 0
    for r in ranges:
        [start, finish] = r.split("-")
        total += sum(get_invalid_ids(int(start), int(finish)))
    print(total)


if __name__ == "__main__":
    main()
