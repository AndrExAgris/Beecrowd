while(1):
    try:
        s,v1,v2 = [int(i) for i in input().split()]
        if(v2>=v1):
            print("impossivel")
        else:
            va = v1 - v2
            temp = float(s/va)
            print("%.2f" %temp)
    except(EOFError):
        break