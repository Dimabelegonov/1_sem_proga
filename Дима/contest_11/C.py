n = int(input())
black = []
di = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
for _ in range(n):
    x, y = map(str, input())

    black.append([di[x], int(y)][::-1])

x, y = map(str, input())
white = [di[x], int(y)][::-1]

dp = [[0 for i in range(10)] for j in range(10)]
matrix = [[0 for i in range(10)] for j in range(10)]
for item in black:
    matrix[item[0]][item[1]] = 1

dp[white[0]][white[1]] = 1

for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j + 1]
        else:
            dp[i][j] += dp[i - 1][j]

print(sum(dp[8]))


