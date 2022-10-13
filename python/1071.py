x = int(input())
y = int(input())
a = x-y-1
a = abs(a)
c = 0
if x<y:
  for i in range(a):
    x = x + 1
    if x%2 == 1:
      c = c+x
  print(c)
elif y<x:
  for i in range(a):
    y = y + 1
    if y%2 == 1:
      c = c+y
  print(c)
else:
  print(c)
