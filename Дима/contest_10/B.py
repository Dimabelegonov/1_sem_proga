n = int(input())
data = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = 1
for i in range(n):
    if i == 0:
        if data[i] != 1:
            if i + data[i] < n:
                dp[i + data[i]] += dp[i]
    else:
        dp[i] += dp[i - 1]
        if data[i] != 1:
            if i + data[i] < n:
                dp[i + data[i]] += dp[i]

print(dp[n - 1] % 937)
