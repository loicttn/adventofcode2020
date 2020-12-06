def chall():
    with open("input", "r") as f:
        p = f.read().split("\n\n")
    print(sum(map(lambda i: len(set("".join(i.split("\n")))), p)))

if __name__ == "__main__":
    chall()
