def func(m):
    if m == 1:
        return k

    return (k + m - 1) + func(m - 1) + (k + m - 2)


k = int(input())
m = int(input())


print(func(m))
