val = [[1001,1.5],[1002,2.5],[1003,3.5],[1004,4.5],[1005,5.5]]

n = int(input())
soma = 0
for i in range(n):
    cod, qtd = map(int, input().split(' '))
    for j in val:
        if j[0] == cod:
            soma += j[1] * qtd
print('%.2f' %soma)