while True:
    try:
        n = int(input())
        
        for i in range(n):
            for j in range(n):
                if i == int(n/2) and j == int(n/2):
                    print('4',end='')
                elif i+1 > n/3 and j+1 > n/3 and i < 2*n/3 and j < 2*n/3:
                    print('1',end='')
                elif i + j == n - 1:
                    print('3',end='')
                elif i == j:
                    print('2',end='')
                else:
                    print('0',end='')
            print()
        print()
    except EOFError:
        break 