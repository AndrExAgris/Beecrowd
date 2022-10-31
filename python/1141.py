n = int(input())
x = 1
count = 1
while n >= count:
    if x % 4 != 0:
        print(str(x) + " ", end="")
    else:
        print("PUM")
        count += 1
    x += 1
