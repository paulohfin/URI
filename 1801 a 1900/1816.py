'''
Vestígios de uma antiga civilização viking foram descobertos nos arredores de Praga, e uma grande quantidade de material impresso foi achada junto ao sítio arqueológico. Como esperado, a leitura deste material mostrou-se uma tarefa árdua e desafiadora, já que essa civilização utilizava um esquema de codifucação de texto para evitar que seu conhecimento fosse assimilado por seus rivais.

Recentemente, pesquisadores tchecos anunciaram com grande euforia à imprensa a compreensão do mecanismo de codificação utilizado por esses vikings. De acordo com os pesquisadores, o alfabeto viking era composto pelas letras de A até Z (incluindo as letras K, W e Y).

A codificação era realizada da forma que segue. Inicialmente, era construída uma lista em que a letra A aparecia na primeira posição, a letra B aparecia na segunda, e assim sucessicamente,com as letras sequindo a mesma ordem que em nosso alfabeto. Em sequida, o texto a ser codificado era barrido da esquerda para a direita e, para cada letra l encontrada, o número de sua posição na lista era impresso e l era movida para o início da lista. Por exemplo, a codificação viking para a mensagem:

A B B B A A B B B B A C C A B B A A A B C

era dada pela seguinte sequência de inteiros:

1 2 1 1 2 1 2 1 1 1 2 3 1 2 3 1 2 1 1 2 3

Os pesquisadores tchecos pediram sua ajuda para construir um programa que recebe uma sequência de inteiros que representa uma mensagem codificada e decodifica-a.

Entrada
Seu programa deve estar preparado para trabalhar com diversas instâncias. Cada instância tem a estrutura que segue. Na primeira linha é fornecido um inteiro m (0 ≤ m ≤ 10000) que representa o número de inteiros que compõem o texto codificado. Na próxima linha são dados, separados por espaços em branco, os m valores inteiros (cada valor é maior ou igual a 1 e menor ou igual a 26). Um valor m = 0 indica o final das instâncias e não ser processado.

Saída
Para cada instância solucionada, você deverá imprimir um identificador Instancia h em que h é um número inteiro, sequêncial e crescente a partir de 1. Na linha seguinte, você deve imprimir o texto decodificado. Uma linha em branco deve ser impressa após cada instância.
'''
n = int(input())
j = 1
while n != 0:
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    linha = input().split(' ')
    print('Instancia ' + str(j))
    
    for i in linha:
        if i.isnumeric():
            k = alpha[int(i)-1]
            print(k,end='')
            alpha.remove(k)
            alpha.insert(0,k)
        
    print('\n')
    n = int(input())
    j += 1
