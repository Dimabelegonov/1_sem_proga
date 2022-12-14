s = list(input())
k = 0
for i in s:
    if i.isdigit() and int(i) % 2 == 0:
        k += 1

print(k)

