n = int(input())
data = [[1], [1, 1]]
if n > 1:
    for j in range(1, n):
        arr = [1]
        for i in range(len(data[j]) - 1):
            arr.append(data[j][i] + data[j][i + 1])
        arr += [1]
        data.append(arr)

    for x in data:
        print(*x)
elif n == 1:
    for x in data:
        print(*x)
else:
    print(*data[0])
