n = int(input())

linha = input().split(' ')
soma = 0
for i in linha:
    if i != '':
        soma += int(i)
print(soma - n)