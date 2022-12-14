s = list(map(str, input().split(".")))

ans = 0

for i in range(len(s)):
    a = s[i].count("<")
    b = s[i].count("v")

    ans += (b + a * 10) * 60 ** (len(s) - 1 - i)


print(ans)
