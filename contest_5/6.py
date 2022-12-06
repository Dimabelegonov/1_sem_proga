def prime(n):
    data = []
    isprime = [True for i in range(n + 1)]

    for i in range(2, n + 1):
        if isprime[i]:
            data.append(i)
            for j in range(i, n + 1, i):
                if j != i:
                    isprime[j] = False

    return data


n = int(input())
erat = prime(n)
for i in range(len(erat)):
    print(erat[i], end=" ")
