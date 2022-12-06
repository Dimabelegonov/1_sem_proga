n = int(input())

b = []

while n // 60 > 0:
    x = n % 60
    y = x // 10
    z = n % 10

    b.append("<" * y + "v" * z)

    n //= 60

x = n % 60
y = x // 10
z = x % 10

b.append("<" * y + "v" * z)

print(".".join([b[i] for i in range(len(b) - 1, -1, -1)]))

