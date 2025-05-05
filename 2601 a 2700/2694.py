'''
Joãozinho tem que ajudar seu pai. Um relatório específico com alguns números está saindo com caracteres indesejáveis no meio. A ideia é apenas somar os 3 valores que aparecem em cada linha sempre na mesma posição, ignorando as letras e apresentar esta soma. Não existem espaços em branco na linha.

Entrada
A primeira linha de entrada contém um inteiro N (N < 100000). Seguem N linhas com exatos 14 caracteres que devem ser lidas e delas extraídos e somados os três números existentes.

Saída
Para cada linha de entrada, seu programa deve apresentar um valor numérico inteiro, que é a soma dos 3 números existentes na linha.
'''
n = int(input())
for i in range(n):
    num = []
    hame = input()
    v = False
    k = 0
    for j in hame:
        if ord(j) >= ord('0') and ord(j) <= ord('9'):
            if v == False:
                v = True
                k = int(j)
            else:
                k = k * 10 + int(j)
        else:
            if v == True:
                v = False
                num.append(k)
                k = 0
    if v == True:
        num.append(k)
    soma = 0 
    for j in num:
        soma += j 
    print(soma)
