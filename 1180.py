n = int(input())
linha = input().split(' ')

i = 0
while linha[i] == '':
    i += 1
minimo = linha[i]
pos = i
post = 0

for i in range(len(linha)):
    if linha[i] == '':
        post += 1
        continue
    else:
        if int(linha[i]) < int(minimo):
            minimo = int(linha[i])
            pos = i - post
       

print('Menor valor: ' + str(minimo))
print('Posicao: ' + str(pos))