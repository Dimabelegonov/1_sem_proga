data = list(map(int, input().split()))
a = 10 ** 9
i = 0
while i < len(data) - 1:
    for j in range(i + 1, len(data)):
        if data[j] == min(data[i: len(data)]):
            data[i], data[j] = data[j], data[i]
            print(*data)

    i += 1


