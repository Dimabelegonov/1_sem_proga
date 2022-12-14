n = int(input())
data = list(map(int, input().split()))
ans = []
for i in range(1, n - 1):
    if (data[i - 1] < data[i] and data[i + 1] < data[i]) or \
            (data[i - 1] > data[i] and data[i + 1] > data[i]):
        ans.append(i)

print(*ans)
