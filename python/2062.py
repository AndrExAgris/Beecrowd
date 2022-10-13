n = int(input())
v = [str(i) for i in input().split()]
for i in range(n):
    a = len(v[i])
    if a == 3:
        if v[i][0] == "O" and v[i][1] == "B":
            v[i] = "OBI"
        if v[i][0] == "U" and v[i][1] == "R":
            v[i] = "URI"
print(' '.join(v))