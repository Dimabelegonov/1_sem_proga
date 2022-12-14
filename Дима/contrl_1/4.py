data = []

s = input()
while s != "#":
    data.append(int(s))
    s = input()


a = round(sum(data) / len(data), 3)
b = max(data)
c = min(data)
d = 0

for i in range(0, len(data), 3):
    d += (data[i] + data[i + 1] + data[i + 2]) % data[i + 2]

print(a, b, c, d)
