def func(a, n):
    if len(a) == n:
        print(a)
        return
    elif len(a) == 0:
        for i in "123456789":
            func(a + i, n)
    else:
        for i in "0123456789":
            func(a + i, n)


func("", int(input()))
