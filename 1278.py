n = int(input())
while True:
    texto = []
    texto2 = []
    for i in range(n):
        texto.append(input())
    maximo = 0
    for i in texto:
        temp = []
        linha = 0
        for j in i.split(' '):
            if j != '':
                temp.append(j)
                linha += len(j)
        linha += len(temp)
        temp.append(linha)
        if linha > maximo:
            maximo = linha
        texto2.append(temp)
    for i in range(len(texto2)):
        for j in range(maximo - texto2[i][len(texto2[i]) - 1]):
            print(' ', end='')
            
        for j in range(len(texto2[i]) - 1):
            if j < len(texto2[i]) - 2:
                print(texto2[i][j], end = ' ')
            else:
                print(texto2[i][j])
    n = int(input())
    if n == 0:
        break
    else:
        print()