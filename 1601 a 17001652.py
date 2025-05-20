'''
Sra. Deli está trabalhando em uma casa de mercearias finas "Deli Deli". No ano passado, a Sra. Deli decidiu expandir seu negócio e construir uma loja online. Ela contratou um programador que implementou a loja online.

Recentemente alguns de seus novos clientes online reclamaram das notas fiscais eletrônicas. O programador esqueceu-se de usar o plural, no caso em que um item é comprado várias vezes. Infelizmente o programador da Sra. Deli está de férias e agora é sua tarefa de implementar esse recurso para a Sra. Deli. Aqui está uma descrição de como fazer o plural:

Se a palavra está na lista de palavras irregulares substitua-a com o plural dado.
Senão se a palavra termina em uma consoante seguida por "y", substitua "y" por "ies".
Senão se a palavra termina em "o", "s", "ch", "sh" ou "x", acrescente "es" à palavra.
Senão acrescente "s" à palavra.
Entrada
A primeira linha do arquivo de entrada consiste de dois inteiros L e N (0 ≤ L ≤ 20, 1 ≤ N ≤ 100). As seguintes L linhas contém a descrição das palavras irregulares e sua forma plural. Cada linha é composta de duas palavras separadas por um caractere de espaço, onde a primeira palavra é o singular, a segunda palavra é a forma plural de uma palavra irregular. Depois da lista de palavras irregulares, as N linhas seguintes contém uma palavra cada, que você tem que transformar para o plural. Você pode assumir que cada palavra é composta de no máximo 20 letras minúsculas do alfabeto Inglês ('a' a 'z').

Saída
Imprima N linhas na saída, onde a i-ésima linha é a forma plural da i-ésima palavra de entrada.
'''
l, n = map(int, input().split(' '))

palavras = []
for i in range(l):
    palavras.append(input().split(' '))
for i in range(n):
    pal = input()
    k = len(pal)
    irregular = False
    for j in range(l):
        if pal == palavras[j][0]:
            print(palavras[j][1])
            irregular = True
    if irregular == False:
        if pal[k-1] == 'y' and pal[k-2] != 'a' and pal[k-2] != 'e' and pal[k-2] != 'i' and pal[k-2] != 'o' and pal[k-2] != 'u':
            print(pal[:k-1] + 'ies')
        elif pal[k-1] == 'o' or pal[k-1] == 's' or pal[k-1] == 'x':
            print(pal + 'es')
        elif pal[k-2:] == 'ch' or pal[k-2:] == 'sh':
            print(pal + 'es')
        else:
            print(pal + 's')