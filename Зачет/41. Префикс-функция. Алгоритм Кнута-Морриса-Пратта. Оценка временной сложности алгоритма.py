def p_func(s):
    p = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]

        if s[i] == s[k]:
            k += 1

        p[i] = k

    return p


def kmp(line, s):
    kmp_line = s + "#" + line
    z = p_func(kmp_line)
    ans = -1
    for i in range(len(kmp_line)):
        if z[i] == len(s):
            ans = abs(i - len(s) * 2)

    return ans


print(kmp("abcabs", "abs"))
