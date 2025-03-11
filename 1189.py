operacao = input()

soma = 0
for i in range(12):
    for j in range(12):
        k = float(input())
        if i > j and i + j < 11:
            soma += k
if operacao == 'S':
    print('%.1f' %soma)
else:
    print('%.1f' %(soma / 30))