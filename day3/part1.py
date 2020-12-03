def chall():
    with open("input", "r") as f:
        m: List[str] = f.read().split("\n")[:-1]
    print(sum([l[(i * 3) % len(m[0])] == "#" for i, l in enumerate(m)]))

if __name__ == "__main__":
    chall()
