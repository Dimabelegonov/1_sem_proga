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


def pi(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]

        if s[i] == s[k]:
            k += 1

        p[i] = k

    return p


s = input()
z = z_func(s)
p = pi(s)
print(z)
print(p)
