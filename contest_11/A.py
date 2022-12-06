x, y = map(int, input().split())
dp = [[0 for i in range(10)] for j in range(10)]
dp[y][x] = 1
for i in range(y, 9):
    for j in range(1, 9):
        dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[-2]))


