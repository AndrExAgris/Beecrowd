while True:
    m, n = [int(i) for i in input().split()]
    x, y = sorted([m, n])
    if m == n:
        break
    elif m == x:
        print("Crescente")
    elif m == y:
        print("Decrescente")
