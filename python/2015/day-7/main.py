from enum import Enum
from typing import List

class Instruction(Enum):
    ASSIGN = 1
    AND = 2
    OR = 3
    LSHIFT = 4
    RSHIFT = 5
    NOT = 6

def to_bin(v):
    return bin(int(v, 2))


def bitwise_complement(value):
    return ~value & 0xffff


def bitwise_and(a: int, b: int):
    if isinstance(a, str):
        a = int(a, 2)
    if isinstance(b, str):
        b = int(b, 2)
    return a & b

def bitwise_or(a: int, b: int):
    if isinstance(a, str):
        a = int(a, 2)
    if isinstance(b, str):
        b = int(b, 2)
    return a | b

def left_shift(value, shift_amount: str):
    if isinstance(value, str):
        value = int(value, 2)
    return value << int(shift_amount)



def right_shift(value, shift_amount: str):
    if isinstance(value, str):
        value = int(value, 2)
    return value >> int(shift_amount)


class Memory(dict):

    def __setitem__(self, key, value):
        k = key.strip()
        # self[k] = value
        super().__setitem__(k, value)

memory = Memory()


retry = []

def is_reference(s: str):
    return s.isalpha()

def retry_if_unresolved_refs(s: str, refs: List[str]) -> bool:
    if all(ref in memory for ref in refs):
        return False
    retry.append(s)
    return True


def parse_instruction(s: str):
    if s.startswith('NOT'):

        original_value, target = s[4:].split(' -> ')

        if is_reference(original_value):
            if retry_if_unresolved_refs(s, [original_value]):
                return

            original_value = memory[original_value]
            # print(original_value)
        memory[target] = bitwise_complement(original_value)
        _type = Instruction.NOT
        # print(_type)

    elif "LSHIFT" in s:

        raw_value, r = s.split(' LSHIFT ')

        if is_reference(raw_value):
            if retry_if_unresolved_refs(s, [raw_value]):
                return

        shift_amount, target = r.split(' -> ')
        raw_value = memory[raw_value]
        memory[target] = left_shift(raw_value, shift_amount)        # _type = Instruction.LSHIFT
        _type = Instruction.LSHIFT
        # print(_type)

    elif "RSHIFT" in s:

        raw_value, r = s.split(' RSHIFT ')

        if is_reference(raw_value):
            if retry_if_unresolved_refs(s, [raw_value]):
                return

            raw_value = memory[raw_value]
        shift_amount, target = r.split(' -> ')
        memory[target] = right_shift(raw_value, shift_amount)
        _type = Instruction.RSHIFT
        # print(_type)

    elif "AND" in s:

        nums, target = s.split(' -> ')
        a, b = nums.split(' AND ')

        check = []
        if is_reference(a):
            check.append(a)
            if retry_if_unresolved_refs(s, [a]):
                return
            a = memory[a]

        if is_reference(b):
            check.append(b)
            if retry_if_unresolved_refs(s, [b]):
                return
            b = memory[b]
            
        memory[target] = bitwise_and(a, b)
        _type= Instruction.AND
        # print(_type)
    elif "OR" in s:
        _type= Instruction.OR
        nums, target = s.split(' -> ')
        a, b = nums.split(' OR ')
        if all(is_reference(x) for x in [a, b]):
            if retry_if_unresolved_refs(s, [a, b]):
                return
            a, b = memory[a], memory[b]
        # print(_type)
        memory[target] = bitwise_or(a, b)

    else:
        _type = Instruction.ASSIGN
        value, target = s.split(' -> ')
        if is_reference(value):
            if retry_if_unresolved_refs(s, [value]):
                return
            value = memory[value]
        memory[target] = int(value)

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    # 44430 -> b # part 1
    parse_instruction("3176 -> b") # part 2
    for l in lines:
        parse_instruction(l)
    while retry:
        for i in retry:
            # print(memory)
            parse_instruction(i)
            retry.remove(i)
    print(memory['a'])

if __name__ == "__main__":
    main()
