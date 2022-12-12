def check(a,b,c):
  s=[[(i+j)*a[0] if i*j==0 else 0 for i in range(len(b)+1)] for j in range(len(c)+1)]
  for i in range(1, len(b) + 1):
      for j in range(1, len(a) + 1):
          if a[j - 1] == b[i - 1]:
              s[i][j] = s[i - 1][j - 1]
          else:
              s[i][j] = min(s[i - 1][j], s[i - 1][j - 1], s[i][j - 1]) + 1
  return s[-1][-1]


a=input().split()
b=input().split()
c=input().split()
check(a,b,c)