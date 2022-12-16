def z_func(s):
    z = [0 for i in range(len(s))]
    l = 0
    r = 0

    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < len(s) and s[z[i]] == s[z[i] + i]:
            z[i] += 1

        if i + z[i] > r:
            l = i
            r = i + z[i] - 1

    return z

