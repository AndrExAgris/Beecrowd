x  = [float(i) for i in input().split()]
l= sorted(x, reverse=True)
a = l[0]
b = l[1]
c = l[2]
if a>=(b+c):
  print("NAO FORMA TRIANGULO")
elif a<(b+c):
  if a**2 == b**2+c**2:
   print("TRIANGULO RETANGULO")
  if a**2 > b**2+c**2:
   print("TRIANGULO OBTUSANGULO")
  if a**2 < b**2+c**2:
   print("TRIANGULO ACUTANGULO")
  if a == b == c:
   print("TRIANGULO EQUILATERO")
  elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")