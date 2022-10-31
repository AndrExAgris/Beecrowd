x = int(input())
if x % 2 == 0:
    a = 11
else:
    a = 10
    print(x)

for i in range(a):
    x = x + 1
    if x % 2 == 1:
        print(x)
