flag = True
x = int(input())
while x != 0 and flag:
    if x == 5:
        print("True")
        flag = False

    x = int(input())

if flag:
    print("False")
