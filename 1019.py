S = int(input())
A = int(S/3600)
B = int((S-A*3600)/60)
C = int(S-A*3600-B*60)
print(str(A)+':'+str(B)+':'+str(C))