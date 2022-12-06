def func(arr):
  mx=int(arr[0])
  for i in range(1,len(arr)):
    if int(arr[i])>mx:
      mx=int(arr[i])
  return mx

print(func(input().split()))