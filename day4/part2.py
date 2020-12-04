import re

def chall():
    with open("input", "r") as f:
        passports = f.read().split("\n\n")
    f = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0
    for p in passports:
        p = re.split("\n| |:", p)
        v = []
        try:
            for x in range(len(p)):
                if p[x] == "eyr" and not (2020 <= int(p[x+1]) <= 2030): print(p[x]);raise ""
                if p[x] == "hgt" and ("cm" not in p[x+1] or not (150 <= int(p[x+1][:-2]) <= 193)) and ("in" not in p[x+1] or not (59 <= int(p[x+1][:-2]) <= 76)): print(p[x]);raise ""
                if p[x] == "hcl" and (p[x+1][0] != "#" or len(p[x+1]) != 7) and int(p[x+1][1:],16): print(p[x]);raise ""
                if p[x] == "iyr" and (len(p[x+1]) != 4 or not (2010 <= int(p[x+1]) <= 2020)): print(p[x]);raise ""
                if p[x] == "byr" and (len(p[x+1]) != 4 or not (1920 <= int(p[x+1]) <= 2002)): print(p[x]);raise ""
                if p[x] == "ecl" and (len(p[x+1]) != 3 or p[x+1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]): print(p[x]);raise ""
                if p[x] == "pid" and (len(p[x+1]) != 9 or not p[x+1].isdigit()): print(p[x]);raise ""
        except:
            print("invalid", p)
            continue
        for x in f:
            if x in p:
                v.append(x)
        res += (len(v) >= 7 and len(v) == len(set(v)))
    print(res)

if __name__ == "__main__":
    chall()
