def get_sum(s: str) -> int:
    if not "X" in s:
        return int(s, 2)
    t = []
    s = list(s)
    for i in range(2**s.count("X")):
        tmp = s.copy()
        i = bin(i).replace("b","")
        while len(i) > s.count("X"): i = i[1:]
        while len(i) < s.count("X"): i = "0" + i
        d = 0
        for x in range(len(s)):
            if "X" == s[x]:
                tmp[x] = i[d]
                d += 1
        t.append(int("".join(tmp), 2))
    return t


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
            index = list(f'{index:036b}')
            value = int(i.split("= ")[1])
            for x in range(len(mask) + 1):
                x = -1 * x
                if mask[x] != "0":
                    index[x] = mask[x]
            for z in get_sum("".join(index)):
                values[z] = value
    print(sum(values.values()))


if __name__ == "__main__":
    chall()
