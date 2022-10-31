d = float(input())

if d > 0 and d <= 2000:
    print("Isento")
elif d > 2000 and d <= 3000:
    r = d - 2000
    s = r * 0.08
    print("R$ %.2f" % s)
elif d > 3000 and d < 4500:
    r = d - 3000
    s = (r * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % s)
else:
    r = d - 4500
    s = (r * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % s)
