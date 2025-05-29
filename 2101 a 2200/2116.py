'''
Juilherme e Jogério, gostam muito de jogos matemáticos. Juilherme acabou de criar mais um jogo matemático para eles se divertirem enquanto assistem essa competição online.

O jogo consiste nos seguintes passos:

1) Juilherme escolhe um número N e Jogério escolhe um número M.
2) Juilherme e Jogério devem então achar dois números primos P1 e P2, de tal forma que eles sejam o mais próximo possível do que numero N e M, respectivamente. Além disso P1 deve ser menor ou igual a N e P2 deve ser menor ou igual a M.
3) A resposta final do desafio é encontrar a multiplicacão de P1 e P2. Quem achar a resposta primeiro é o vencedor.

Como eles irão tentar achar a resposta o mais rápido possível, algumas vezes chegando a resultados incorretos, eles precisam de um programa que entregue a resposta final do jogo, para que possa ser comparada com a resposta encontrada por eles.

Usando as informacoes do jogo, faça um programa que dado os números N e M imprima o resultado final.

Entrada
A entrada do programa consiste de apenas uma linha com N e M (2 <= N, M <= 1000).

Saída
A saída do seu programa deve conter apenas uma linha informando a resposta final do jogo.
'''
def prim(n):
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            return False
    return True
    
def proxprim(n):
    for i in range(100):
        if prim(n-i):
            return n-i

N, M = map(int, input().split(' '))

p1 = proxprim(N)
p2 = proxprim(M)

print(p1*p2)
