n, c, m = [int(i)for i in input().split()]
count = c
a = 0
b = 0
vc = [int(i) for i in input().split()]
vm = [int(i) for i in input().split()]
vis = [False]*(n+5)
for i in vc:
  if(vis[i] == True):
    count -= 1
    continue
  for j in vm:
    if j == i:
      count -= 1
      vis[j] = True
      break

print(count)