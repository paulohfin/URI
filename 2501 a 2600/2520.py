'''
Analógimôn Go! é um jogo bastante popular. Em sua jornada, o jogador percorre diversas cidades capturando pequenos monstrinhos virtuais, chamados analógimôns. Você acabou de chegar em uma cidade que contém o último analógimôn que falta para sua coleção!

A cidade pode ser descrita como um grid de N linhas e M colunas. Você está em uma dada posição da cidade, enquanto o último analógimôn está em outra posição da mesma cidade. A cada segundo, você pode se mover (exatamente) uma posição ao norte, ao sul, a leste ou a oeste. Considerando que o analógimôn não se move, sua tarefa é determinar o menor tempo necessário para ir até a posição do monstrinho.

A figura abaixo descreve o exemplo da entrada, e apresenta um caminho percorrido em 5 segundos. Outros caminhos percorridos no mesmo tempo são possíveis, mas não há outro caminho que pode ser percorrido em um tempo menor.



Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém dois inteiros N e M (2 ≤ N, M ≤ 100), o número de linhas e de colunas na cidade, respectivamente. As próximas N linhas contém M inteiros cada, descrevendo a cidade. O inteiro 0 indica uma posição em branco; o inteiro 1 indica a sua posição na cidade; o inteiro 2 indica a posição do analógimôn na cidade. É garantido que haverá exatamente um inteiro 1 e exatamente um inteiro 2 na descrição da cidade, e que os demais inteiros serão iguais a 0.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma linha contendo o menor tempo necessário para ir até o monstrinho, em segundos.
'''
def dif(a, b):
    if b > a:
        return b - a 
    else:
        return a - b

while True:
    try:
        n, m = map(int, input().split(' '))
        x1 = x2 = y1 = y2 = 0
        for i in range(n):
            l = input().split(' ')
            for j in range(len(l)):
                if l[j] == '1':
                    x1 = i + 1  
                    y1 = j + 1
                if l[j] == '2':
                    x2 = i + 1
                    y2 = j + 1
        
        print(dif(x1,x2) + dif(y1,y2))
    except EOFError:
        break
