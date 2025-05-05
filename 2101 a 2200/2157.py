'''
Imprimir números em sequência é uma tarefa relativamente simples. Mas, e quando se trata de uma sequência espelho? Trata-se de uma sequência que possui um número de início e um número de fim, e todos os números entre estes, inclusive estes, são dispostos em uma sequência crescente, sem espaços e, em seguida, esta sequência é projetada de forma invertida, como um reflexo no espelho. Por exemplo, se a sequência for de 7 a 12, o resultado ficaria 789101112211101987

Escreva um programa que, dados dois números inteiros, imprima a respectiva sequência espelho.

Entrada
A entrada possui um valor inteiro C indicando a quantidade de casos de teste. Em seguida, cada caso apresenta dois valores inteiros, B e E (1 ≤ B ≤ E ≤ 12221), indicando o início e o fim da sequência.

Saída
Para cada caso de teste, imprima a sequência espelho correspondente.
'''
n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    palavra = ''
    palavra2 = ''
    for i in range(a, b + 1):
        palavra += str(i)
    
    print(palavra, end='')
    for i in range(len(palavra)):
        print(palavra[len(palavra) - i - 1], end='')
    print()
