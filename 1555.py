def funcao(x, y):
    if 9 * x * x + y * y > 2 * x * x + 25 * y * y and 9 * x * x + y * y > -100 * x + y * y * y:
        print('Rafael ganhou')
    elif 2 * x * x + 25 * y * y > -100 * x + y * y * y:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')
        
n = int(input())
for i in range(n):
    p = input().split(' ')
    funcao(int(p[0]), int(p[1]))