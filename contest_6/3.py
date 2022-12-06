data = list(list(map(int, input().split())))

i = 0
while i < len(data) - 1:
    if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        print(*data)
        i = 0
    else:
        i += 1
