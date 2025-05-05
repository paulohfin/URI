'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado abaixo (área verde).




Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante de dupla precisão (double) que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''
c = input()

soma = 0.0
for i in range(12):
    for j in range(12):
        valor = float(input())
        if i > j and i + j > 11:
            soma += valor
if c == 'S':
    print('%.1f' %(soma))
else:
    print('%.1f' %(soma/30))
