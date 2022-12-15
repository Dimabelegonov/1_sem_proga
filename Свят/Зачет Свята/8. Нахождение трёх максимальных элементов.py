def func(a):
    m1 = float("-inf")
    m2 = float("-inf")
    m3 = float("-inf")
    for i in range(len(a)):
        if a[i] >= m1:
            m1, m2, m3 = a[i], m1, m2
        elif a[i] >= m2:
            m2, m3 = a[i], m2
        elif a[i] >= m3:
            m3 = a[i]
    print(m1, m2, m3)


a = list(map(int, input().split()))
func(a)
