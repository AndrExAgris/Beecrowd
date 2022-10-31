x = [int(i) for i in input().split()]
l = sorted(x)
a = l[0]
b = l[1]
c = (b) / (a)
if c == int(c):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
