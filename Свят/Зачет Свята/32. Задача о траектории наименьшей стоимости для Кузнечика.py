def func(a):
    """
    Нахождение
    """
    s = [a[0]]
    for i in range(1, len(a)):
        if i == 1:
            s.append(a[i] + s[i - 1])
        else:
            s.append(min(s[i - 1], s[i - 2]) + a[i])
    print(s)

    """
    Восстановление
    """
    path = [len(a) - 1]
    while path[-1] != 0:
        i = path[-1]
        if s[i - 1] < s[i - 2]:
            path.append(i - 1)
        else:
            path.append(i - 2)
    print(path[::-1])


a = list(map(int, input().split()))
func(a)
