p = 0
n = 0
par = 0
impar = 0
for i in range(5):
  a=float(input())

  if a > 0:
    p = p+1
  elif a < 0:
    n = n+1

  if a%2 == 0:
    par = par+1
  else:
    impar = impar+1

print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(p,"valor(es) positivo(s)")
print(n,"valor(es) negativo(s)")