import re

def get_nb(bags, colors) -> int:
    r = []
    for x in bags:
        if sum([c in bags[x] for c in colors]) == len(colors):
            r.append(x)
    if len(r) == 0: return 0
    return len(r) + sum([get_nb(bags, [x]) for x in r])



def chall():
    with open("input", "r") as f:
        c = f.read().split(".\n")[:-1]
    print(len(c))
    bags = {}
    for i in c:
        x, y = i.split(" bags contain ")
        if not bags.get(x):
            bags[x] = []
        contains = re.split(" bag, | bags, ", y.strip())
        for d in range(len(contains)):
            if "no" in contains[d][:2]:
                break
            for _ in range(int(contains[d].split()[0])):
                bags[x].append(" ".join(contains[d].split()[1:]).replace("bags", "").replace(" bag", "").strip())
    print(get_nb(bags, ["shiny gold"]))


if __name__ == "__main__":
    chall()
