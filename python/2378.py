n, c = [int(i) for i in input().split()]
count = 0
resp = "N"
for i in range(n):
    s, e = [int(i) for i in input().split()]
    count = count - s + e
    if count > c:
        resp = "S"
print(resp)
