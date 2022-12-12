def check(a):
  s=""
  k=0
  for i in range(len(a)):
    if a[i]=="\"" and k==0:
      k=1
      j=i+1
      while a[j]!="\"":
        s=s+a[j]
        j+=1
  print(s)

a=input()
check(a)