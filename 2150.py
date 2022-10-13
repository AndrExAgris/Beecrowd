while(1):
    try:
        x = list(input())
        p = list(input())
        count = 0
        for i in p:
            for j in x:
                if i == j:
                    count+=1
        print(count)


    except(EOFError):
        break