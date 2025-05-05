'''
Ao observar a paisagem da Nlogônia, o professor MC percebeu que a cada intervalo de 100 metros existe um pico. E que exatamente na metade de dois picos há um vale. Logo, a cada 50 metros há um vale ou um pico e, ao longo da paisagem, não há um pico seguido por outro pico, nem um vale seguido por outro vale.

O professor MC ficou curioso com esse padrão e quer saber se, ao medir outras paisagens, isso se repete. Sua tarefa é, dada uma paisagem, indicar se ela possui esse padrão ou não.

Entrada
A entrada é dada em duas linhas. A primeira tem o número N de medidas da paisagem (1 < N ≤ 100). A segunda linha tem N inteiros: a altura Hi de cada medida (-10000 ≤ Hi ≤ 10000, para todo Hi, tal que 1 ≤ i ≤ N). Uma medida é considerada um pico se é maior que a medida anterior. Uma medida é considerada um vale se é menor que a medida anterior.

Saída
A saída é dada em uma única linha. Caso a paisagem tenha o mesmo padrão da Nlogônia, deve ser mostrado o número 1. Caso contrário, mostra-se o número 0.
'''
n = int(input())
k = input().split(' ')
z = 1
if n > 2:
    for i in range(len(k) - 2):
        if (int(k[i+2]) > int(k[i+1]) and int(k[i+1]) < int(k[i])) or (int(k[i+2]) < int(k[i+1]) and int(k[i+1]) > int(k[i])):
            z = 1 
        else:
            z = 0
elif n == 2:
    if k[0] == k[1]:
        z = 0
print(z)
