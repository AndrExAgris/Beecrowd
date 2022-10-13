def split(h):
    return [char for char in h]

x=int(input())
vet =[2,5,5,4,5,6,3,7,6,6]
for i in range(x):
    soma=0
    a=input()
    b=split(a)
    for j in b:
        if int(j) == 0:
            j=9
        soma+=vet[int(j)-1]
    print(soma,"leds")