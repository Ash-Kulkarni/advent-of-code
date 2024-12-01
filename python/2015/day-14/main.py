import re
from typing import NamedTuple

class Reindeer(NamedTuple):
    name: str
    speed: int
    fly_time: int
    rest_time: int

    def get_distance(self, time: int):
        cycle_time = self.fly_time + self.rest_time
        num_cycles = time // cycle_time
        cycle_distance = num_cycles * self.speed * self.fly_time

        remaining_time = time % cycle_time
        fly_time = min(remaining_time, self.fly_time)
        return cycle_distance + fly_time * self.speed

def parse_reindeer(line):
    pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    name, speed, fly_time, rest_time = re.match(pattern, line).groups()
    return Reindeer(name, int(speed), int(fly_time), int(rest_time))

def read_input():
    with open("input.txt") as f:
        data = f.read()
    return data.splitlines()


def main():
    input = read_input()
    time = 2503
    reindeers = [parse_reindeer(line) for line in input]
    reindeer_points = {r: 0 for r in reindeers}
    for i in range(1, time + 1):
        leading_reindeers = []
        max_distance = 0
        for r in reindeers:
            d = r.get_distance(i)
            if d > max_distance:
                max_distance = d
                leading_reindeers = [r]
            elif d == max_distance:
                leading_reindeers.append(r)
        for r in leading_reindeers:
            reindeer_points[r] += 1
    for r, points in reindeer_points.items():
        print(f"{r.name}: {points}")

if __name__ == "__main__":
    main()
