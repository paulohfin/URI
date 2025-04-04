while True:
    try:
        p, j1, j2, r, a = map(int, input().split(' '))
        
        if r == 1 and a == 0: print('Jogador 1 ganha!')
        elif r == 0 and a == 1: print('Jogador 1 ganha!')
        elif r == 1 and a == 1: print('Jogador 2 ganha!')
        elif p == 0 and (j1 + j2) % 2 != 0:  print('Jogador 1 ganha!')
        elif p == 1 and (j1 + j2) % 2 == 0: print('Jogador 1 ganha!')
        else: print('Jogador 2 ganha!')
    except EOFError:
        break