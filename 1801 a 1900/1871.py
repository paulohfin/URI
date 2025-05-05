'''
Um dia o Prof. Humberto José Roberto fez o seguinte questionamento: Se o zero a esquerda de um número não tem valor algum, por que teria em outras posições de um número? Analisando da seguinte forma, ele pede sua ajuda para, ao somar dois valores inteiros, que o resultado seja exibido segundo o raciocínio dele, ou seja, sem os Zeros. Por exemplo, ao somar 15 + 5, o resultado seria 20, mas com esta nova ideia, o novo resultado seria 2, e, ao somar 99 + 6, o resultado seria 105, mas com esta nova ideia, o novo resultado seria 15.

Escreva um programa que, dado dois números inteiros, sem o algarismo zero, some os mesmos e, caso o resultado tenha algum algarismo zero, que os retire antes de exibir.

Entrada
Haverá diversos casos de teste. Cada caso de teste inicia com dois inteiros M e N (1 ≤ M ≤ N ≤ 999.999.999).

O último caso de teste é indicado quando N = M = 0, sendo que este caso não deve ser processado.

Saída
Para cada caso de teste, imprima o resultado da soma dos dois valores, sem os Zeros.
'''
while True:
    try:
        num1, num2 = map(int, input().split(' '))
        if num1 == 0 and num2 == 0:
            break
        num = num1 + num2
        soma = str(num)
        soma2 = []
        for i in soma:
            if i != '0':
                soma2.append(i)
        for i in soma2:
            print(i, end='')
        print()
    except EOFError:
        break
