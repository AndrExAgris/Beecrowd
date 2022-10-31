I = -1
J = 3
for i in range(5):
    I = I + 2
    J = J + 5

    for i in range(3):
        J = J - 1
        print("I=%.0f" % I, "J=%.0f" % J)
