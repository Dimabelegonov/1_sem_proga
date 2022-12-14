def check(n, s, f, HANOI_PATH):
    if n > 0:
        if s + f == 4:
            check(n, s, 2, HANOI_PATH)
            check(n, 2, f, HANOI_PATH)
        else:
            check(n - 1, s, 6 - s - f, HANOI_PATH)
            HANOI_PATH.append([n, s, f])
            check(n - 1, 6 - s - f, f, HANOI_PATH)


HANOI_PATH = []

check(N, 1, 3, HANOI_PATH)
