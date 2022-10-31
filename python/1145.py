x, y = [int(i) for i in input().split()]
n = 1
while n <= y:
    for j in range(x - 1):
        print(n, end=" ")
        n += 1
    print(n)
    n += 1
