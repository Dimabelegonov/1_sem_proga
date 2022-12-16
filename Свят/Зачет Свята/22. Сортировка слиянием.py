def merge(l, r):
    result = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    while i < len(l):
        result.append(l[i])
        i += 1
    while j < len(r):
        result.append(r[j])
        j += 1
    return result


def func(a):
    if len(a) < 2:
        return a
    n = len(a) // 2
    l = a[:n]
    r = a[n:]
    l = func(l)
    r = func(r)
    return merge(l, r)


a = list(map(int, input().split()))
print(func(a))

"""
Временная сложность алгоритма - O(nlogn).
"""
