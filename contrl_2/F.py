zagon, loshad = map(int, input().split())
kor1 = input().split()
kor2 = []

for i in range(0, zagon):
    kor2.append(int(kor1[i]))
lenn = int(0)
rasst = int(kor2[zagon - 1] - kor2[0])

while lenn < rasst:
    a = (lenn + rasst) // 2
    count = 1
    j = 0

    for i in range(0, zagon, 1):
        if abs(kor2[i] - kor2[j] >= a):
            count += 1
            j = i
    if count >= loshad:
        lenn = a + 1
    else:
        rasst = a
print(rasst - 1)
