n = int(input())
data = list(map(int, input().split()))
kr = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = 1
dp[1] = 1 if data[0] == data[1] or kr[0] == data[1] else 0
for i in range(2, n):
    dp[i] += dp[i - 2] if data[i - 2] == data[i] or kr[i - 2] == data[i] else 0
    dp[i] += dp[i - 1] if data[i - 1] == data[i] or kr[i - 1] == data[i] else 0


print(dp[n - 1] % 947)
