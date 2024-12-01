with open("input.txt") as f:
    data = f.read().strip()

def has_three_letter_straight(s: str) -> bool:

    for i in range(len(s) - 2):

        a, b, c = s[i], s[i + 1], s[i + 2]
        x = ord(a)
        y = ord(b)
        z = ord(c)

        if x + 1 == y and y + 1 == z:
            return True

    return False



def has_no_iol(s: str) -> bool:
    for c in "iol":
        if c in s:
            return False
    return True

def contains_two_pairs(s: str) -> bool:
    seen = False
    pair = {}
    for i, c in enumerate(s[:-1]):
        if c == s[i + 1] and not seen:
            pair[c] = i
            seen = True
        if seen:
            seen = False
    if len(pair) >= 2:
        return True


def increment_char(c: str) -> str:
    if c == "z":
        return "a"
    return chr(ord(c) + 1)

def increment_password(s: str) -> str:
    password = list(s)
    for i in range(len(password) - 1, -1, -1):
        password[i] = increment_char(password[i])
        if password[i] != "a":
            break
    return "".join(password)

def get_next_password(s: str) -> str:
    current_password = s
    while True:
        current_password = increment_password(current_password)

        if has_three_letter_straight(current_password) and has_no_iol(current_password) and contains_two_pairs(current_password):
            return current_password

def main():
    next_password = get_next_password(data)
    print(f"Next password: {next_password}")
    next_password = get_next_password(next_password)
    print(f"Next password: {next_password}")

if __name__ == "__main__":
    main()

