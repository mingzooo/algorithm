arr =[]
for _ in range(9):
  n = int(input())
  arr.append(n)
a = 0
b = 0
for i in range(9):
  for j in range(i+1, 9):
    if(sum(arr)-arr[i]-arr[j]==100):
      a = arr[i]
      b = arr[j]
      break

arr.remove(a)
arr.remove(b)
for x in arr:
  print(x)