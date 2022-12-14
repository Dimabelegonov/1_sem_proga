s = input()

ans = 0
for i in range(len(s)):
    ans += int(s[i]) * (-10) ** (len(s) - 1 - i)

print(ans)
