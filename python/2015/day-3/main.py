from typing import List


def get_input() -> List[str]:
    with open("./input.txt") as f:
        return f.readlines()

class Santa:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def move(self, direction: str) -> None:
        match direction:
            case "^":
                self.y += 1
            case "v":
                self.y -= 1
            case ">":
                self.x += 1
            case "<":
                self.x -= 1
            case _:
                raise Exception("Invalid direction")

def main():
    [input] = get_input()
    x = 0
    y = 0
    santa = Santa(x,y)
    robo_santa = Santa(x,y)
    real_santa = True
    visits = {(x,y): 1}
    for direction in input:
        real_santa = not real_santa
        s = santa if real_santa else robo_santa

        s.move(direction)
        visits[(s.x, s.y)] = visits.get((s.x, s.y), 0) + 1

    print(len([v for v in visits.values() if v >= 1]))

if __name__ == "__main__":
    main()

