'''
O mostro do lago Ness é um animal não-identificado misterioso que, dizem, habita o Lago Ness, um grande lago localizado na cidade de Inverness, no norte da Escócia. Nessie é geralmente categorizado como um tipo de mostro de lagos.
Tradução livre de trecho de https://en.wikipedia.org/wiki/Loch_Ness_Monster.

Em julho de 2003, a rede BBC fez uma grande investigação sobre o Lago Ness, usando 600 sonares separados. Nenhum vestígio de nenhum "mostro marítimo" (isto é, um grande animal, conhecido ou desconhecido) foi encontrado no lago. A equipe da BCC concluiu que Nessie não existe. Agora, nós queremos repetir este experimento.

Dada uma grade de n linhas e m colunas representando o lago, 6 ≤ n, m ≤ 10000, encontre o menor número de sonares que você precisa colocar no lago de tal forma que podemos controlar todas as posições da grade, com as seguintes condições:

Um sonar ocupa uma posição da grade; O sonar controla sua própria posição, além das suas posições adjacentes;
As posições nas bordas da grade não precisam ser controladas, pois Nessie não conseguiria se esconder nelas (ela é grande demais para isso).
Considere as seguintes figuras:

 

Nas figuras, X representa um sonar, e as posições escuras representam as posições controladas por sonares. A última figura exemplifica uma solução para o problema.

Entrada
A primeira linha da entrada contém um inteiro t, indicando o número de casos de teste. Cada caso de teste é descrito por uma linha contendo dois inteiros separados por um espaço, n e m (6 ≤ n, m ≤ 10000), indicando o tamanho da grade (n linhas e m colunas).

Saída
Para cada caso de teste, imprima uma linha contendo o menor número de sonares necessários.
'''
import math

n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    
    print(math.ceil((a - 2) / 3) * math.ceil((b - 2) / 3))
