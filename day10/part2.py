from typing import *

def get_nb(s: List[int], i: int, ttl = 0) -> int:
    if i + 1 == len(s): return ttl
    x = s[i + 1] - s[i]
    if x == 3:
        ttl += 1
        return get_nb(s, i + 1)
    if i + 3 < len(s) and s[i + 3] - s[i] <= 3:
        ttl += 3
        get_nb(s, i + 1)
        get_nb(s, i + 2)
        get_nb(s, i + 3)
    elif i + 2 < len(s):
        xx = s[i + 2] - s[i]
        if xx <= 3:
            ttl += 2
            get_nb(s, i + 1)
            get_nb(s, i + 2)
    ttl += 1
    return get_nb(s, i + 1)


def chall():
    with open("input", "r") as f:
        c = sorted(map(lambda x: int(x), f.read().split("\n")[:-1]))
    print(get_nb(c, 0))

if __name__ == "__main__":
    chall()
