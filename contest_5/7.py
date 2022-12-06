n = int(input())
arr = [0 for _ in range(101)]
for i in range(n):
    arr[int(input())] += 1

k = max(arr)
for i, x in enumerate(arr):
    if x == k:
        print(i)
        break
