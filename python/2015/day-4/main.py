import hashlib


def get_input() -> str:
    with open("./input.txt") as f:
        return f.readlines()[0]

def encode(s: str) -> bytes:
    return s.encode("utf-8")

def main():

    # input = get_input()
    input="bgvyzdsv"


    i = 0
    while True:
        s = input + str(i)
        e = encode(s)
        # print(s)
        res = hashlib.md5(e)
        if res.hexdigest().startswith("000000"):

            print(i)
            print(res.hexdigest())
            break
        i+=1

if __name__ == "__main__":
    main()
