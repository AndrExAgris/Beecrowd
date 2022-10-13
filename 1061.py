z, d1 = input().split()
hi, mi, si = input().split(':')
w, d2 = input().split()
hf, mf, sf = input().split(':')
D1 = int(hi)*3600+int(mi)*60+int(si)
D2 = int(hf)*3600+int(mf)*60+int(sf)
temp = D2-D1
dias = int(d2) - int(d1)
tt = dias*86400+temp
s = (tt)%60
tt = (tt-s)/60
m = int(tt)%60
tt = (tt-m)/60
h = int(tt)%24
tt = (tt-h)/24
d = int(tt)
print(d,'dia(s)')
print(h,'hora(s)')
print(m,'minuto(s)')
print(s,'segundo(s)')