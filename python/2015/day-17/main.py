import itertools

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

containers = list(map(int, data))
combinations = itertools.chain.from_iterable(itertools.combinations(containers, r) for r in range(1, len(containers) + 1))

min_num_containers = 0
valid_combinations = []
for c in combinations:
    if sum(c) != 150:
        continue
    num_containers = len(c)
    if min_num_containers == 0 or num_containers < min_num_containers:
        min_num_containers = num_containers
        valid_combinations = [c]
    elif num_containers == min_num_containers:
        valid_combinations += [c]

print(len(valid_combinations))
