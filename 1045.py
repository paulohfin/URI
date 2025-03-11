a, b, c = map(float, input().split(' '))

lado = []
lado.append(a)
lado.append(b)
lado.append(c)
lado.sort()
if lado[2] >= lado[1] + lado[0]:
    print('NAO FORMA TRIANGULO')
else:
    if lado[2] * lado[2] == lado[1] * lado[1] + lado[0] * lado[0]:
        print('TRIANGULO RETANGULO')
    if lado[2] * lado[2] > lado[1] * lado[1] + lado[0] * lado[0]:
        print('TRIANGULO OBTUSANGULO')
    if lado[2] * lado[2] < lado[1] * lado[1] + lado[0] * lado[0]:
        print('TRIANGULO ACUTANGULO')
    if a == b and a == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c: 
        print('TRIANGULO ISOSCELES')