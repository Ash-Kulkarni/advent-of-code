import itertools

with open('input.txt', 'r') as file:
    data = file.read().splitlines()

def build_town_map(data) -> dict:
    town_map = {}

    for line in data:
        towns, d = line.split(' = ')
        t1, t2 = towns.split(' to ')
        dist = int(d)
        for t in [t1, t2]:
            if t not in town_map:
                town_map[t] = {}
        town_map[t1][t2] = dist
        town_map[t2][t1] = dist
    return town_map

def calculate_distance(towns, town_map) -> int:
    current = towns[0]
    total = 0
    for t in towns[1:]:
        total += town_map[current][t]
        current = t
    return total

def main():
    town_map = build_town_map(data)
    shortest_flight = None
    longest_flight = None
    for p in itertools.permutations(town_map.keys()):
        total_distance = calculate_distance(p, town_map)
        # if shortest_flight is None or total_distance < shortest_flight:
        #     shortest_flight = total_distance
        if longest_flight is None or total_distance > longest_flight:
            longest_flight = total_distance
    # print(shortest_flight)
    print(longest_flight)

if __name__ == "__main__":
    main()
