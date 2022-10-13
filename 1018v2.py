x = int(input())
print(x)
n100 = x//100
print("%d nota(s) de R$ 100,00" %n100) 
n50 = (x-n100*100)//50
print("%d nota(s) de R$ 50,00" %n50)
n20 = (x-n100*100-n50*50)//20
print("%d nota(s) de R$ 20,00" %n20)
n10 = (x-n100*100-n50*50-n20*20)//10
print("%d nota(s) de R$ 10,00" %n10)
n5 = (x-n100*100-n50*50-n20*20-n10*10)//5
print("%d nota(s) de R$ 5,00" %n5)
n2 = (x-n100*100-n50*50-n20*20-n10*10-n5*5)//2
print("%d nota(s) de R$ 2,00" %n2)
n1 = (x-n100*100-n50*50-n20*20-n10*10-n5*5-n2*2)
print("%d nota(s) de R$ 1,00" %n1)