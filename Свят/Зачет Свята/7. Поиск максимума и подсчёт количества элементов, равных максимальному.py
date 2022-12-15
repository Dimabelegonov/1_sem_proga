def func(a):
    cnt = 1
    ma = a[0]
    for i in range(1, len(a)):
        if a[i] > ma:
            ma = a[i]
            cnt = 1
        elif a[i] == ma:
            cnt += 1
    return ma, cnt


data = list(map(int, input().split()))
print(func(data))
