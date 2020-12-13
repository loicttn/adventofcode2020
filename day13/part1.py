def chall():
    with open("input", "r") as f:
        c = f.read().split("\n")
    i = int(c[0])
    ids = list(map(lambda x: [int(x), int(x)], filter(lambda x: x != "x", c[1].split(","))))
    for x in range(len(ids)):
        while ids[x][1] < i:
            ids[x][1] += ids[x][0]
    x = min(ids, key=lambda x: x[1])
    print(x[0] * (x[1] - i))

if __name__ == "__main__":
    chall()
