def func2(a, b, data):
    s = []
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and data[j][i] == 1 + data[j - 1][i - 1]:
            s.append(a[i - 1])
            i -= 1
            j -= 1
        elif a[i - 1] != b[j - 1]:
            if data[j - 1][i] == max(data[j - 1][i], data[j][i - 1]):
                j -= 1
            elif data[j][i - 1] == max(data[j - 1][i], data[j][i - 1]):
                i -= 1
    s = s[::-1]
    return s


def func1(a):
    b = sorted(a)
    data = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                data[j][i] = data[j - 1][i - 1] + 1
            else:
                data[j][i] = max(data[j - 1][i], data[j][i - 1])
    return func2(a, b, data)


a = list(map(int, input().split()))
print(func1(a))
