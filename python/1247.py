while(1):
    try:
        dist,vf,vg  = [int(i) for i in input().split()]

        x = ((dist**2)+(12**2))**(1/2)

        a = x/vg
        b = 12/vf

        if(a<=b):
            print("S")
        else:
            print("N")
 

    except(EOFError):
        break
    