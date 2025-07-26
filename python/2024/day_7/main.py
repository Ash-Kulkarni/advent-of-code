from itertools import product


def get_input():
    with open("input.txt") as file:
        return file.read().strip().splitlines()


def generate_operations(ops, length):
    ops = ["+", "*", "||"]
    return product(ops, repeat=length - 1)


def scan_input():
    for line in get_input():
        val, nums_str = line.split(":")
        nums = [int(num.strip()) for num in nums_str.split(" ") if num]
        yield int(val.strip()), nums


def eval_line(val, nums):
    for ops in generate_operations(["+", "*"], len(nums)):
        res = nums[0]
        for op, num in zip(ops, nums[1:]):
            if op == "+":
                res += num
            elif op == "*":
                res *= num
            elif op == "||":
                res = int(str(res) + str(num))
        if res == val:
            return val
    return 0


total = 0
for val, nums in scan_input():
    total += eval_line(val, nums)
print(total)
