p1 = input()
p2 = input()

a1, a2, a3, a4, a5 = map(int, p1.split(' '))
b1, b2, b3, b4, b5 = map(int, p2.split(' '))

if a1 + b1 == 1 and a3 + b3 == 1 and a4 + b4 == 1 and a5 + b5 == 1 and a2 + b2 == 1:
    print('Y')
else:
    print('N')