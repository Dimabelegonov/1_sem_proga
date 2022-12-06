n = int(input())
month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
         "September": 9, "October": 10, "November": 11, "December": 12}


data = []
for _ in range(n):
    t = list(map(str, input().split()))
    cnt = int(t[0]) * 24 + month[t[1]] * 800 + int(t[2]) * 10000 + float(".".join(list(map(str, t[3].split(":")))))

    data.append([t, cnt])

data.sort(key=lambda x: x[1])
for i in data:
    print(" ".join(i[0]))
