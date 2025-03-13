n = int(input())
soma = 0
for i in range(n):
    L, C = map(int, input().split(' '))
    
    if L > C:
        soma += C
print(soma)