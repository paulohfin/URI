def perfeito(p):
    soma = 0
    for i in range(1, p):
        if p % i == 0:
            soma += i
    return soma

n = int(input())

for i in range(n):
    p = int(input())
    
    if perfeito(p) == p:
        print(p, 'eh perfeito')
    else:
        print(p, 'nao eh perfeito')