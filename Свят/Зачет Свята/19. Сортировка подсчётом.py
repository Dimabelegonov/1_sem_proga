data = list(map(int, input().split()))
a = [0] * (max(data) + 1)
for x in data:
    a[x] += 1
data.clear()
for i in range(len(a)):
    for x in range(a[i]):
        data.append(i)
print(data)

"Временная сложность алгоритма - O(n+k), где k - максимальное чилос в массиве"
