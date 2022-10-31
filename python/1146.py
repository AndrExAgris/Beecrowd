n = int(input())
while n != 0:
    x = 1
    for i in range(n - 1):
        print(x, end=" ")
        x += 1
    print(x)
    n = int(input())
