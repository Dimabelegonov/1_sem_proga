n = int(input())
n_max = 0
cnt = 0
while n != 0:
    if n_max < n:
        n_max = n
        cnt = 1
    elif n_max == n:
        cnt += 1

    n = int(input())

print(cnt)
