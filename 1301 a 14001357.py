'''
O sistema Braille, desenvolvido por Louis Braille em 1825, revolucionou a comunicação escrita para as pessoas cegas e visualmente debilitadas. Braille, um francês cego, desenvolveu uma linguagem tátil onde cada elemento é representado por uma célula com seis posições, arranjadas em três fileiras e duas colunas. Cada posição pode ser relevada ou não, permitindo 64 configurações diferentes que podem ser sentidas por dedos treinados. A figura abaixo mostra a representação Braille para os dígitos decimais (um ponto preto indica uma posição relevada).

​

De modo a desenvolver um novo sistema de software para ajudar professores a lidar com estudantes cegos ou visualmente debilitados, um módulo de dicionário Braille é necessário. Dada uma mensagem, composta apenas por dígitos, seu trabalho é traduzi-la para ou do Braille. Você pode ajudar?

Entrada
Cada caso de teste é descrito usando três ou cinco linhas. A primeira linha contém um inteiro D representando o número de dígitos em uma mensagem (1 ≤ D ≤ 100). A segunda linha contém uma única letra maiúscula 'S' ou 'B'. Se a letra é 'S', a próxima linha contém uma mensagem composta de D dígitos decimais que seu programa deve traduzir para o Braille. Se a letra é 'B', as próxima três linhas contém uma mensagem composta de D células Braille que seu programa deve traduzir do Braille. As células Braille são separadas por espaços simples. Em cada célula Braille uma posição relevada é denotada pelo caractere '*' (asterisco), enquanto uma não relevada é denotada por um caractere '.' (ponto).

O último caso de teste é seguido por uma linha contendo um zero.

Saída
Para cada caso de teste imprima apenas os dígitos da tradução correspondente, no mesmo formato que a entrada (veja os exemplos para maiores explicações).
'''
n = int(input())

while n != 0:
    l = input()
    if l == 'S':
        ler = input()
        for i in range(len(ler)):
            if ler[i] == '1' or ler[i] == '2' or ler[i] == '5' or ler[i] == '8':
                print('*.',end='')
            elif ler[i] == '3' or ler[i] == '4' or ler[i] == '6' or ler[i] == '7':
                print('**',end='')
            elif ler[i] == '9' or ler[i] == '0':
                print('.*',end='')
                
            if i != n-1:
                print(' ',end='')
        print()
        for i in range(len(ler)):
            if ler[i] == '1' or ler[i] == '3':
                print('..',end='')
            elif ler[i] == '2' or ler[i] == '6' or ler[i] == '9':
                print('*.',end='')
            elif ler[i] == '4' or ler[i] == '5':
                print('.*',end='')
            elif ler[i] == '7' or ler[i] == '8' or ler[i] == '0':
                print('**',end='')
            if i != n-1:
                print(' ',end='')
        print()
        for i in range(len(ler)):
            if i == n-1:
                print('..')
            else:
                print('.. ',end='')
                
    else:
        l1 = input().split(' ')
        l2 = input().split(' ')
        l3 = input().split(' ')
        for i in range(len(l1)):
            if l1[i] == '*.':
                if l2[i] == '..':
                    print(1,end='')
                elif l2[i] == '*.':
                    print(2,end='')
                elif l2[i] == '.*':
                    print(5,end='')
                elif l2[i] == '**':
                    print(8,end='')
            elif l1[i] == '**':
                if l2[i] == '..':
                    print(3,end='')
                elif l2[i] == '.*':
                    print(4,end='')
                elif l2[i] == '*.':
                    print(6,end='')
                elif l2[i] == '**':
                    print(7,end='')
            else:
                if l2[i] == '*.':
                    print(9,end='')
                elif l2[i] == '**':
                    print(0,end='')
        print()
    n = int(input())