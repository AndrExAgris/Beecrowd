for i in range(int(input())):
  x, y = [int(i) for i in input().split()]
  if y == 0:
    print("divisao impossivel")
  else:
    print('%.1f' %(x/y))