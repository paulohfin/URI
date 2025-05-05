'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo
'''
i = 1
j = 7

while i < 10:
    print('I=' + str(i) + ' J=' + str(j))
    print('I=' + str(i) + ' J=' + str(j-1))
    print('I=' + str(i) + ' J=' + str(j-2))
    i+=2
