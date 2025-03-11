leitura1 = input()
leitura2 = input()
leitura3 = input()
leitura4 = input()

a = leitura1.split(' ')
dia1 = int(a[1])
a = leitura2.split(' ')
h1 = int(a[0])
m1 = int(a[2])
s1 = int(a[4])
a = leitura3.split(' ')
dia2 = int(a[1])
a = leitura4.split(' ')
h2 = int(a[0])
m2 = int(a[2])
s2 = int(a[4])

s = s2 - s1
if s < 0:
    m2 -= 1 
    s += 60
m = m2 - m1
if m < 0:
    h2 -= 1 
    m += 60
h = h2 - h1
if h < 0:
    dia2 -= 1 
    h += 24
dia = dia2 - dia1
print(dia,'dia(s)')
print(h,'hora(s)')
print(m,'minuto(s)')
print(s,'segundo(s)')