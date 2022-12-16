def func(a):
    res = []
    stack = []
    for i in range(len(a)):
        if a[i] in "(/*":
            stack.append(a[i])
        elif a[i] == ")":
            e = stack.pop()
            while e != "(":
                res.append(e)
                e = stack.pop()
        elif a[i] in "+-":
            if len(stack) > 0:
                e = stack.pop()
                while e in "*/" and len(stack) > 0:
                    res.append(e)
                    e = stack.pop()
                if e in "*/":
                    res.append(e)
                else:
                    stack.append(e)
            stack.append(a[i])
        else:
            res.append(a[i])
    while len(stack) > 0:
        res.append(stack.pop())
    return res


a = input().split()
print(*func(a))
