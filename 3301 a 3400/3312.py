'''
Guilherme tem dez anos e é um pequeno entusiasta da matemática, e descobriu recentemente a existência dos famosos números primos. Com seu grande interesse pela disciplina, sua professora Marlene já lhe adiantou alguns conteúdos e um deles é o fatorial. Guilherme adora fazer exercícios e deseja treinar mais para preparar‐se para a Olimpíada de Matemática. Marlene passou uma lista de números para Guilherme resolver em casa, na qual todos os números primos encontrados deverão ser encontrados também seu respectivo fatorial. Ajude Guilherme a conferir seus exercícios e estudar para a Olimpíada

Entrada
A primeira linha da entrada contém um inteiro N indicando a quantidade de números a serem lidos. A segunda linha tem N números inteiros entre 1 e 100.

Limites:

1 ≤ N ≤ 100000;

Saída
A saída contém a quantidade de linhas representadas dos números que são primos, dentre os N números lidos. Em cada linha deve apresentar o número lido, seguido de um ponto de exclamação, um espaço, seguido por um sinal de igual, mais um espaço e o fatorial correspondente deste número
'''
def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fatorial(n):
    if n < 2:
        return 1 
    else:
        return n * fatorial(n - 1)

while True:
    try:
        n = int(input())
        linha = input().split(' ')
        
        for i in linha:
            
            if i != '':
                if primo(int(i)):
                    print(i + '! =',fatorial(int(i)))
    except EOFError:
        break
