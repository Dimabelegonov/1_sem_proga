def func(n, x, y, x1, y1):
    if n == 3:
        return -1

    if x < 1 or x > 8 or y < 1 or y > 8:
        return -1

    if x == x1 and y == y1:
        return n

    data = [func(n + 1, x + 1, y + 2, x1, y1),
            func(n + 1, x + 1, y - 2, x1, y1),
            func(n + 1, x - 1, y + 2, x1, y1),
            func(n + 1, x - 1, y - 2, x1, y1),
            func(n + 1, x + 2, y + 1, x1, y1),
            func(n + 1, x + 2, y - 1, x1, y1),
            func(n + 1, x - 2, y + 1, x1, y1),
            func(n + 1, x - 2, y - 1, x1, y1)]

    return max(data)


x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
print(func(0, x, y, x1, y1))


