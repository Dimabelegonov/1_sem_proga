a = list(map(int, input().split()))
su = 0
cnt = 0
mu = 1
for x in a:
    su += x
    cnt += 1
    mu *= x
print(su, cnt, mu)
