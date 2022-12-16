def z_func(s):
    z = [0 for i in range(len(s))]
    l = 0
    r = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i, z[i - l])

        while z[i] + i < len(s) and s[i + z[i]] == s[z[i]]:
            z[i] += 1

        if z[i] + i > r:
            r = z[i] + i
            l = i

    return z


print(z_func("aaaa"))
