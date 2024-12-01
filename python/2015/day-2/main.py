from typing import List

def get_input() -> List[str]:
    with open("./input.txt") as f:
        return f.readlines()

def get_dimensions(dimension_string: str) -> List[int]:
    return [int(x) for x in dimension_string.split("x")]

def get_areas(x,y,z)-> List[int]:
    return [x*y, y*z, z*x]

def get_surface_area(x,y,z) -> int:
    return 2 * sum(get_areas(x,y,z))

def get_smallest_area(x, y, z) -> int:
    return min(get_areas(x,y,z))

def get_volume(x,y,z) -> int:
    return x*y*z

def get_smallest_perimeter(x,y,z) -> int:
    return 2 * min(x+y, y+z, z+x)

def main():
    part_1 = 0
    part_2 = 0
    for dimension_string in get_input():
        x,y,z = get_dimensions(dimension_string)
        part_1 += get_surface_area(x,y,z) + get_smallest_area(x,y,z)
        part_2 += get_volume(x,y,z) + get_smallest_perimeter(x,y,z)

    print(part_1)
    print(part_2)

if __name__ == "__main__":
    main()
