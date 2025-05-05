'''
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.
'''
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
