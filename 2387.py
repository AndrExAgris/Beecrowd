vet = []
a=b=count=0
t = int(input())
for i in range(t):
    x=[int(i) for i in input().split()]
    vet.append(x)
vet.sort(key=lambda vet: vet[1])
for j in range(t):
    if vet[j][0] >= b:
        count+=1
        b = vet[j][1]
print(count)