a = int(input())

data = []
i = 2
while a != 1:

    if a % i == 0:
        a //= i
        data.append(i)
    else:
        i += 1

for t in data:
    print(t)
