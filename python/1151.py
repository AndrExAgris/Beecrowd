vet = [0]
x = 1
y = 1
for i in range(50):
  vet.append(x)
  z = x+y
  x = y
  y = z
n = int(input())
for j in range(n-1):
  print(vet[j], end=" ")
print(vet[n-1])