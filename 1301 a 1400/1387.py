'''
Og é um homem das cavernas com vários filhos e filhas, e ele quer contar todos eles. Og conta seus filhos com sua mão esquerda e suas filhas com sua mão direita.

Entretanto, Og não é inteligente, e não sabe somar os dois números. Assim, ele pediu para você escrever um programa que realize a soma.

Entrada
A entrada contém vários casos de teste. Cada caso de teste consiste em uma linha contendo dois inteiros L e R, separados por um espaço, indicando o número de filhos e de filhas, respectivamente (1 ≤ L, R ≤ 5).

O fim do arquivo de entrada é indicado por L = R = 0.

Saída
Para cada caso de teste, imprima uma linha contendo um inteiro indicando quantos filhos e filhas Og tem ao todo.
'''
a, b = map(int, input().split(' '))

while a != 0 and b != 0:
    print(a+b)
    a, b = map(int, input().split(' '))
