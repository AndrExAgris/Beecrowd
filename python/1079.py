x = int(input())
for i in range(x):
    a, b, c = [float(i) for i in input().split()]
    y = (a * 2 + b * 3 + c * 5) / 10
    print("%.1f" % y)
