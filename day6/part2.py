def chall():
    with open("input", "r") as f:
        p = f.read().split("\n\n")
    res = 0
    for i in p:
        c = {}
        for z in filter(lambda x: len(x), i.split("\n")):
            for cc in z:
                if c.get(cc):
                    c[cc] += 1
                else:
                    c[cc] = 1
        for x in c:
            if c[x] == len(list(filter(lambda x: len(x), i.split("\n")))):
                res += 1
    print(res)


if __name__ == "__main__":
    chall()
