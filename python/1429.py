import math

x = int(input())
while x != 0:
    num = list(str(x))
    tam = tab = len(num)
    count = 0
    for i in range(tam):
        count += math.factorial(tab) * int(num[i])
        tab -= 1
    print(count)
    x = int(input())
