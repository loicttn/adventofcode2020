def chall():
    with open("input", "r") as f:
        content: List[str] = f.read().split('\n')[:-1]
    res: int = 0
    for c in content:
        r, l, p = c.split()
        r, l = list(map(int,r.split("-"))), l[0]
        if r[0] <= p.count(l) <= r[1]:
            res += 1
    print(res)


if __name__ == "__main__":
    chall()
