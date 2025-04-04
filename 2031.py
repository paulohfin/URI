n = int(input())

for i in range(n):
    j1 = input()
    j2 = input()
    if j1 == 'ataque':
        if j2 == 'ataque':
            print('Aniquilacao mutua')
        elif j2 == 'pedra':
            print('Jogador 1 venceu')
        elif j2 == 'papel':
            print('Jogador 1 venceu')
    elif j1 == 'pedra':
        if j2 == 'ataque':
            print('Jogador 2 venceu')
        elif j2 == 'pedra':
            print('Sem ganhador')
        elif j2 == 'papel':
            print('Jogador 1 venceu')
    elif j1 == 'papel':
        if j2 == 'ataque':
            print('Jogador 2 venceu')
        elif j2 == 'pedra':
            print('Jogador 2 venceu')
        elif j2 == 'papel':
            print('Ambos venceram')