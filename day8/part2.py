def chall():
    with open("ex", "r") as f:
        c = f.read().split("\n")[:-1]
    acc = 0
    i = 0
    visited = []
    while i < len(c):
        if i != 0 and list(map(lambda x:x[0], visited)).count(i) >= 3:
            for v in visited:
                if visited.count(v) >= 2:
                    print(v)
                    return
            print(visited)
        visited.append((i, acc))
        inst, val = c[i].split()
        if inst == "acc":
            acc += int(val)
        elif inst == "jmp":
            i += int(val)
            continue
        i += 1
    print(acc)

if __name__ == "__main__":
    chall()
