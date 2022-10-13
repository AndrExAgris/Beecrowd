B = int(input())
E = int(input())
N = pow(B%9,E,9)
if N <= 0:
   print("9")
else:
    print (N)