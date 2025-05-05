'''
Na última aula de matemática, Rafael, Beto e Carlos aprenderam algumas novas funções matemáticas. Cada um deles se identificou com uma função em especial, e resolveram competir para ver quem tinha a função de maior resultado.

A função que Rafael escolheu é r(x, y) = (3x)² + y².

Já Beto escolheu a função b(x, y) = 2(x²) + (5y)².

Carlos, por sua vez, escolheu a função c(x, y) = -100x + y³.

Dados os valores x e y, diga quem escolheu a função com o maior resultado.

Entrada
A primeira linha de entrada contém um inteiro N que determina a quantidade de casos de teste. Cada caso de teste consiste em dois inteiros x e y (1 ≤ x, y ≤ 100), indicando as variáveis a serem inseridas na função.

Saída
Para cada caso de teste imprima uma linha, contendo uma frase, indicando quem ganhou a competição. Por exemplo, se Rafael ganhar a competição, imprima “Rafael ganhou”. Assuma que nunca haverá empates.
'''
def funcao(x, y):
    if 9 * x * x + y * y > 2 * x * x + 25 * y * y and 9 * x * x + y * y > -100 * x + y * y * y:
        print('Rafael ganhou')
    elif 2 * x * x + 25 * y * y > -100 * x + y * y * y:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')
        
n = int(input())
for i in range(n):
    p = input().split(' ')
    funcao(int(p[0]), int(p[1]))
