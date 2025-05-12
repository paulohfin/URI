'''
Este ano tem Copa do Mundo! O país inteiro se prepara para torcer para a equipe canarinho conquistar mais um título, tornando-se hexacampeã.

Na Copa do Mundo, depois de uma fase de grupos, dezesseis equipes disputam a Fase final, composta de quinze jogos eliminatórios. A figura abaixo mostra a tabela de jogos da Fase final:



Na tabela de jogos, as dezesseis equipes finalistas são representadas por letras maiúsculas (de A a P), e os jogos são numerados de 1 a 15. Por exemplo, o jogo 3 é entre as equipes identificadas por E e F; o vencedor desse jogo enfrentará o vencedor do jogo 4, e o perdedor será eliminado. A equipe que vencer os quatro jogos da Fase final será a campeã (por exemplo, para a equipe K ser campeã ela deve vencer os jogos 6, 11, 14 e 15.

Dados os resultados dos quinze jogos da Fase final, escreva um programa que determine a equipe campeã.

Entrada
A entrada é composta de quinze linhas, cada uma contendo o resultado de um jogo. A primeira linha contém o resultado do jogo de número 1, a segunda linha o resultado do jogo de número 2, e assim por diante. O resultado de um jogo é representado por dois números inteiros M e N separados por um espaço em branco, indicando respectivamente o número de gols da equipe representada à esquerda e à direita na tabela de jogos (0 ≤ M ≤ 20, 0 ≤ N ≤ 20 e M ≠ N).

Saída
Seu programa deve imprimir uma única linha, contendo a letra identificadora da equipe campeã.
'''
def venc(t1, t2, p):
    if int(p[0]) > int(p[1]):
        return t1
    else:
        return t2

while True:
    try:
        times = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
        qua = []
        se = []
        fi = []
        for i in range(8):
            v = input().split(' ')
            qua.append(venc(times[2 * i], times[2 * i + 1], v))
        for i in range(4):
            v = input().split(' ')
            se.append(venc(qua[2 * i], qua[2 * i + 1], v))
        for i in range(2):
            v = input().split(' ')
            fi.append(venc(se[2 * i], se[2 * i + 1], v))
        v = input().split(' ')
        print(venc(fi[0], fi[1], v))
    except EOFError:
        break 
