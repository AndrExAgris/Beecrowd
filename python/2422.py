casas = []
resp1 = 0
resp2 = 0
for i in range(int(input())):
    x = int(input())
    casas.append(x)
soma = int(input())
k = 0
l = len(casas)-1
while(k<l):
    if casas[k] + casas[l] == soma:
        resp1 = casas[k]
        resp2 = casas[l]
        break
    if casas[k] + casas[l] < soma:
        k+=1
    if casas[k] + casas[l] > soma:
        l-=1

print(resp1,resp2)