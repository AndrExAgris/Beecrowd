n_rodadas = int(input())
vitorias = 0

for rodada in range(0,n_rodadas):
    carro = int(input())
    if carro != 1:
        vitorias = vitorias + 1

print(vitorias)

