while 1:
    n = 0
    m = 0
    while m == 0:
        n = float(input())
        if n < 0 or n > 10:
            print("nota invalida")
            n = 0
        else:
            m = n
            n = 0
            break
    while n == 0:
        n = float(input())
        if n < 0 or n > 10:
            print("nota invalida")
            n = 0
        else:
            print("media = %.2f" % ((m + n) / 2))
    a = 0
    while 1:
        a = float(input("novo calculo (1-sim 2-nao)\n"))
        if a < 1 or 1 > a < 2 or a > 2:
            continue
        break
    if a == 1:
        continue
    elif a == 2:
        break
