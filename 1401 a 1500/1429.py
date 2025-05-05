'''
Mateus, um calouro de engenharia, está desenvolvendo uma nova notação posicional para representar números inteiros. Ele o apelidou de "A Curious Method" ("Um Método Curioso"), representado pela sigla ACM. A notação ACM usa os mesmos dígitos que a notação decimal, isto é, de 0 a 9.

Para converter um número A da notação ACM para a notação decimal, você deve adicionar k termos, onde k é o número de dígitos de A (na notação ACM), O valor do i-ésimo termo, correspondente ao i-ésimo dígito ai, contando da direita para a esquerda, é ai × i!. Por exemplo, 719ACM é equivalente a 5310, já que 7 × 3! + 1 × 2! + 9 × 1! = 53.

Mateus acabou de iniciar seus estudos sobre teoria dos números, e provavelmente não sabe quais propriedades um sistema numérico deve ter, mas no momento, ele só está interessado em converter um número de ACM para decimal. Você pode ajudá-lo?

Entrada
Cada caso de teste é dado por uma única linha não-nula contendo, no máximo, 5 dígitos, representando um número na notação ACM. A linha não possui zeros no início.

O último caso de teste é representado por uma linha contendo um único zero.

Saída
Para cada caso de teste, escreva uma única linha contendo a representação decimal do número ACM correspondente.
'''
def fatorial(n):
    if n == 0:
        return 1
    else: return n * fatorial(n - 1)

while True:
    palavra = input()
    if palavra !='0':
        j = len(palavra)
        soma = 0
        for i in range(len(palavra)):
            soma += (ord(palavra[i]) - ord('0')) * fatorial(j)
            j-=1

        print(soma)
    else: break
