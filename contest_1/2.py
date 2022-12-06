a = int(input())
s = input().strip()
b = int(input())
if s == "<":
    print("YES" if a < b else "NO")
else:
    print("YES" if b < a else "NO")
