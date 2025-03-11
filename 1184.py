operacao = input()

soma = 0
for i in range(12):
    for j in range(12):
        k = float(input())
        if j < i:
            soma += k
if operacao == 'S':
    print(soma)
else:
    print('%.1f' %(soma / 66))