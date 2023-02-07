def func(a):
    arr = []
    while a != 0:
        arr.append(a % 10)
        a = a // 10
    for i in range(len(arr) - 1, 0, -1):
        print(arr[i], "*10^", i, sep="", end=" + ")
    print(arr[0], "*10^", 0, sep="")


a = int(input())
func(a)
