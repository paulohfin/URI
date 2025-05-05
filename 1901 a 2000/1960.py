'''
A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata de numerar as páginas de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas pois, quando necessário, dividem o livro em volumes.

Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na numeração romana.

Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000.

Entrada
A entrada é um número inteiro positivo N (0 < N < 1000).

Saída
A saída é o número N escrito na numeração romana em uma única linha. Use sempre letras maiúsculas.
'''
def cprint(n):
    if n == 100:
        print('C',end='')
    elif n == 200:
        print('CC',end='')
    elif n == 300:
        print('CCC',end='')
    elif n == 400:
        print('CD',end='')
    elif n == 500:
        print('D',end='')
    elif n == 600:
        print('DC',end='')
    elif n == 700:
        print('DCC',end='')
    elif n == 800:
        print('DCCC',end='')
    elif n == 900:
        print('CM',end='')
def dprint(n):
    if n == 10:
        print('X',end='')
    elif n == 20:
        print('XX',end='')
    elif n == 30:
        print('XXX',end='')
    elif n == 40:
        print('XL',end='')
    elif n == 50:
        print('L',end='')
    elif n == 60:
        print('LX',end='')
    elif n == 70:
        print('LXX',end='')
    elif n == 80:
        print('LXXX',end='')
    elif n == 90:
        print('XC',end='')
def uprint(n):
    if n == 1:
        print('I',end='')
    elif n == 2:
        print('II',end='')
    elif n == 3:
        print('III',end='')
    elif n == 4:
        print('IV',end='')
    elif n == 5:
        print('V',end='')
    elif n == 6:
        print('VI',end='')
    elif n == 7:
        print('VII',end='')
    elif n == 8:
        print('VIII',end='')
    elif n == 9:
        print('IX',end='')

while True:
    try:
        n = int(input())
        cprint(int(n/100) * 100)
        n -= 100 * int(n/100)
        dprint(int(n/10) * 10)
        n -= 10 * int(n/10)
        uprint(n)
        print()
    except EOFError:
        break 
