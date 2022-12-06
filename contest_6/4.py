data = list(map(int, input().split()))

for _ in range(len(data)):
    for i in range(len(data) - 1):
        if data[i + 1] < data[i]:
            data[i], data[i + 1] = (data[i + 1], data[i])
            print(*data)
