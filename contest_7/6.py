def func(a, n):
    print(*data[a:n])

    if n - a != 1:
        func(a + 1, n)


def main(n):
    if n == len(data) + 1:
        return

    func(0, n)
    main(n + 1)


data = list(map(str, input().split()))
main(1)

