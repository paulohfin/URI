'''
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.
'''
a = int(input())
b = int(input())

soma = 0
if a < b:
    for i in range(a, b+1):
        if i % 13 != 0:
            soma += i

else:
    for i in range(b, a+1):
        if i % 13 != 0:
            soma += i
print(soma)
