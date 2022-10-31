while True:
    m, n = sorted([int(i) for i in input().split()])
    if m != 0 and n != 0 and m > 0 and n > 0:
        x = n - m
        y = m
        print(m, end=" ")
        for i in range(x):
            m = m + 1
            y = y + m
            print(m, end=" ")
        print("Sum=" + str(y))
    else:
        break
