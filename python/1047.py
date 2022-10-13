hi, mi, hf, mf = [int(i) for i in input().split()]
h = 0
m = 0
HI =hi*60 + mi
HF = hf*60 + mf

if HI < HF:
  h = int((HF-HI)/60)
  m = int((HF-HI) - h*60)

if HI > HF:
  h = int((1440-HI+HF)/60)
  m = int((1440-HI+HF) - h*60)

if HI == HF:
  h = int(24)
  m == int(0)
print('O JOGO DUROU',h,'HORA(S) E',m,'MINUTO(S)')