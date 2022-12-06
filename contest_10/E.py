n = int(input())
ways = [2**i if i < 3 else 0 for i in range(n+1)]

for i in range(3, n+1):
    ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

print(ways[n])



