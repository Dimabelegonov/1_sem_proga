"""
Расстояние Левенштейна, или редакционное расстояние - это минимальное количество операций вставки одного символа,
удаления одного символа и замены одного символа на другой, необходимых для превращения одной строки в другую.
"""


def func(a, b):
    data = [[i + j if i * j == 0 else 0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    for j in range(1, len(b) + 1):
        for i in range(1, len(a) + 1):
            if a[i - 1] == b[j - 1]:
                data[j][i] = data[j - 1][i - 1]
            else:
                data[j][i] = min(data[j - 1][i - 1], data[j - 1][i], data[j][i - 1]) + 1
    for x in data:
        print(x)
    return data[-1][-1]


print(func(input(), input()))
