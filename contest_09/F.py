n = int(input())
data = list(map(int, str(n)))
data.sort()

if data[0] == 0:
    for i in range(len(data)):
        if data[i] != 0:
            data[0], data[i] = data[i], data[0]
            break

for i in range(len(data)):
    data[i] = str(data[i])

print("".join(data))
