s = list(map(str, input().split()))

ans = 0

for i in range(len(s)):
    a = s[i].count(".")
    b = s[i].count("|")

    ans += (a + b * 5) * 20 ** (len(s) - 1 - i)


print(ans)
