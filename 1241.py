n = int(input())

for m in range(n):
    linha = input().split(' ')
    l1 = len(linha[0])
    l2 = len(linha[1])
    if linha[0][l1 - l2:] == linha[1]:
        print('encaixa')
    else:
        print('nao encaixa')