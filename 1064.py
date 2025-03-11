soma = 0.0
pos = 0
for i in range(6):
    n = float(input())
    if n > 0:
        soma += n
        pos += 1
print(pos,'valores positivos')
print('%.1f' %(soma/pos))