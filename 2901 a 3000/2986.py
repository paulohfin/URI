'''
Uma vez, enquanto estudavamos pra Maratona de Porgramção, Tobias e eu nos deparamos com um problema interesante, espero que vocês também gostem.

Existe uma escada com N degraus. Você pode escolher entre descer 1, 2, ou 3 degraus por vez a cada movimento. De quantas maneiras diferentes você poderia descer essa escada com N degraus?

Entrada
Um único número inteiro N (1 ≤ N ≤ 100.000), o número de degraus na escada.

Saída
Um único inteiro, o número combinações de formas diferentes de descer a escada. A resposta pode ser um pouco grande, então imprima o resto da divisão pelo nosso primo favorito (109+7).
'''
def degrau(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a = 1 
        b = 2
        c = 4
        for i in range(n - 3):
            temp = a + b + c
            a = b
            b = c
            c = temp
            c %= 1000000007
        return c

while True:
    try:
        n = int(input())
        print(degrau(n))
    except EOFError:
        break
