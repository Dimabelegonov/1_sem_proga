n = int(input())
data = [int(input()) for i in range(n)]
dp = [0 for i in range(n)]
dp[0] = 0
if n == 1:
    print(0)
else:
    dp[1] = abs(data[0] - data[1])
    for i in range(2, n):
        a = abs(data[i - 1] - data[i])
        b = 3 * abs(data[i - 2] - data[i])
        dp[i] = min(a + dp[i - 1], b + dp[i - 2])

    print(dp[n - 1])
