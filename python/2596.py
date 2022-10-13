for i in range(int(input())):
    n =int(input())

    def Sieve(n):
        s = [0 for i in range(n)]
        for i in range(1,n+1):
            for j in range(i,n,i):
                s[j] += 1

        count = 0

        for(i) in range(1,n):
            if s[i]%2 ==0:
                count+=1
        
        print(count)
    Sieve(n+1)