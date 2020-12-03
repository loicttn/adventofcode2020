def chall():
    with open("input", "r") as f:
        m: List[str] = f.read().split("\n")[:-1]
    res = sum([l[i % len(m[0])] == "#" for i, l in enumerate(m)]) * \
        sum([l[(i * 3) % len(m[0])] == "#" for i, l in enumerate(m)]) * \
        sum([l[(i * 5) % len(m[0])] == "#" for i, l in enumerate(m)]) * \
        sum([l[(i * 7) % len(m[0])] == "#" for i, l in enumerate(m)]) * \
        sum([l[int(i / 2) % len(m[0])] == "#" and i % 2 == 0 for i, l in enumerate(m)])
    print(res)


if __name__ == "__main__":
    chall()
