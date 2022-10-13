n = int(input())
x=1
n = n-1
for i in range(n):
  x=x+1
  if x%2 == 0:
    y = x**2
    print(str(x)+'^2 =',y)