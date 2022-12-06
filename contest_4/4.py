def prime(n):
    data = []
    isprime = [True for i in range(10 ** 5)]

    for i in range(2, 10 ** 5):
        if isprime[i]:
            data.append(i)
            for j in range(i, 10 ** 5, i):
                if j != i:
                    isprime[j] = False

    print(data[n])


prime(int(input()) - 1)

