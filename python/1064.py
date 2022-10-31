n = 0
media = 0
for i in range(6):
    a = float(input())
    if a > 0:
        n = n + 1
        media = media + a
print(n, "valores positivos")
if n != 0:
    media = media / n
    print("%.1f" % media)
else:
    print("-nan")
