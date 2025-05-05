'''
Tausfão apresenta um programa de televisão o qual dá prêmios aos participantes que respondem corretamente a cálculos matemáticos. Quando os participantes erram, ele ressalta o quão longe a resposta está da esperada. Levando em consideração somente as respostas erradas, ajude o Tausfão informando como deve ser a pronúncia do erro do participante.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro C, representando a quantidade de casos de teste. As próximas C linhas serão formadas por um número inteiro, seguido por um espaço, um caractere de operação (adição, subtração ou multiplicação), outro número inteiro, mais um espaço, um sinal de igualdade, outro espaço e, por fim, um número inteiro, representando o resultado dito pelo participante em relação ao referido cálculo do caso de teste.

Saída
Para cada caso de teste de entrada do seu programa, imprima a expressão “Errou!”, baseada na distância da resposta do participante em relação à resposta correta.
'''
n = int(input())
for i in range(n):
    l = input().split(' ')
    if l[1] == '+':
        erro = int(l[4]) - (int(l[0]) + int(l[2]))
        if erro < 0:
            erro = -erro
        print('E',end='')
        for i in range(erro):
            print('r',end='')
        print('ou!')
    elif l[1] == '-':
        erro = int(l[4]) - (int(l[0]) - int(l[2]))
        if erro < 0:
            erro = -erro
        print('E',end='')
        for i in range(erro):
            print('r',end='')
        print('ou!')
    else:
        erro = int(l[4]) - (int(l[0]) * int(l[2]))
        if erro < 0:
            erro = -erro
        print('E',end='')
        for i in range(erro):
            print('r',end='')
        print('ou!')
