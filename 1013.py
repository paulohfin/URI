'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

def abs(a):
    if a >= 0: return a
    else: return -a

def maior(a, b):
    return (a + b + abs(a - b))/2

a1, a2, a3 = map(int, input().split(' '))

m = maior(a1, maior(a2, a3))

print(int(m), 'eh o maior')
