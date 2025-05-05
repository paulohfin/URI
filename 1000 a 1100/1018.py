'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
n = int(input())
temp = n
a1 = int(n / 100)
n -= a1 * 100

a2 = int(n / 50)
n -= a2 * 50

a3 = int(n / 20)
n -= a3 * 20

a4 = int(n / 10)
n -= a4 * 10

a5 = int(n / 5)
n -= a5 * 5

a6 = int(n / 2)
n -= a6 * 2

a7 = int(n)
print(temp)
print(a1,'nota(s) de R$ 100,00')
print(a2,'nota(s) de R$ 50,00')
print(a3,'nota(s) de R$ 20,00')
print(a4,'nota(s) de R$ 10,00')
print(a5,'nota(s) de R$ 5,00')
print(a6,'nota(s) de R$ 2,00')
print(a7,'nota(s) de R$ 1,00')
