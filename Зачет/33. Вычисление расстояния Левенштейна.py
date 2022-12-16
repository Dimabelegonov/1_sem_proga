"""
Расстояние Левенштейна, или редакционное расстояние - это минимальное количество операций вставки одного символа,
удаления одного символа и замены одного символа на другой, необходимых для превращения одной строки в другую.
"""


def levenshtein(a, b):
    n1 = len(a)
    n2 = len(b)

    dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(n1):
        dp[i + 1][0] = i + 1

    for j in range(n2):
        dp[0][j + 1] = j + 1

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j])

    return dp[-1][-1]
