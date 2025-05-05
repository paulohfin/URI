'''
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.
'''
a = 0
g = 0
d = 0

n = 0
while n != 4:
    n = int(input())
    if n == 1:
        a += 1 
    elif n == 2:
        g += 1 
    elif n == 3:
        d += 1
print('MUITO OBRIGADO')
print('Alcool:', a)
print('Gasolina:', g)
print('Diesel:', d)
