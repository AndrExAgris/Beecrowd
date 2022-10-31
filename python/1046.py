a, b = input().split()
a = int(a)
b = int(b)
h = 0
if a < b:
    h = b - a
if a > b:
    h = 24 - a + b
if a == b:
    h = 24
print("O JOGO DUROU %i HORA(S)" % h)
