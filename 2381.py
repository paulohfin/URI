n, k = map(int, input().split(' '))
nome = []
for i in range(n):
    nome.append(input())
nome.sort()
print(nome[k-1])