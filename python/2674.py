n =100002
s = [True for i in range(n)]
s[0] = False
s[1] = False
for i in range(2,n):
  if(s[i]):
    for j in range(i*i,n,i):
      s[j] = False

while(True):
  try:
    n = input()
    sup=True

    for i in n:
      sup &= s[int(i)]
    if sup and s[int(n)]:
      print("Super")
    elif s[int(n)]:
      print("Primo")
    else:
      print("Nada")
  except:
    break