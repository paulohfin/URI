def funcao(x, y):
    print(int(x * y / 2),'cm2')
n = int(input())
for i in range(n):
    p = input().split(' ')
    funcao(int(p[0]), int(p[1]))