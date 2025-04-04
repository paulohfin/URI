caso = 1
while True:
    try:
        n = int(input())
        if n == 0:
            print('Caso ' + str(caso) + ': 1 numero')
            print('0')
            print()
        
        elif n == 1:
            print('Caso ' + str(caso) + ': 2 numeros')
            print('0 1')
            print()
        
        else:
            print('Caso ' + str(caso) + ': ' + str(1 + int((1 + n) * n/2)) + ' numeros')
            print(0, end='')
            for i in range(n + 1):
                for j in range(i):
                    print(' ' + str(i), end='')
            print()
            print()
        caso += 1
    except EOFError:
        break