data = list(map(int, input().split()))

i = 0
while i < len(data) - 1:
    j = i + 1
    while j > 0 and data[j] < data[j - 1]:
        data[j], data[j - 1] = data[j - 1], data[j]
        j -= 1
        print(*data)

    i += 1
