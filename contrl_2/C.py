s = list(input())
di = {}

for i in s:
    if i != " ":
        if i in di.keys():
            di[i] += 1
        else:
            di[i] = 1


ans = []
for i in di.keys():
    ans.append([i, di[i]])

ans = sorted(ans)
for i in ans:
    print(*i)
