casos = int(input())
c = 0
r = 0
s = 0

for i in range(casos):
   a, b = [str(j) for j in input().split()]
   if b == 'C':
      c = c+int(a)
   if b == 'R':
      r = r+int(a)
   if b == 'S':
      s = s+int(a)

t = c+r+s

o = float(100*c)/t
p = float(100*r)/t
q = float(100*s)/t

print("Total: %.0f cobaias" %t)
print("Total de coelhos: %.0f" %c)
print("Total de ratos: %.0f" %r)
print("Total de sapos: %.0f" %s)
print("Percentual de coelhos: %.2f" %o,"%")
print("Percentual de ratos: %.2f" %p,"%")
print("Percentual de sapos: %.2f" %q,"%")