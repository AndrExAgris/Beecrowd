a = int(input())
b = int(input())
c = int(input())

x = (2*b)+(4*c)
y = (a*4)+(2*b)
z = (a*2)+(c*2)

resp=x

if(y<resp):
    resp = y

if(z<resp):
    resp = z

print(resp)
    