'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''
a = []
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
pos = 0

for i in range(len(a)):
    if a[i] > 0:
        pos += 1
        
print(pos, 'valores positivos')
