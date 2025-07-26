def get_input() -> str:
    with open("mock.txt") as file:
        return file.read().strip()


def reformat(input: str) -> str:
    res = ""
    block = True
    file_id = 0
    for x in input:
        res += (str(file_id) if block else ".") * int(x)
        if block:
            file_id += 1
        block = not block
    return res


def compress(input: str) -> str:
    res = ""
    right = -1
    total_length = len(input)

    for i in range(len(input)):
        if i - right > total_length:
            res += "."
            continue

        if input[i] != ".":
            res += input[i]

        else:
            while i - right < total_length:
                if input[right] == ".":
                    right -= 1
                else:
                    res += input[right]
                    right -= 1
                    break
    return res


def calculate_checksum(input: str) -> int:
    return sum([i * int(x) for i, x in enumerate(input) if x != "."])


input = get_input()
reformatted = reformat(input)
compressed = compress(reformatted)
checksum = calculate_checksum(compressed)
print(checksum)
# i have no idea why this isn't working, probably the compress
