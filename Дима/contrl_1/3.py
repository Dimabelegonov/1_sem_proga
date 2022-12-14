n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

s = 0
for i in range(n):
    s += data[i][i]

print(s)
