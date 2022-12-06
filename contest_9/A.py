n = int(input())
k = int(input())

data = list(map(int, input().split()))

ans = -1
for i in range(n):
    if data[i] == k:
        ans = i + 1

print(ans)
