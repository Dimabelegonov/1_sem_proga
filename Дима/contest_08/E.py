n = int(input())
data = list(map(int, input().split()))
data.sort()
k = n // 2 + 1
ans = 0
i = 0
while k > 0:
    ans += data[i] // 2 + 1
    k -= 1
    i += 1

print(ans)
