def chall():
    with open("input", "r") as f:
        inst = map(lambda x: (x[0], int(x[1:] if len(x[1:]) else "")), f.read().split("\n")[:-1])
    pp = [0, 0]
    ww = [10, -1]
    for i in inst:
        if i[0] == "L":
            for _ in range(0, i[1], 90):
                ww = [ww[1], ww[0] * -1]
        if i[0] == "R":
            for _ in range(0, i[1], 90):
                ww = [ww[1] * -1, ww[0]]
        if i[0] == "F":
            pp[0] += i[1] * ww[0]
            pp[1] += i[1] * ww[1]
        if i[0] == "N":
            ww[1] -= i[1]
        if i[0] == "S":
            ww[1] += i[1]
        if i[0] == "E":
            ww[0] += i[1]
        if i[0] == "W":
            ww[0] -= i[1]
    print(abs(pp[0]) + abs(pp[1]))

if __name__ == "__main__":
    chall()
