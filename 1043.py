a, b,c = map(float, input().split(' '))

lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort()

if lista[2] >= lista[1] + lista[0]:
    print('Area = %.1f' %((a + b) * c / 2))
else:
    print('Perimetro = %.1f' %(a + b + c))