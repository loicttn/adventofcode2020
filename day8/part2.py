def chall():
    with open("ex", "r") as f:
        c = f.read().split("\n")[:-1]
    acc = 0
    i = 0
    visited = []
    while i < len(c):
        print(visited)
        if i != 0 and i in map(lambda x:x[0], visited):
            for x in range(-1, -1 * len(c), -1):
                if "jmp" in c[visited[x][0]]:
                    print(f"fix {i} to {visited[x][0]+1}")
                    i = visited[x][0] + 1
                    acc = visited[x][1]
                    break
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
