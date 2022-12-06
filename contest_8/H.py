n = int(input())
data = list(map(int, input().split()))

for _ in range(n):
    i = 1
    j = 0
    k = 0
    while i < len(data):
        if data[j] >= 0 and data[i] >= 0:
            if data[j] > data[i]:
                data[j], data[i] = data[i], data[j]
                print(*data)
            j = i
            i += 1

        elif data[k] < 0 and data[i] < 0:
            if data[k] < data[i]:
                data[k], data[i] = data[i], data[k]
                print(*data)
            k = i
            i += 1

        else:
            if data[i] >= 0 and data[j] < 0:
                j = i
                i += 1
            elif data[i] < 0 and data[k] >= 0:
                k = i
                i += 1
