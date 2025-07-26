def get_map():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


class Simulation:
    def __init__(self, map: list[str]):
        self.map = map
        self.size_y = len(map)
        self.size_x = len(map[0])
        self.guard_dir = "N"
        self.guard_pos = self.get_starting_point()

    def get_starting_point(self):
        for i in range(self.size_y):
            for j in range(self.size_x):
                if self.map[i][j] == "^":
                    return [i, j]
        raise ValueError("no guard on map")

    def step(self):
        if self.guard_is_blocked():
            self.turn_guard_cw()
        self.move_guard_forward()

    def guard_leaving_map(self):
        gy, gx = self.guard_pos
        if (
            self.guard_dir == "N"
            and gy == 0
            or self.guard_dir == "E"
            and gx == self.size_x - 1
            or self.guard_dir == "S"
            and gy == self.size_y - 1
            or self.guard_dir == "W"
            and gx == 0
        ):
            return True
        return False

    def guard_is_blocked(self):
        gy, gx = self.guard_pos
        if (
            (self.guard_dir == "N" and self.map[gy - 1][gx] == "#")
            or (self.guard_dir == "E" and self.map[gy][gx + 1] == "#")
            or (self.guard_dir == "S" and self.map[gy + 1][gx] == "#")
            or (self.guard_dir == "W" and self.map[gy][gx - 1] == "#")
        ):
            return True

    def turn_guard_cw(self):
        if self.guard_dir == "N":
            self.guard_dir = "E"
        elif self.guard_dir == "E":
            self.guard_dir = "S"
        elif self.guard_dir == "S":
            self.guard_dir = "W"
        elif self.guard_dir == "W":
            self.guard_dir = "N"
        else:
            raise ValueError("unknown guard dir", self.guard_dir)

    def move_guard_forward(self):
        gy, gx = self.guard_pos
        r = self.map[gy]
        self.map[gy] = r[:gx] + "X" + r[gx + 1 :]
        if self.guard_dir == "N":
            self.guard_pos[0] -= 1
        elif self.guard_dir == "E":
            self.guard_pos[1] += 1
        elif self.guard_dir == "S":
            self.guard_pos[0] += 1
        elif self.guard_dir == "W":
            self.guard_pos[1] -= 1
        else:
            raise ValueError("unknown guard dir", self.guard_dir)

    def run(self):
        while not self.guard_leaving_map():
            self.step()
        print(sum([1 for r in self.map for c in r if c == "X"]) + 1)


s = Simulation(get_map())
s.run()
