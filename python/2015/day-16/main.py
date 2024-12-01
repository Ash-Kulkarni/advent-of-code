with open("input.txt") as f:
    data = f.readlines()

sues = {}
for line in data:
    sue, rest = line.split(":", 1)
    sue_num = int(sue.split()[1])
    scan = {}
    for item in rest.split(","):
        key, value = item.split(":")
        scan[key.strip()] = int(value)
    sues[sue_num] = scan


matching_sue = {
    "children": 3,
    "cats": 7, # more than 7
    "samoyeds": 2,
    "pomeranians": 3, # less than 3
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5, # less than 5
    "trees": 3, # more than 3
    "cars": 2,
    "perfumes": 1
}
def test_scan(matching_sue, scan):
    for k, v in matching_sue.items():
        if not k in scan:
            continue
        if k in ["cats", "trees"]:
            if not scan[k] > v:
                return False
            
        elif k in ["pomeranians", "goldfish"]:
            if not scan[k] < v:
                return False
        elif not scan[k] == v:
            return False
    return True

for sue_num, scan in sues.items():
    if test_scan(matching_sue, scan):
        print(sue_num)
        break

