'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
'''
soma = 1
i =  3
j = 2
while i < 40:
    #print(soma, '+' + str(i) + '/' + str(j))
    soma += float(i / j)
    i += 2
    j *= 2
print('%.2f' %soma)
