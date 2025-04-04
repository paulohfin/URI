'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''
a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
pos = 0
neg = 0
par = 0
impar = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        par += 1
    else:
        impar += 1
    if a[i] > 0:
        pos += 1
    if a[i] < 0:
        neg += 1

        
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s)')
