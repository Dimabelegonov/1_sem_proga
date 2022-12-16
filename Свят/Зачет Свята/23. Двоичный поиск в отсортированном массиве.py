def func(a, s):
    l, r = 0, len(a) - 1
    while r - l > 0:
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


# Задача про коров

def check(coords, x, k):
    cnt = 1
    last_cow = coords[0]
    for c in coords:
        if c - last_cow >= x:
            cnt += 1
            last_cow = c

    return cnt >= k

def binary_search_answer(coords, k):  # coords - координаты стоил, k - количество коров
    right = coords[-1] - coords[0] + 1
    left = 0
    while right - left > 1:
        mid = (right + left) // 2
        if check(coords, mid, k):
            left = mid
        else:
            right = mid

    return left


print(binary_search_answer([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# Задача про доску

def func1(w, h, n):
    L = max(w, h)
    R = L * n
    while R - L > 1:
        M = (R + L) // 2
        res = (M // w) * (M // h)
        if res < n:
            L = M
        else:
            R = M
    print(R)


w, h, n = int(input()), int(input()), int(input())
func1(w, h, n)
