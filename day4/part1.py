import re

def chall():
    with open("input", "r") as f:
        passports = f.read().split("\n\n")
    f = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0
    for p in passports:
        p = re.split("\n| |:", p)
        print(p)
        v = []
        for x in f:
            if x in p:
                v.append(x)
        res += (len(v) >= 7 and len(v) == len(set(v)))
    print(res)

if __name__ == "__main__":
    chall()
