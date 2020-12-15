def chall():
    with open("input", "r") as f:
        c = f.read().split("\n")
    values = {}
    mask = ""
    for i in c:
        if "mask" in i:
            mask = i.split("= ")[1]
        if "mem" in i:
            index = int(i.split("[")[1].split("]")[0])
            value = list(f'{int(i.split("= ")[1]):036b}')
            for x in range(len(mask) + 1):
                x = -1 * x
                if mask[x] != "X":
                    value[x] = mask[x]
            values[index] = int("".join(value), 2)
    print(sum(values.values()))


if __name__ == "__main__":
    chall()
