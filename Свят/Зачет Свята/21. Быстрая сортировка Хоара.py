def func(a):
    if len(a) <= 1:
        return a
    n = a[len(a) // 2]
    l = []
    c = []
    r = []
    for x in a:
        if x < n:
            l.append(x)
        elif x == n:
            c.append(x)
        elif x > n:
            r.append(x)
    return func(l) + c + func(r)


data = list(map(int, input().split()))
print(func(data))
"""
Временная сложность алгоритма - O(nlogn) - лучший случай, O(n^2) - худший случай.
"""
