n = int(input())
s = input()
data = [[] for i in range(n)]
while s != "#":
    a, b = map(int, s.split())
    data[a].append(b)
    data[a].sort(reverse=True)
    s = input()


data.sort(key=lambda x: sum(x), reverse=True)

for i in data:
    print(*i, end=" ")
