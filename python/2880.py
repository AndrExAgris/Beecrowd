palavra = input()
crib = input()

tam_palavra = len(palavra)
tam_crib = len(crib)

possivel = 0

linhas = tam_palavra-tam_crib

for linha in range(linhas+1):
    for letra in range(tam_crib):
        if palavra[linha+letra] == crib[letra]:
            break
    else:
        possivel = possivel + 1
        
print(possivel)