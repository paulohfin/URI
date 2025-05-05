'''
Uma fábrica produz barras de chocolates no formato de paralelepípedos e de cubos, com o mesmo volume. Porém, como a máquina que produz os chocolates em formato de cubo está apresentando alguns problemas, os donos da fábrica pediram a sua ajuda para resolver este problema.

Sua tarefa é, dadas as dimensões das arestas do chocolate em formato de paralelepípedo, dizer qual é o tamanho que a aresta em formato de cubo deve ter.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém três inteiros A, B e C (1 ≤ A, B, C ≤ 103), indicando os tamanhos das arestas do chocolate em formato de paralelepípedo. A entrada termina quando A = B = C = 0, e não deve ser processado.

Saída
Para cada entrada, você deve imprimir um único inteiro que deve ser truncado,representando o tamanho da aresta do chocolate em forma de cubo.
'''
import math

a, b, c = map(int, input().split(' '))

while a != 0 and b != 0 and c != 0:
    aresta = math.pow(a * b * c, 1/3)
    print(int(aresta))
    a, b, c = map(int, input().split(' '))
