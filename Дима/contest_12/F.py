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


line = input()
line_plus = line + line[::-1]
# print(line_plus)
ans = z_func(line_plus)
ans = ans[len(line):]
print(*ans[::-1])
