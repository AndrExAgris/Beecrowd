while(True):   
    try:
        x, y = [str(i) for i in input().split()] 
        vet = []

        for i in range(int(x)):
            vet.append(int(y[i]))

        a = sum(vet)

        if a%3 == 0:
            print(str(a)+" sim")
        else:
            print(str(a)+" nao")

    except EOFError:
        break