a, b = map(int, input().split())
data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))
di_1 = {}
di_2 = {}
k = 0
for x in data_1:
    if x not in di_1.keys():
        di_1[x] = 1
        k += 1

flag = True
for x in data_2:
    if x not in di_1.keys():
        flag = False
    if x not in di_2.keys():
        di_2[x] = 1

for x in data_1:
    if x not in di_2.keys():
        flag = False

if flag:
    print("Yes")
else:
    print("No")
