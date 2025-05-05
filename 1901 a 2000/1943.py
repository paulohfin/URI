'''
Recentemente aconteceu a fase regional da Maratona de Programação da SBC, onde mais de 600 times participaram em mais de 40 sedes diferentes pelo Brasil. Seu amigo participou da competição, e quando questionado sobre sua colocação lhe disse: “Ficamos no top 10”.

Você ficou feliz pelo seu amigo, mas não pode deixar de ficar curioso sobre qual foi sua real colocação. “Top 10” poderia indicar qualquer posição entre primeiro e décimo colocado, porém se ele estivesse em primeiro provavelmente teria dito “Top 1”, se estivesse em segundo ou terceiro provavelmente teria dito “Top 3”, e se estivesse em quarto ou quinto provavelmente teria dito “Top 5”. Logo, sua real colocação foi entre sexto e décimo, pois as pessoas geralmente se colocam na menor categoria a qual pertencem.

Você reuniu então todas as categorias de colocações que as pessoas mais usam: 1, 3, 5, 10, 25, 50 e 100. Dada uma colocação K, diga o número da menor categoria que esta colocação pertence.

Entrada
Cada caso de teste contém um inteiro K, representando uma colocação (1 ≤ K ≤ 100).

Saída
Para cada caso de teste imprima uma linha contendo a frase “Top N”, e substitua a letra N pelo número da menor categoria que a colocação K pertence.
'''
while True:
    try:
        n = int(input())
        if n == 1:
            print('Top 1')
        elif n <= 3:
            print('Top 3')
        elif n <= 5:
            print('Top 5')
        elif n <= 10:
            print('Top 10')
        elif n <= 25:
            print('Top 25')
        elif n <= 50:
            print('Top 50')
        elif n <= 100:
            print('Top 100')
    except EOFError:
        break
