def check(a):
  s="02468"
  k=0
  for i in range(len(a)):
    if a[i] in s:
      k=k+1
  print(k)

a=input()
check(a)