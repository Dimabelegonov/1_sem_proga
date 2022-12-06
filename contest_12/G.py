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
s = s1 + "#" + 2 * s2
z = z_func(s)
ans = -1
for i in range(len(s)):
    if z[i] == len(s1):
        ans = abs(i - len(s1) - 1 - len(s2))

print(ans)

