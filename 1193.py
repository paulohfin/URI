n = int(input())

for i in range(n):
    k = input().split(' ')
    
    if k[1] == 'dec':
        print('Case ' + str(i+1) + ':')
        print(hex(int(k[0]))[2:],'hex')
        print(bin(int(k[0]))[2:],'bin')
    elif k[1] == 'hex':
        print('Case ' + str(i+1) + ':')
        print(int(k[0],16), 'dec')
        print(bin(int(k[0],16))[2:],'bin')
    elif k[1] == 'bin':
        print('Case ' + str(i+1) + ':')
        print(int(k[0],2),'dec')
        print(hex(int(k[0],2))[2:],'hex')
    print()