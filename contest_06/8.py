n = int(input())

data = []
data_1 = []
for _ in range(n):
    a = int(input())
    if a % 2:
        data.append(a)
    else:
        data.append(a)
        data_1.append(a)

data_1.sort()
k = 0
for i in range(len(data)):
    if data[i] % 2 == 0:
        data[i] = data_1[k]
        k += 1

print(*data)
