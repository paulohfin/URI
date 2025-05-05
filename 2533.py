while True:
    try:

        n = int(input())
        nota = 0
        soma1 = 0
        soma2 = 0
        for i in range(n):
            ni, ci = map(int, input().split(' '))
            
            soma1 += ni * ci 
            soma2 += ci * 100
            
            
        print('%.4f'%(soma1/soma2))
    except EOFError:
        break