n = int(input())
data = [0] * n
arr = list(map(int, input().split()))
data[0] = arr[0]
data[1] = arr[1]
for i in range(2, n):
    data[i] = arr[i] + min(data[i - 1], data[i - 2])

print(min(data[-1], data[-2]))
