n = int(input())

for i in range(n):
    x, y = map(int, input().split(' '))
    
    if y == 0:
        print('divisao impossivel')
    else:
        print(f'%0.1f' %(float(x/y)))