'''
Escreva um programa que dado um inteiro N, imprima os números primos gêmeos mais próximos menores ou iguais a N.

De acordo com a wikipedia, "Um primo gêmeo é um número primo que é 2 a menos ou 2 a mais que outro número primo - por exemplo, qualquer membro do par primo gêmeo (41, 43). Em outras palavras, um primo gêmeo é primo que tem um intervalo de dois ".

Entrada
A entrada deve conter um inteiro N, em que (5 ≤ N ≤ 1000).

Saída
A saída deve conter dois inteiros X e Y separados por espaço, representando os dois números primos gêmeos mais próximos menores ou iguais a N.
'''
def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primoGemeo(n):
    if primo(n) and primo(n - 2):
        return True
    else:
        return False

while True:
    try:
        n = int(input())
        for i in range(n):
            k = primoGemeo(n - i)
            if k == True:
                print(n - i - 2, n - i)
                break
    except EOFError:
        break
