def work(n, start, finish, HANOI_PATH):
    if n > 0:
        if start + finish == 4:
            work(n, start, 2, HANOI_PATH)
            work(n, 2, finish, HANOI_PATH)
        else:
            work(n - 1, start, 6 - start - finish, HANOI_PATH)
            HANOI_PATH.append([n, start, finish])
            work(n - 1, 6 - start - finish, finish, HANOI_PATH)


HANOI_PATH = list()
# N = int(input())
work(N, 1, 3, HANOI_PATH)
# print(HANOI_PATH)
