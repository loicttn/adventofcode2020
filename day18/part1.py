def e(stack, x= False):
    buff = [None, None, None]
    index = 0
    if not x:
        for t in range(len(stack) - 1, 0, -1):
            if stack[t] == "(":
                index = t
                break
    else:
        index = -1
    for t in range(index + 1, len(stack)):
        t = index + 1
        if buff[0] is None:
            buff[0] = stack.pop(t)
        elif buff[1] is None:
            buff[1] = stack.pop(t)
        elif buff[2] is None:
            buff[-1] = stack.pop(t)
            buff[0] = str(eval("".join(buff)))
            buff[1] = None
            buff[2] = None
    if len(stack):
        stack[-1] = buff[0]
    return stack, buff[0]

def chall():
    with open("input", "r") as f:
        c = f.read().replace("(", " ( ").replace(")", " ) ").replace("*", " * ").replace("+", " + ").replace("-", " - ").replace("/", " / ").split("\n")[:-1]
    stack = []
    res = 0
    for i in c:
        for x in i.split():
            if len(stack) and x == ")":
                stack = e(stack)[0]
                continue
            stack.append(x)
        res += int(e(stack, True)[1])
    print(res)

if __name__ == "__main__":
    chall()
