def din(a):
    s = [1 if a[0]!=0 else 0]
    for i in range(1, len(a)):
        if i == 1:
            if a[i] != 0:
                s.append(s[i - 1])
            else:
                s.append(0)
        else:
            if a[i] == 0:
                s.append(0)
            else:
                s.append(s[i - 1] + s[i - 2])
    return s[-1]


def rec(a, i, step):
    if i == 0 and a[i]!=0:
        return 1
    elif i < 0:
        return 0
    if a[i] == 0:
        return 0
    else:
        return rec(a, i - 1, step + 1) + rec(a, i - 2, step + 1)

a = list(map(int, input().split()))
print(din(a))
print(rec(a, len(a) - 1, 0))
