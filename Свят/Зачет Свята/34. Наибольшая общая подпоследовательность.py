def func2(a, b, data):
    s = []
    i = len(a)
    j = len(b)
    while i > 0 and j > 0:
        if data[j][i] == data[j - 1][i - 1] + 1 and a[i - 1] == b[j - 1]:
            s.append(a[i - 1])
            i += -1
            j += -1
        elif a[i - 1] != b[j - 1]:
            if data[j][i - 1] == max(data[j][i - 1], data[j - 1][i]):
                j += 0
                i += -1
            elif data[j - 1][i] == max(data[j][i - 1], data[j - 1][i]):
                j += -1
                i += 0
    '''
    Если совпадение элементов произошло сверху то в какой-то момент data[j][i - 1] (слева) < data[j - 1][i](сверху).
    И мы передвигаемся наверх
    '''

    h = ''
    for x in s:
        h = str(x) + h
    return h


def func1(a, b):
    data = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                data[j][i] = data[j - 1][i - 1] + 1
            else:
                data[j][i] = max(data[j - 1][i], data[j][i - 1])
    for x in data:
        print(x)
    return func2(a, b, data)


print(func1(input(), input()))
