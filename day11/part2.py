def get_map(c):
    check = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    ly, lx = range(len(c)), range(len(c[0]))
    res = [c[i].copy() for i in ly]
    for y in ly:
        for x in lx:
            if c[y][x] == ".": continue
            occ = 0
            for p in check:
                yy, xx = y + p[0], x + p[1]
                while yy in ly and xx in lx:
                    if c[yy][xx] == "#":
                        occ += 1
                        break
                    if c[yy][xx] == "L": break
                    yy += p[0]
                    xx += p[1]
            if c[y][x] == "L" and occ == 0:
                res[y][x] = "#"
            elif c[y][x] == "#" and occ >= 5:
                res[y][x] = "L"
    return res

def chall():
    with open("input", "r") as f:
        c = list(map(lambda x: list(x), f.read().split("\n")[:-1]))
    x = c
    p = [None]
    while x != p:
        p = x.copy()
        x = get_map(x)
    print(sum([i.count("#") for i in x]))


if __name__ == "__main__":
    chall()
