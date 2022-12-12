def merge_by_molweight(L,R):
  a="CHNO"
  n=[12,1,14,16]
  L1=[]
  for i in range(len(L)):
    k=[]
    for j in range(len(L[i])):
      if L[i][j] in a:
        k.append(n[a.find(L[i][j])])
      else:
        k[-1]=k[-1]*int(L[i][j])
    L1.append(sum(k))
  R1=[]
  for i in range(len(R)):
    k=[]
    for j in range(len(R[i])):
      if R[i][j] in a:
        k.append(n[a.find(R[i][j])])
      else:
        k[-1]=k[-1]*int(R[i][j])
    R1.append(sum(k))
  s=[]
  i,j=0,0
  while i<len(L1) and j<len(R1):
    if L1[i]<=R1[j]:
      s.append(L[i])
      i=i+1
    else:
      s.append(R[j])
      j=j+1
  if i==len(L1):
    for h in range(j,len(R1)):
      s.append(R[h])
  elif j==len(R1):
    for h in range(i,len(L1)):
      s.append(L[h])
  return s

merge_by_molweight(['N2', 'CO2', 'C6H6'], ['C6H5CH3', 'C60'])

