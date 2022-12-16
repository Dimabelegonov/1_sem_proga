def gen(num, m):
    if len(num) == m:
        print(num)
        return

    if len(num) == 0:
        for i in "123456789":
            gen(str(num) + i, m)
    else:
        for i in "0123456789":
            gen(str(num) + i, m)


gen("", 4)
