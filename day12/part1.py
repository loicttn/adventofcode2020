def chall():
    with open("input", "r") as f:
        inst = map(lambda x: (x[0], int(x[1:] if len(x[1:]) else "")), f.read().split("\n")[:-1])
    poses = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    p = 0
    pp = [0, 0]
    for i in inst:
        if i[0] == "L":
            for _ in range(0, i[1], 90):
                p = (p - 1) % (-1 * len(poses))
        if i[0] == "R":
            for _ in range(0, i[1], 90):
                p = (p + 1) % len(poses)
        if i[0] == "F":
            pp[0] += poses[p][0] * i[1]
            pp[1] += poses[p][1] * i[1]
        if i[0] == "N":
            pp[1] -= i[1]
        if i[0] == "S":
            pp[1] += i[1]
        if i[0] == "E":
            pp[0] += i[1]
        if i[0] == "W":
            pp[0] -= i[1]
    print(abs(pp[0]) + abs(pp[1]))

if __name__ == "__main__":
    chall()
