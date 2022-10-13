I = round(-0.2,1)
J = round(2.8,1)
for i in range(11):
   I = round(I+0.2,1)
   J = round(J-3+0.2,1)

   for i in range(3):
      J = J+1

      if I%1 == 0:
         I = int(I)
      if J%1 == 0:
         J = int(J)

      print("I="+str(I),"J="+str(J))