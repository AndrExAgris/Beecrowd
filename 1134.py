alcool = 0
gasolina = 0
diesel = 0
while(1):
    x = int(input())
    if x>4 or x<1:
        continue
    if x == 1:
        alcool+=1
    if x == 2:
        gasolina+=1
    if x == 3:
        diesel+=1
    if x == 4:
        break

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)