'''
Você chegou a um dos últimos chefões no novo jogo de ação 2-D de deslocamento lateral, KiloMan. O chefão tem uma arma grande que pode atirar projéteis em várias alturas. Para cada tiro, KiloMan pode ficar parado ou pular. Se ele ficar parado e o tiro estiver na altura 1 ou 2, ele será atingido. Se ele pular e o tiro estiver a uma altura maior que 2, então ele também será atingido. Caso contrário, ele não é atingido. Dada a altura de cada tiro e a sequência de pulos, quantas vezes KiloMan será atingido?

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N que indica o número de casos de teste. Cada caso de teste é composto por 3 linhas. A primeira linha contém um inteiro T (1 ≤ T ≤ 50) que indica o número de tiros. A segunda linha contém T inteiros, que representam a sequência das alturas às quais os tiros estão sendo disparados. Cada elemento da sequência será entre 1 e 7, inclusive. A terceira linha da entrada contém a string "pulos", que representa a sequência de pulos que KiloMan tentará; 'J' significa que ele irá pular e 'S' significa que ele ficará parado. Por exemplo, se o primeiro número da sequência de tiros for 3 e o primeiro caractere de "pulos" for 'J', então KiloMan pulará assim que o chefão atirar a uma altura 3 (e, portanto, ele será atingido).

Saída
Para cada caso, seu programa deve imprimir um inteiro representando o número de vezes que KiloMan é atingido.
'''
n = int(input())

for i in range(n):
    m = int(input())
    tiro = input().split(' ')
    pulo = input()
    acerto = 0
    for j in range(len(tiro)):
        if (int(tiro[j]) > 2 and pulo[j] == 'J') or (int(tiro[j]) < 3 and pulo[j] == 'S'):
            acerto += 1 
    print(acerto)