n = int(input())
flag = True
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
