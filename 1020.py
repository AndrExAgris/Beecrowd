D = int(input())
A = int(D/365)
M = int((D-A*365)/30)
d = int(D-A*365-M*30)
print('%.0f ano(s)' % A)
print('%.0f mes(es)' % M)
print('%.0f dia(s)' % d)