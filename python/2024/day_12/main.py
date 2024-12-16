with open('test_input.txt') as f:

    grid = [x.strip().split('\n')[0] for x in f.readlines()]

for g in grid:
    print(g)

    
y, x = 0, 0



def grid_size(grid):
    return len(grid), len(grid[0])

def in_grid(y, x, size_y, size_x):
    if y < 0 or x < 0:
        return False

    if y >= size_y or x >= size_x:
        return False

    return True


def go_east(y, x):
    return y, x + 1

def go_south(y, x):
    return y+1, x
def go_west(y, x):
    return y, x - 1

def go_north(y, x):
    return y-1, x

size = grid_size(grid)
y_size, x_size = size
def get_next_coords(y, x):
    next_coords = [fn(y, x) for fn in [go_east, go_south, go_west, go_north]]
    return [c for c in next_coords if in_grid(*c, y_size, x_size)]


seen = {}


def get_all_coordinates(size):
    all_coords = set()
    y_size, x_size = size
    for j in range(0, y_size):
        for i in range(0, x_size):
            all_coords.add((j, i))
    return all_coords



def subtract_coordinates(total, coords):
    return total - coords

def find_connected_component(char, component_num, coords):
    # current_char = grid[y, x]
    key = (char, component_num)
    if (key) not in seen:
        seen[key] = set()

    for y, x in coords:
        

        if (y,x) in seen[key]:
            continue
        
        this_char = grid[y][x]
        if this_char == char:
            seen[key].add((y,x))
            find_connected_component(char, component_num, get_next_coords(y,x))
            

    return seen[key]

remaining_coords = get_all_coordinates(size)
component_num = 0
while len(remaining_coords) != 0:
    y, x = next(iter(remaining_coords))
    start_char = grid[y][x]
    found_coords = find_connected_component(start_char, component_num, [(y,x)])
    remaining_coords = subtract_coordinates(remaining_coords, found_coords)
    if not remaining_coords:
        break
    component_num +=1 

print(seen)
