n = int(input())
for i in range(n):
    l = input().split(' ')
    if l[1] == '+':
        erro = int(l[4]) - (int(l[0]) + int(l[2]))
        if erro < 0:
            erro = -erro
        print('E',end='')
        for i in range(erro):
            print('r',end='')
        print('ou!')
    elif l[1] == '-':
        erro = int(l[4]) - (int(l[0]) - int(l[2]))
        if erro < 0:
            erro = -erro
        print('E',end='')
        for i in range(erro):
            print('r',end='')
        print('ou!')
    else:
        erro = int(l[4]) - (int(l[0]) * int(l[2]))
        if erro < 0:
            erro = -erro
        print('E',end='')
        for i in range(erro):
            print('r',end='')
        print('ou!')