import re
import itertools

# Carol would gain 29 happiness units by sitting next to Mallory.
# David would gain 67 happiness units by sitting next to Alice.
# David would gain 25 happiness units by sitting next to Bob.

def get_data():
    pattern = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).')
    with open("input.txt") as f:
        data = f.read()
    for m in re.finditer(pattern, data):
        yield m.groups()

def get_seating_values():
    pair_total_values = {}

    for (p1, gain_or_loss, value, p2) in get_data():
        pair = tuple(sorted([p1, p2]))
        if pair not in pair_total_values:
            pair_total_values[pair] = 0
        if gain_or_loss == "gain":
            pair_total_values[pair] += int(value)
        elif gain_or_loss == "lose":
            pair_total_values[pair] -= int(value)

    unq_people = set()
    for p1, p2 in pair_total_values.keys():
        unq_people.add(p1)
        unq_people.add(p2)
    for p in unq_people:
        pair = tuple(sorted(["me", p]))
        pair_total_values[pair] = 0
    unq_people = unq_people.union({"me"})

    return pair_total_values, unq_people

def get_seating_arrangement_happiness(arrangement, seating_values):
    total = 0
    for i, p in enumerate(arrangement):
        if i == 0:
            p1 = arrangement[-1]
        else:
            p1 = arrangement[i-1]
        p2 = p
        key = tuple(sorted([p1, p2]))
        total += seating_values[key]
    return total

seating_values, unq_people = get_seating_values()
seating_arrangements = itertools.permutations(unq_people)
max_happiness = max(get_seating_arrangement_happiness(sa, seating_values) for sa in seating_arrangements)
print(max_happiness)
