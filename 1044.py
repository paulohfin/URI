a, b = map(int, input().split(' '))

if a > b:
    temp = a
    a = b
    b = temp
if b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')