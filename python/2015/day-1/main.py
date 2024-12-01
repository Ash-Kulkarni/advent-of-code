def get_input():
    with open("./input.txt") as f:
        return f.readline()

def main():
    result = 0
    for i, x in enumerate(get_input()):
        match x:
            case "(":
                result += 1
            case ")":
                result -= 1
        if -1 == result:
            print(i)
            break
    print(result)

if __name__ == "__main__":
    main()
