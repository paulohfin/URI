'''
A empresa Animações Livres de Falhas, ou ALF, realiza as mais diversas animações usando apenas caracteres na tela. Um dia, foram desafiados a fazer uma animação de uma Espiral Quadrada. Esta deverá proceder da seguinte forma:

*Sempre exibirá uma tabela quadrada, com N linhas e N colunas, com um caractere em seu respectivo lugar, sem espaços entre os mesmos;

*Esta quantidade N será sempre ímpar;

*O primeiro quadro desta animação será com um caractere ‘X’ no centro da tabela e o restante da mesma ocupado com caracteres ‘O’;

*Nos quadros seguintes, o caractere ‘X’ será deslocado para os outros locais da tabela, substituindo onde o mesmo estava com ‘O’, exibindo sempre uma vez o ‘X’ em cada quadro. O deslocamento será no formato de uma espiral quadrada, realizando o deslocamento para direita, para cima, para esquerda e para baixo. Veja um exemplo de todos os quadros da animação com N = 5:



Escreva um programa que, dado um número inteiro, imprima todos os quadros da animação da espiral quadrada.

Entrada
Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro N (1 ≤ N ≤ 25), indicando o tamanho da tela.

O último caso de teste é indicado quando N = 0, sendo que este caso não deverá ser processado.

Saída
Para cada caso de teste imprima N x N tabelas, cada uma separada com um ‘@’, seguindo as regras da animação como descritas anteriormente.
'''
def printar(n, posx, posy):
    for i in range(n):
        for j in range(n):
            if i == posy and j == posx:
                print('X', end='')
            else:
                print('O', end='')
        print()
    print('@')

n = int(input())
while n != 0:
    meio = int(n / 2)
    posx = meio
    posy = meio
    printar(n, posx, posy)
    add = 1
    posx += 1
    while posx < n:
        printar(n, posx, posy)
        
        while posy > meio - add:
            posy -= 1
            printar(n, posx, posy)
        
        while posx > meio - add:
            posx -= 1
            printar(n, posx, posy)
            
        while posy < meio + add:
            posy += 1
            printar(n, posx, posy)
            
        while posx < meio + add:
            posx += 1
            printar(n, posx, posy)
        posx += 1
        add += 1
        
    n = int(input())
