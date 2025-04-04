'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
din = float(input())

print("NOTAS:")
print(int(din/100),"nota(s) de R$ 100.00")
din -= int(din/100) * 100

print(int(din/50),"nota(s) de R$ 50.00")
din -= int(din/50) * 50

print(int(din/20),"nota(s) de R$ 20.00")
din -= int(din/20) * 20

print(int(din/10),"nota(s) de R$ 10.00")
din -= int(din/10) * 10

print(int(din/5),"nota(s) de R$ 5.00")
din -= int(din/5) * 5

print(int(din/2),"nota(s) de R$ 2.00")
din -= int(din/2) * 2

print("MOEDAS:")
print(int(din),"moeda(s) de R$ 1.00")
din -= int(din)
din *= 100
print(int(din/50),"moeda(s) de R$ 0.50")
din -= int(din/50) * 50

print(int(din/25),"moeda(s) de R$ 0.25")
din -= int(din/25) * 25

print(int(din/10),"moeda(s) de R$ 0.10")
din -= int(din/10) * 10

print(int(din/5),"moeda(s) de R$ 0.05")
din -= int(din/5) * 5

print(int(din),"moeda(s) de R$ 0.01")
