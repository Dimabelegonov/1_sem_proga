cnt = 0
k = 10 ** 9

n = int(input())
while n != 0:
    if n < k:
        k = n
        cnt = 1
    elif n == k:
        cnt += 1

    n = int(input())

print(cnt)
