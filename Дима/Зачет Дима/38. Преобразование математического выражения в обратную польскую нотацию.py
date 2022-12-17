def to_polska(s):
    res = []
    stack = []
    for ch in list(s):
        if ch in "(/*":
            stack.append(ch)
        elif ch == ")":
            e = stack.pop()
            while e != "(":
                res.append(e)
                e = stack.pop()
        elif ch in "+-":
            if len(stack) > 0:
                e = stack.pop()
                while len(stack) > 0 and e in "/*":
                    res.append(e)
                    e = stack.pop()
                if e in "/*":
                    res.append(e)
                else:
                    stack.append(e)
            stack.append(ch)
        else:
            res.append(ch)
    while len(stack) > 0:
        res.append(stack.pop())

    return res


s = "4*3+5*(7+8)+4*(3-5)"
print(to_polska(s))
