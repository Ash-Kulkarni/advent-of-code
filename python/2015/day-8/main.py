from typing import List

with open("input.txt") as f:
    data = f.read().splitlines()


def get_escaped_char_diff(s: str) -> int:
    chars_code = 4
    escaped_indices = []
    for i, c in enumerate(s):
        if c == "\\" and i not in escaped_indices:
            escaped_indices.append(i+1)
            escaped_char = s[i+1]
            match escaped_char:
                case "x":
                    chars_code += 1
                case _:
                    chars_code += 2
    return chars_code




chars_code = 0

for line in data:
    chars_code += get_escaped_char_diff(line)

print(chars_code)
