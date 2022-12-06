"Алгоритм нахождения всех простых чисел до некоторого числа n"

def func(N):
  A=[1]*(N+1)
  B=[]
  A[0],A[1]=0,0
  for i in range(N+1):
    if A[i]==1:
      B.append(i)
      j=2*i
      while j<(N+1):
        A[j]=0
        j=j+i
  return B
print(" ".join(map(str,func(int(input())))))

"Временная сложность алгоритма - O(nlog(log_n))"