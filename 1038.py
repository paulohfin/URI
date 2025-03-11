while True:
    try:
        prod, qtd = map(int, input().split(' '))
        
        if prod == 1:
            print(f'Total: R$ %0.2f' %(qtd * 4))
        elif prod == 2:
            print(f'Total: R$ %0.2f' %(qtd * 4.5))
        elif prod == 3:
            print(f'Total: R$ %0.2f' %(qtd * 5))
        elif prod == 4:
            print(f'Total: R$ %0.2f' %(qtd * 2))
        elif prod == 5:
            print(f'Total: R$ %0.2f' %(qtd * 1.5))
    except EOFError:
        break