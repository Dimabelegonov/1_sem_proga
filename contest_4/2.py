a = int(input())

flag = True
for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        flag = False


if flag:
    print(1)
else:
    print(0)
