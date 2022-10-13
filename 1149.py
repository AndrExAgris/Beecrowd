vet = [int(i) for i in input().split()]
a = 0
for i in range((vet[-1]-1)+1):
    a += vet[0] +i

print(a)