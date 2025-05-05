'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''
n = int(input())
nc = 0
nr = 0
ns = 0
total = 0
for i in range(n):
    a, b = input().split(' ')
    if b == 'C':
        nc += int(a)
    if b == 'R':
        nr += int(a)
    if b == 'S':
        ns += int(a)
    total += int(a)
print('Total: ' + str(total) + ' cobaias')
print('Total de coelhos: ' + str(nc))
print('Total de ratos: ' + str(nr))
print('Total de sapos: ' + str(ns))
print('Percentual de coelhos: %.2f' %(nc/total * 100) + ' %')
print('Percentual de ratos: %.2f' %(nr/total * 100) + ' %')
print('Percentual de sapos: %.2f' %(ns/total * 100) + ' %')
