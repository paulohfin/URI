'''
Espero que você esteja curtindo a competição :D.

Nós, os autores (Diego Rangel, Francisco Arcos, Gabriel Duarte e Gustavo Policarpo), estamos felizes por você estar tentando resolver nossos problemas. Para você que é iniciante não sair da sala sem nenhum balão, aqui vai um desafio para você:

Neste ano os balões têm formato esférico, segundo a empresa que produz os balões: "(...) por motivos complexos de engenharia esse formato é melhor (...)" vai entender...
Entretanto esse formato faz com que o balão use mais gás hélio e isso causou um problema, pois o organizador já havia comprado um tanque com L litros de gás antes dessa novidade no mercado de balões.
Sabendo o raio do modelo de balões e a quantidade de gás hélio disponível, você poderia ajudar a equipe dizendo quantos balões podem ser enchidos completamente?

Entrada
A entrada é composta por dois inteiros R e L (1 ≤  R, L ≤ 109), que são o raio e a quantidade de gás disponível, respectivamente. 

Considere PI = 3.1415

Saída
Você deve imprimir um único inteiro representando a quantidade de balões que podem ser enchidos completamente com a quantidade de gás hélio disponível.
'''
while True:
    try:
        r, l = map(int, input().split(' '))
        v = 4/3 * 3.1415 * r * r * r
        print(int(l / v))
    except EOFError:
        break
