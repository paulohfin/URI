'''
Você sempre fica tão animado nesta época do ano que adora falar sobre isso o tempo todo! Neste ano, você tem gritado aos quatro ventos: Então é natal!! Colocando toda essa felicidade pra fora, você montou novamente um programa neste ano que, colocando um índice I de felicidade, seu grito de "Então é Natal!" é cada vez mais animado!

Entrada
A entrada é composta por um inteiro I (1 < I ≤ 104) que representa o seu índice de felicidade.

Saída
A saída é composta pela frase "Entao eh Natal!", sendo repetidas I vezes as letras a da frase. Uma quebra de linha é necessária após a impressão da frase.
'''
while True:
    try:
        n = int(input())
        print('Ent',end='')
        for i in range(n):
            print('a',end='')
        print('o eh N',end='')
        for i in range(n):
            print('a',end='')
        print('t',end='')
        for i in range(n):
            print('a',end='')
        print('l!')
    except EOFError:
        break 
