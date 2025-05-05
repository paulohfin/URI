'''
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

Entrada
A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo nome de cada um dos jogadores. Abaixo do nome de cada jogador, seguem duas linhas com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) representam a quantidade de tentativas de saques, bloqueios e ataques e na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

Saída
A saída deve conter o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.
'''
n = int(input())
S = 0
B = 0
A = 0
S1 = 0
B1 = 0
A1 = 0
for i in range(n):
    nome = input()
    s, b, a = map(int, input().split(' '))
    
    S += s 
    B += b 
    A += a 
    s1, b1, a1 = map(int, input().split(' '))
    
    S1 += s1 
    B1 += b1 
    A1 += a1  

print('Pontos de Saque: %.2f'%(100*S1/S),end='')
print('%')
print('Pontos de Bloqueio: %.2f'%(100*B1/B),end='')
print('%')
print('Pontos de Ataque: %.2f'%(100*A1/A),end='')
print('%')
