def chall():
    with open("input", "r") as f:
        c = sorted(map(lambda x: int(x), f.read().split("\n")[:-1]))
    a = sum([c[i+1] - c[i] == 1 for i in range(len(c) - 1)]) + 1
    b = sum([c[i+1] - c[i] == 3 for i in range(len(c) - 1)]) + 1
    print(a * b)

if __name__ == "__main__":
    chall()
