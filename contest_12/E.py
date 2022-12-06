def z_func(s):
    z = [0 for i in range(len(s))]
    r = 0
    l = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


s1 = input()
s2 = input()
s = s1 + "#" + s2
data = z_func(s)
ans = []
for i in range(len(data)):
    if data[i] == len(s1):
        ans.append(i - len(s1) - 1)

if len(ans) > 0:
    print(*ans)
else:
    print(-1)