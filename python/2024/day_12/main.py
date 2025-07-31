def get_input() -> list[str]:
    with open("input.txt", "r") as file:
        return file.read().strip().splitlines()


def parse_input(input_data: list[str]) -> dict[tuple[int, int], str]:
    data = {}
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            data[(x, y)] = char
    return data


def neighbors(point: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = point
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return [(x + dx, y + dy) for dx, dy in directions]


def get_regions(data: dict[tuple[int, int], str]) -> dict[str, set[tuple[int, int]]]:
    all_points = set()
    regions = []
    for (x, y), char in data.items():
        if (x, y) in all_points:
            continue
        region = set()
        queue = [(x, y)]
        while queue:
            current = queue.pop()
            if current in region:
                continue

            region.add(current)

            for n in neighbors(current):
                if (n) in data and n not in region and data[n] == char:
                    queue.append(n)
        regions.append(region)
        all_points |= region
    return regions


def get_region_area(region: set[tuple[int, int]]) -> int:
    return len(region)


def get_region_perimeter(region: set[tuple[int, int]]) -> int:
    perimeter = 0
    for point in region:
        for n in neighbors(point):
            if n not in region:
                perimeter += 1
    return perimeter


def get_region_number_of_sides(region: set[tuple[int, int]]) -> int:
    # number of sides is equal to the number of corners
    # 2 adjacent sides that don't match (normal corner)
    # or 2 adjacent sides that match but diagonal that doesn't match (internal corner)
    num_sides = 0
    for x, y in region:
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbor_x = (x + dx, y)
            neighbor_y = (x, y + dy)
            neighbor_dia = (x + dx, y + dy)

            if neighbor_x not in region and neighbor_y not in region:
                num_sides += 1
            if (
                neighbor_x in region
                and neighbor_y in region
                and neighbor_dia not in region
            ):
                num_sides += 1
    return num_sides


def part_1():
    print(
        sum(
            get_region_area(r) * get_region_perimeter(r)
            for r in get_regions(parse_input(get_input()))
        )
    )


def part_2():
    print(
        sum(
            get_region_area(r) * get_region_number_of_sides(r)
            for r in get_regions(parse_input(get_input()))
        )
    )


part_1()

part_2()
