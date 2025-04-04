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