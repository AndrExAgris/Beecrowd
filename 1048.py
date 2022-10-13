salary = float(input())

if 0 <= salary <= 400.00:
  print ('Novo salario: %.2f' %(salary*1.15))
  print('Reajuste ganho: %.2f' %((salary*1.15)-salary))
  print('Em percentual: 15 %')

if 400.01 <= salary <= 800.00:
  print ('Novo salario: %.2f' %(salary*1.12))
  print('Reajuste ganho: %.2f' %((salary*1.12)-salary))
  print('Em percentual: 12 %')

if 800.01 <= salary <= 1200.00:
  print ('Novo salario: %.2f' %(salary*1.1))
  print('Reajuste ganho: %.2f' %((salary*1.1)-salary))
  print('Em percentual: 10 %')

if 1200.01 <= salary <= 2000.00:
  print ('Novo salario: %.2f' %(salary*1.07))
  print('Reajuste ganho: %.2f' %((salary*1.07)-salary))
  print('Em percentual: 7 %')

if 2000.00 < salary:
  print ('Novo salario: %.2f' %(salary*1.04))
  print('Reajuste ganho: %.2f' %((salary*1.04)-salary))
  print('Em percentual: 4 %')