from typing import *

def get_seat(p: str) -> Tuple[int, int, int]:
    r = range(0, 128)
    for i in p[:-3]:
        if i == "F": r = r[:int(len(r)/2)]
        if i == "B": r = r[int(len(r)/2):]
    c = range(0, 7)
    for i in p[-3:]:
        if i == "L": c = c[:int(len(c)/2)]
        if i == "R": c = c[int(len(c)/2):]
    if not len(c): c = [0]
    return [r[0], c[0] + 1, r[0] * 8 + c[0] + 1]

def chall():
    with open("input", "r") as f:
        passes: List[str] = f.read().split("\n")
    print(max(map(lambda p: get_seat(p), passes), key=lambda p: p[2])[2])

if __name__ == "__main__":
    chall()
