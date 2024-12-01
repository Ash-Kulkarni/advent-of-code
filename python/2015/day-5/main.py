

def get_input() -> str:
    with open("./input.txt") as f:
        return f.readlines()

def has_three_vowels(s: str) -> bool:
    vowels = "aeiou"
    vowel_count = 0
    for v in vowels:
        vowel_count += s.count(v)
    return vowel_count >= 3

def has_double_letter(s: str) -> bool:
    current = s[0]
    for i in range(1, len(s)):
        if s[i] == current:
            return True
        current = s[i]
    return False

def contains_bad_string(s: str) -> bool:
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad in bad_strings:
        if bad in s:
            return True
    return False

def is_nice(s: str) -> bool:
    return has_three_vowels(s) and has_double_letter(s) and not contains_bad_string(s)

def has_pair_twice(s: str) -> bool:
    pairs = {}
    for i in range(1, len(s)):

        pair_value = s[i-1] + s[i]

        if pair_value in pairs:
            if pairs[pair_value][0] != i-1:
                return True

            pairs[pair_value].append(i)
        else:
            pairs[pair_value] = [i]

    return False

def has_repeating_letter(s: str) -> bool:
    for i in range(2, len(s)):
        if s[i-2] == s[i]:
            return s[i]
    return False

def is_nice_v2(s: str) -> bool:
    return has_pair_twice(s) and has_repeating_letter(s)

def main():
    input = get_input()
    nice = 0
    for string in input:
        if is_nice_v2(string.strip()):
            nice += 1
    print(nice)


if __name__ == "__main__":
    main()

