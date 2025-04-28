def printa(n):
    if n < 10:
        print('0' + str(n),end='')
    else:
        print(n,end='')

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split(' '))
   
    printa(a)
    print(':',end='')
    printa(b)
    if c == 1:
       print(' - A porta abriu!')
    else:
        print(' - A porta fechou!')