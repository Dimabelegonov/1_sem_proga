n = int(input())
di = {}

for _ in range(n):
    s = input()
    if s in di.keys():
        di[s] += 1
    else:
        di[s] = 1

data = []
for i in di.keys():
    data.append([i, di[i]])

data = sorted(data, key=lambda x: x[1], reverse=True)

for i in data:
    print(*i)
