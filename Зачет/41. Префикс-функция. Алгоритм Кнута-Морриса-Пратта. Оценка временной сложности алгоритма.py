def p_func(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]

        if s[i] == s[k]:
            k += 1

        p[i] = k

    return p


def z_func(s):
    z = [0 for i in range(len(s))]
    l = 0
    r = 0

    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i, z[i - l])

        while i + z[i] < len(s) and s[z[i]] == s[z[i] + i]:
            z[i] += 1

        if i + z[i] > r:
            l = i
            r = i + z[i]

    return z


def kmp(line, s):
    kmp_line = s + "#" + line
    z = z_func(kmp_line)
    ans = -1
    for i in range(len(kmp_line)):
        if z[i] == len(s):
            ans = abs(i - len(s) - 1)

    return ans


print(kmp("abcabs", "abs"))
