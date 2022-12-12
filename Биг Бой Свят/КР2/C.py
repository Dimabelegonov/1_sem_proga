
def check(a):
  s={}
  for i in range(len(a)):
    if a[i]!=" " and a[i] in s.keys():
      s[a[i]]+=1
    elif a[i]!=" " and a[i] not in s.keys():
      s[a[i]]=1

  b=[]
  for i in s.keys():
    b.append([i,s[i]])
  b=sorted(b)

  for i in range(len(b)):
    print(" ".join(map(str,b[i])))

a=input()
check(a)