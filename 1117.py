while True:
    try:
        a = 0
        b = 0
        while True:
            a = float(input())
            if a < 0 or a > 10:
                print('nota invalida')
            else:
                break
                
        while True:
            b = float(input())
            if b < 0 or b > 10:
                print('nota invalida')
            else:
                break
            
        print(f'media = %0.2f' %((a + b) / 2))
        break
    
    except EOFError:
        break