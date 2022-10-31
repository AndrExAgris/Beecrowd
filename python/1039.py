while 1:
    try:
        r1, x1, y1, r2, x2, y2 = [int(i) for i in input().split()]
        resp = 0
        a = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
        if (a + r2) <= r1:
            print("RICO")
        else:
            print("MORTO")
    except (EOFError):
        break
