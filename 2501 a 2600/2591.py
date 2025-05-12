'''
O Hamekameka foi inventado por Mestre Hame praticado por cinquenta anos antes de conhecer Kogu. Chamando sua energia latente nas palmas de suas mãos, Hame consegue lançar um raio explosivo de energia. Kogu aprende após ver Mestre Hame usando-o para apagar as chamas na casa de um Rei. Para a surpresa de Hame, Kogu consegue performar a técnica de primeira, embora seja apenas forte o suficiente para destruir o carro que Chamya deu para Mulba. Kogu descobriu que há um padrão na pronúncia correta deste ataque, de modo que, se não for pronunciado corretamente, o mesmo não acontece.

Escreva um programa que, dada a parte inicial de um Hamekameka, faça a finalização ideal para que o ataque seja realizado com sucesso.

Entrada
A entrada começa com um valor C, indicando a quantidade de casos de teste. Em seguida, temos C linhas, cada uma com o início de um ataque, com, no máximo, 200 letras.

Saída
Para cada caso de teste, imprima a finalização adequada, para que o ataque se concretize.
'''
n = int(input())

for i in range(n):
    hame = input().split('k')
    a1 = hame[0].count('a')
    a2 = hame[1].count('a')
    print('k', end='')
    for j in range(a1 * a2):
        print('a', end='')
    print()
