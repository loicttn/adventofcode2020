def chall():
    content: List[int] = []
    with open("input", "r") as f:
        content = list(map(int, filter(lambda x: len(x) != 0,f.read().split("\n"))))
    for x in content:
        for y in content[1:]:
            if x + y == 2020:
                print(x * y)
                return


if __name__ == "__main__":
    chall()
