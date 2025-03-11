a = input()
b = a.split(' ')

n = 0
cont = 0
c = 0

for i in b:
    if cont == 0:
        n = int(i)
        cont += 1
    elif int(i) > 0:
        c = int(i)
        break
soma = 0
for i in range(c):
    soma += n + i

print(soma)