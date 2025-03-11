n = int(input())
for i in range(n):
    linha = input().split(' ')
    print('Case ' + str(i + 1) + ': ' + str(linha[int(len(linha)/2)]))