'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''
soma = 0.0
pos = 0
for i in range(6):
    n = float(input())
    if n > 0:
        soma += n
        pos += 1
print(pos,'valores positivos')
print('%.1f' %(soma/pos))
