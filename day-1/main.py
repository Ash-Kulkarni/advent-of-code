import re


def get_data():
    with open("input.txt") as f:
        data = f.read()
        return data


def get_line_values(line: str) -> int:
    digits = re.sub("[^0-9]", "", line)

    if len(digits) < 2:
        raise ValueError("line has < 2 numbers")

    return int(digits[0] + digits[-1])


def process_part_1(input: str) -> None:
    input_lines: list[str] = input.split("/n/n")
    line_totals = map(get_line_values, input_lines)
    total = sum(line_totals)
    print(total)


if __name__ == "__main__":
    process_part_1(get_data())
