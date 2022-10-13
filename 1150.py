x = int(input())
y = int(input())
while(y<=x):
  y = int(input())
count = 1
v = x+1
while(x<=y):
  x += v
  v += 1
  count+=1

print(count)
