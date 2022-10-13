n=0
m=0
while m == 0:
  n = float(input())
  if n<0 or n>10:
    print("nota invalida")
    n = 0
  else:
    m = n
    n = 0
    break
while n == 0:
  n = float(input())
  if n<0 or n>10:
    print("nota invalida")
    n = 0
  else:
    print("media = %.2f" %((m+n)/2))