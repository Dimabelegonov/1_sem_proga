def func(a):
    print(" ".join(map(str, a)))
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp

                print(" ".join(map(str, a)))
            else:
                continue


a = input().split()
func(a)
