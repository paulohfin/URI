'''
Em cada fase do jogo do Pula Sapo você deve conduzir seu anfíbio através de uma sequência de canos de alturas diferentes até chegar a salvo no cano mais à direita. Entretanto, o sapo só consegue sobreviver se a diferença de altura entre canos consecutivos for de, no máximo, a altura do pulo do sapo. Caso a altura do cano seguinte seja muito alta, o sapo bate no cano e cai. Se a altura do cano seguinte for muito baixa, o sapo não aguenta a queda. O sapo sempre começa em cima do cano mais à esquerda.

Neste jogo, a distância entre os canos é irrelevante, ou seja, o sapo sempre consegue alcançar o próximo cano com um pulo.



Você deve escrever um programa que, dadas as alturas dos canos e a altura do pulo do sapo, mostra se a fase do jogo pode ser vencida ou não.

Entrada
A entrada é dada em duas linhas. A primeira tem dois inteiros positivos P e N, a altura do pulo do sapo e o número de canos (1 ≤ P ≤ 5 e 2 ≤ N ≤ 100). A segunda linha tem N inteiros positivos que indicam as alturas dos canos ordenados da esquerda para a direita. Não há altura maior do que 10.

Saída
A saída é dada em uma única linha. Se o sapo pode chegar no cano mais à direita, escreva "YOU WIN". Se o sapo não consegue, escreva "GAME OVER".
'''
def mod(n):
    if n > 0:
        return n 
    else:
        return -n

p, n = map(int, input().split(' '))
pulo = input().split(' ')
i = 0
cnt = 0
while i < len(pulo):
    while i < len(pulo) and pulo[i] == '':
        i += 1
    if i < len(pulo): d1 = pulo[i]
    i+=1
    while i < len(pulo) and pulo[i] == '':
        i += 1
        
    if i < len(pulo):
        d2 = pulo[i]
        if mod(int(d2) - int(d1)) <= p:
            cnt += 1
if cnt == n - 1:
    print('YOU WIN')
else:
    print('GAME OVER')
