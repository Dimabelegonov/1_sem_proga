n = int(input())
m = int(input())
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())

c = int(input())
dp = [[0 for j in range(m)] for i in range(n)]
dp[0][0] = c
for i in range(0, n):
    for j in range(0, m):
        if i != 0 or j != 0:
            if j > 0 and i > 0:
                dp[i][j] = max(dp[i - 1][j] - matrix[i][j], dp[i][j - 1] - matrix[i][j])
            elif i == 0:
                dp[i][j] = dp[i][j - 1] - matrix[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] - matrix[i][j]

# for i in matrix:
#     print(*i)
#
# for i in dp:
#     print(*i)

if dp[n - 1][m - 1] >= 0:
    print(dp[n - 1][m - 1])
else:
    print("Impossible")
