import math

x, y = [int(i) for i in input().split()]
a = x * y
a = a / 10
for i in range(1, 9):
    print(math.ceil(a * i), end=" ")

print(math.ceil(a * 9))
