with open('input.txt', 'r') as file:
    data = file.read()

def get_digit_runs(data:str) -> list:
    runs = []

    current_digit = data[0]
    current_run = []

    for i, d in enumerate(data):
        if d == current_digit:
            current_run.append(current_digit)
        else:
            runs.append(current_run)
            current_digit = d
            current_run = [current_digit]

            if i != len(data) - 1:
                continue
            runs.append(current_run)

    return runs


def process(runs) -> str:
    res = []
    for r in runs:
        l = len(r)
        n = r[0]
        res.append(f'{l}{n}')
    return "".join(res)

def main():
    input = "1113122113"
    for _ in range(50):
        runs = get_digit_runs(input)
        processed = process(runs)
        input = processed
    print(len(input))

    # print(len(process(runs)))

if __name__ == "__main__":
    main()
