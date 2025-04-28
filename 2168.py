n = int(input())

k = []

for i in range(n+1):
    j = input().split(' ')
    k.append(j)

for i in range(n):
    for j in range(n):
        if int(k[i][j]) + int(k[i+1][j]) + int(k[i][j+1]) + int(k[i+1][j+1]) > 1:
            print('S',end='')
        else:
            print('U',end='')
    print()