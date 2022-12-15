# ДОДЕЛАТЬ!
def func(a, s):
    l, r = 0, len(a) - 1
    while l != r:
        m = (l + r) // 2
        if a[m] == s:
            return m
        elif s < a[m]:
            r = m
        elif a[m] < s:
            l = m


a = list(map(int, input().split()))
print(func(a, int(input())))

"""
Временная сложность алгоритма - O(logn) - худший случай, O(1) - лучший случай.
"""

# задача про коров и про доску