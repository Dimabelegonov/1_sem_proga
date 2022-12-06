n = int(input())
if n % 2 == 1:
    print(0)
else:
    dp = [0 for i in range(n + 1)]
    dp[2] = 3
    if n == 2:
        print(3)
    else:
        dp[4] = 11
        for i in range(6, n + 1):
            dp[i] = 4 * dp[i - 2] - dp[i - 4]

        print(dp[n])
