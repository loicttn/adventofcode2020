def chall():
    with open("input", "r") as f:
        content: List[str] = f.read().split('\n')[:-1]
    res: int = 0
    for c in content:
        r, l, p = c.split()
        r, l = list(map(lambda x: int(x) - 1,r.split("-"))), l[0]
        try:
            if p[r[0]] == l and p[r[1]] != l:
                res += 1
            elif p[r[0]] != l and p[r[1]] == l:
                res += 1
        except:
            pass
    print(res)


if __name__ == "__main__":
    chall()
