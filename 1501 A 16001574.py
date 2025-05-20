'''
Você possui um robô na origem do eixo x. O robô receberá algumas instruções. Sua tarefa é predizer sua posição depois de executar todas as instruções.

LEFT: move uma unidade para a esquerda (diminui p em 1, onde p é a posição do robô antes de mover)
RIGHT: move uma unidade para a direita (incrementa p em 1)
SAME AS i: executa a mesma ação que na i-ésima instrução. É garantido que i é um inteiro positivo não maior que o número de instruções já executadas.
Entrada
A primeira linha contém o número de casos de testes T (T <= 100). Cada caso de teste inicia com um inteiro n ( 1 <= n <= 100), o número de instruções. Cada uma das n linhas seguintes contém uma instrução.

Saída
Para cada caso de teste, imprima a posição final do robô. Note que após processar cada caso de teste, o robô deve ter sua posição inicial resetada para a origem.
'''
def ler(linha,i):
    if linha[i][0] == 'LEFT':
        return -1
    elif linha[i][0] == 'RIGHT':
        return 1
    else:
        return ler(linha,int(linha[i][2])-1)

n = int(input())

for i in range(n):
    m = int(input())
    pos = 0
    linha = []
    for j in range(m):
        linha.append(input().split(' '))
    for j in range(m):
        pos += ler(linha,j)
    print(pos)