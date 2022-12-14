
def nn(s,a1,a2):
  a=[a1,a2]
  if (a[0]==s[0] and a[1]==s[1]) or (a[0]==s[0]+1 and a[1]==s[1]+2) or (a[0]==s[0]-1 and a[1]==s[1]+2) or (a[0]==s[0]+1 and a[1]==s[1]-2) or (a[0]==s[0]-1 and a[1]==s[1]-2) or (a[0]==s[0]+2 and a[1]==s[1]+1) or (a[0]==s[0]+2 and a[1]==s[1]-1) or (a[0]==s[0]-2 and a[1]==s[1]+1) or (a[0]==s[0]-2 and a[1]==s[1]-1):
    return False
  else:
    return True
def check(s,a1,a2):
  if (a1>7 or a2>7 or a1<0 or a2<0) or nn(s,a1,a2)==False:
    return 0
  elif a1==7 and a2==7:
    return 1
  return check(s,a1+1,a2+1) + check(s,a1+1,a2) + check(s,a1,a2+1)


h=input()
l="abcdefgh"
s=[l.find(h[0]),int(h[1])-1]
a=[0,0]
print(check(s,a[0],a[1]))
# check(a,00)