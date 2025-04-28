'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
pos = 1
maior = int(input())
for i in range(99):
    n = int(input())
    if n > maior:
        maior = n
        pos = i + 2 
print(maior)
print (pos)
