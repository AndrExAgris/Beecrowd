n = int(input())
v = [int(i) for i in input().split()]
v.sort()
p = 1
if v[0] <= 8:
  for i in range(n-1):
    if v[i] >= (v[i+1]-8):
      p += 1
    else:
      break
if p==n:
  print("S")
else:
  print("N") 
