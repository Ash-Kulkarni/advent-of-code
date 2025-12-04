from pydantic import BaseModel
from collections import namedtuple
import itertools
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np


def get_input(mock) -> list[str]:
    with open("mock.txt" if mock else "input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def get_grid_size(mock) -> tuple[int, int]:
    if mock:
        return 11, 7
    else:
        return 101, 103


Quadrants = namedtuple(
    "Quadrants", ["top_left", "top_right", "bottom_left", "bottom_right"]
)


class Robot(BaseModel):
    position: tuple[int, int]
    velocity: tuple[int, int]
    grid_size: tuple[int, int]

    def get_next_position(self) -> int:
        displacement_x = self.position[0] + self.velocity[0]
        displacement_y = self.position[1] + self.velocity[1]
        # print(
        #     f"Robot {self.position} with velocity {self.velocity} has displacement ({displacement_x}, {displacement_y})"
        # )
        if 0 <= displacement_x < self.grid_size[0]:
            next_x = displacement_x
        elif displacement_x < 0:
            next_x = self.grid_size[0] + displacement_x
        else:
            next_x = displacement_x % self.grid_size[0]

        if 0 <= displacement_y < self.grid_size[1]:
            next_y = displacement_y
        elif displacement_y < 0:
            next_y = self.grid_size[1] + displacement_y
        else:
            next_y = displacement_y % self.grid_size[1]

        # print(
        #     f"Robot {self.position} with velocity {self.velocity} moves to ({next_x}, {next_y})"
        # )
        return next_x, next_y

    def step(self):
        self.position = self.get_next_position()


def parse_line(line: str, grid_size: tuple[int, int]) -> Robot:
    p_str, v_str = line.split(" ")
    return Robot(
        position=tuple(map(int, p_str[2:].split(","))),
        velocity=tuple(map(int, v_str[2:].split(","))),
        grid_size=grid_size,
    )


def get_quadrants(
    robots: list[Robot], grid_size: tuple[int, int]
) -> list[tuple[int, int]]:
    # skip middle row and column
    mid_x = grid_size[0] // 2
    mid_y = grid_size[1] // 2

    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0

    for r in robots:
        if r.position[0] < mid_x and r.position[1] < mid_y:
            top_left += 1
        elif r.position[0] > mid_x and r.position[1] < mid_y:
            top_right += 1
        elif r.position[0] < mid_x and r.position[1] > mid_y:
            bottom_left += 1
        elif r.position[0] > mid_x and r.position[1] > mid_y:
            bottom_right += 1
        else:
            # ignore robots on the middle row and column
            ...

    return Quadrants(
        top_left=top_left,
        top_right=top_right,
        bottom_left=bottom_left,
        bottom_right=bottom_right,
    )


def show_grid(robots: list[Robot], grid_size: tuple[int, int], without_center=False):
    grid = [["." for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for r in robots:
        x, y = r.position
        if grid[y][x] == ".":
            grid[y][x] = "1"
        else:
            grid[y][x] = str(int(grid[y][x]) + 1)
    mid_x = grid_size[0] // 2
    mid_y = grid_size[1] // 2
    for i in range(grid_size[1]):
        for j in range(grid_size[0]):
            if without_center and (i == mid_y or j == mid_x):
                grid[i][j] = " "

    for row in grid:
        print(" ".join(row))
    print("\n")


def step_robots(robots: list[Robot], steps: int):
    for _ in range(steps):
        for r in robots:
            r.step()


def part_1():
    mock = False
    input = get_input(mock)
    grid_size = get_grid_size(mock)
    robots = [parse_line(line, grid_size) for line in input]
    step_robots(robots, 100)

    factor = 1
    for name, q in zip(
        ["Top Left", "Top Right", "Bottom Left", "Bottom Right"],
        get_quadrants(robots, grid_size),
    ):
        print(f"{name}: {q}")
        factor *= q
    print(f"Part 1: {factor}")


def part_2():
    mock = False
    input_data = get_input(mock)
    grid_size = get_grid_size(mock)
    robots = [parse_line(line, grid_size) for line in input_data]
    for _ in range(40):
        for r in robots:
            r.step()

    fig, ax = plt.subplots()
    ax.set_xlim(0, grid_size[0])
    ax.set_ylim(0, grid_size[1])
    ax.set_aspect("equal")
    scatter = ax.scatter([], [], s=10)

    def update(frame):
        for r in robots:
            r.step()
        positions = np.array([r.position for r in robots])
        scatter.set_offsets(positions)
        ax.set_title(f"Step {frame}")
        return (scatter,)

    anim = FuncAnimation(fig, update, frames=10, interval=1000)

    anim.save("robots.gif", writer=PillowWriter(fps=10))


part_1()
part_2()
