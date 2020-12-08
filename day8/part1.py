def chall():
    with open("input", "r") as f:
        c = f.read().split("\n")
    acc = 0
    i = 0
    visited = []
    while i < len(c):
        if i != 0 and i in visited:
            print(acc)
            break
        visited.append(i)
        inst, val = c[i].split()
        if inst == "acc":
            acc += int(val)
        elif inst == "jmp":
            i += int(val)
            continue
        i += 1

if __name__ == "__main__":
    chall()
