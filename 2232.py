import math

n = int(input())

for i in range(n):
    k = int(input())
    soma = 0
    for j in range(k):
        soma += math.pow(2,j)
    print(int(soma))