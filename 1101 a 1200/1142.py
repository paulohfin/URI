'''
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
'''
n = int(input())

k = 0
for i in range(n):
    print(k+1, k+2, k+3, 'PUM')
    k+=4
