def lis(s1):
    return lcs(s1, sorted(list(set(s1))))


def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # for i in dp:
    #     print(*i)
    answer = get_str(dp, s2)

    return answer


def get_str(dp, s2):
    k = dp[-1][-1]
    ans = []
    i = len(dp) - 1
    j = len(dp[0]) - 1
    while i > 0 and j > 0:
        if dp[i][j - 1] == k:
            j -= 1
        elif dp[i - 1][j] == k:
            i -= 1
        elif dp[i - 1][j - 1] == k - 1:
            k -= 1
            ans.append(s2[j - 1])
            i -= 1
            j -= 1

    return ans[::-1]


print(lis([3, 4, 5, 7, 6, 4, 2, 1, 5, 6]))
