from sys import stdin, stdout 
a = ['1\n', '7\n', '9\n', '3\n']
for i in range(int(stdin.readline())):
    stdout.write(a[int(stdin.readline())%4])