a, b = map(int, input().split(' '))

for i in range(1, b + 1):
    if i % a == 0:
        print(i, end='\n')
    else:
        print (i, end=' ')