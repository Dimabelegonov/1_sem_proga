def func(a):
    print(" ".join(map(str, a)))
    for i in range(len(a)):
        for j in range(1, len(a) - i):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                print(" ".join(map(str, a)))
            else:
                continue


a = input().split()
func(a)
