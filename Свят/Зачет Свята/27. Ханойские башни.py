def hanoi(i, j, n):
    if n == 1:
        print("Move disk 1 from pin", i, "to", j)
    else:
        tmp = 6 - i - j
        hanoi(i, tmp, n - 1)
        print("Move disk", n, "from pin", i, "to", j)
        hanoi(tmp, j, n - 1)


i, j, n = int(input()), int(input()), int(input())
hanoi(i, j, n)

"""
Временная сложность алгоритма - O(2^n)
"""
