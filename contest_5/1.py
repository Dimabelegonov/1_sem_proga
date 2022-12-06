n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

k = int(input())

cnt = 0
for i in range(n):
    if data[i] > data[k] and k != i:
        cnt += 1

print(cnt)
