'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.
'''
while True:
    try:
        x,y = map(int, input().split(' '))
        
        if x == 0 or y == 0:
            break
        elif x > 0:
            if y > 0:
                print('primeiro')
            else:
                print('quarto')
        else:
            if y > 0:
                print('segundo')
            else:
                print('terceiro')
            

    except EOFError:
        break
