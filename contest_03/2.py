n = int(input())
sr = 0
cnt_sr = 0
for _ in range(n):
    a, h, w, t = map(float, input().split())

    if a >= 60 or abs(h - w - 100) > 10:
        cnt_sr += 1
        sr += t

if cnt_sr > 0:
    print(sr / cnt_sr)
else:
    print(0)
