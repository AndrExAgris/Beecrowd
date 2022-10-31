for i in range(int(input())):
    x, y = [int(i) for i in input().split()]
    a = abs(x - y) - 1
    c = 0
    if x < y:
        for i in range(a):
            x = x + 1
            if x % 2 == 1:
                c = c + x
        print(c)
    elif x > y:
        for i in range(a):
            y = y + 1
            if y % 2 == 1:
                c = c + y
        print(c)
    else:
        print(c)
