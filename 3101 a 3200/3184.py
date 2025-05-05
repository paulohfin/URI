'''
Nós estamos construindo um jogo de computador old-school. É um simples jogo de aventura baseado em textos onde você anda por aí e encontra tesouros, evitando cair em armadilhas.

Ele é jogado em uma grid retangular e a jogadora obtém informações muito limitadas sobre seus arredores. O jogo consistirá na jogadora se movendo pelo grid pelo tempo que ela quiser (ou até ela cair em uma armadilha). A jogadora pode mover para cima, baixo, esquerda e direita (mas não na diagonal). Ela obterá ouro se ela estiver no mesmo quadrado em que o ouro está. Se a jogadora estiver próxima (ou seja, no lado de cima, baixo, esquerda ou direita de) uma ou mais armadilhas, ela vai “sentir uma corrente de ar”, mas não saberá de qual direção esta corrente vem, ou de quantas armadilhas ela está perto. Se ela tentar se mover para um quadrado que contém uma parede, ela será notificada que há uma parede naquela direção e permanecerá onde ela estava antes.

Para fins de pontuação, nós queremos mostrar à jogadora quantos ouros ela poderia ter obtido com segurança. Isto é, quantos ouros uma jogadora pode conseguir jogando com uma ótima estratégia e sempre tendo certeza de que aquele quadrado que ela se mover é seguro. A jogadora não tem acesso ao mapa e os mapas são gerados aleatoriamente para cada jogo, de modo que ela não possua nenhum conhecimento prévio do jogo.

Entrada
A primeira linha contém dois inteiros positivos W e H, sendo nenhum deles menor que 3 ou maior que 50, assumindo a largura e a altura do mapa respectivamente. As próximas H linhas contém W caracteres cada, que são os quadrados do mapa. Os símbolos que podem aparecer no mapa são os seguintes:

                P – A posição inicial da jogadora

                G – Uma pepita de ouro

                T – Uma armadilha

                # – Uma parede

    . – Um chão normal

Haverá apenas um único ‘P’ no mapa, e a borda do mapa sempre conterá paredes.

Saída
Imprima o número de pepitas de ouro que a jogadora consegue sem o risco de cair em uma armadilha.
'''
w, h = map(int,input().split(' '))
linha = []
for i in range(h):
    linha.append(list(input()))
ouro = 0
mudar = True
while mudar == True:
    mudar = False
    for i in range(h):
        for j in range(w):
            if linha[i][j] == 'P':
                linha[i][j] = '*'
                mudar = True
            elif linha[i][j] == '*':
                if linha[i + 1][j] == 'T' or linha[i - 1][j] == 'T' or linha[i][j + 1] == 'T' or linha[i][j - 1] == 'T':
                    linha[i][j] = '#'
                else:
                    if linha[i + 1][j] == 'G':
                        linha[i + 1][j] = '*'
                        ouro += 1
                        mudar = True
                    elif linha[i + 1][j] == '.':
                        linha[i + 1][j] = '*'
                        mudar = True
                        
                    if linha[i - 1][j] == 'G':
                        linha[i - 1][j] = '*'
                        ouro += 1
                        mudar = True
                    elif linha[i - 1][j] == '.':
                        linha[i - 1][j] = '*'
                        mudar = True
                        
                    if linha[i][j + 1] == 'G':
                        linha[i][j + 1] = '*'
                        ouro += 1
                        mudar = True
                    elif linha[i][j + 1] == '.':
                        linha[i][j + 1] = '*'
                        mudar = True
                        
                    if linha[i][j - 1] == 'G':
                        linha[i][j - 1] = '*'
                        ouro += 1
                        mudar = True
                    elif linha[i][j - 1] == '.':
                        linha[i][j - 1] = '*'
                        mudar = True
print(ouro)
