n = int(input())

for i in range(n):
    linha = input().split(' ')
    a, b = map(int, input().split(' '))
    if (a+b) % 2 == 0:
        if linha[1] == 'PAR':
            print(linha[0])
        else:
            print(linha[2])
    else:
        if linha[1] == 'PAR':
            print(linha[2])
        else:
            print(linha[0])