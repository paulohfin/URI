n = int(input())

while n > 0:
    soma = 0
    for i in range(n):
        k = input()
        if k.find('suco de laranja') != -1:
            k.split(' ')
            soma += int(k[0]) * 120
        elif k.find('morango fresco') != -1:
            k.split(' ')
            soma += int(k[0]) * 85
        elif k.find('mamao') != -1:
            k.split(' ')
            soma += int(k[0]) * 85
        elif k.find('goiaba vermelha') != -1:
            k.split(' ')
            soma += int(k[0]) * 70
        elif k.find('manga') != -1:
            k.split(' ')
            soma += int(k[0]) * 56
        elif k.find('laranja') != -1 and k.find('laranja') == -1:
            k.split(' ')
            soma += int(k[0]) * 50
        elif k.find('brocolis') != -1:
            k.split(' ')
            soma += int(k[0]) * 34
    if soma > 130:
        print('Menos',soma - 130, 'mg')
    elif soma < 110:
        print('Mais',110 - soma, 'mg')
    else:
        print(soma,'mg')
    n = int(input())