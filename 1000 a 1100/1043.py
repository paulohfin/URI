'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''
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
