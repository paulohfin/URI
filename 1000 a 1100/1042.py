'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''
a, b,c = map(int, input().split(' '))

lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print()
print(a)
print(b)
print(c)
