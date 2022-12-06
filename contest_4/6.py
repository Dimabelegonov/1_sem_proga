n = int(input())

a, b = 0, 0
for g in range(2, n + 1):
    i = g

    while i % 2 == 0:
        a += 1
        i //= 2

    while i % 5 == 0:
        b += 1
        i //= 5

print(min(a, b))
