c = input()

soma = 0.0
for i in range(12):
    for j in range(12):
        valor = float(input())
        if i < j and i + j > 11:
            soma += valor
if c == 'S':
    print('%.1f' %(soma))
else:
    print('%.1f' %(soma/30))