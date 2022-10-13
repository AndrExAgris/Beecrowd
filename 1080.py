v = 1
h = 0
a = int(input())
for i in range(99):
  b = int(input())
  if a>=b:
    v = v+1
  if b>a:
    v = v+1
    h = v
    a=b
print(a)
print(h)