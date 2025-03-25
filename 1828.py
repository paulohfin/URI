n = int(input())

for i in range(n):
    linha = input().split(' ')
    print('Caso #%d:' %(i + 1), end=' ')
    if linha[0] == 'tesoura':
        if linha[1] == 'papel':
            print('Bazinga!')
        elif linha[1] == 'Spock':
            print('Raj trapaceou!')
        elif linha[1] == 'lagarto':
            print('Bazinga!')
        elif linha[1] == 'pedra':
            print('Raj trapaceou!')
        elif linha[1] == 'tesoura':
            print('De novo!')
    elif linha[0] == 'pedra':
        if linha[1] == 'papel':
            print('Raj trapaceou!')
        elif linha[1] == 'Spock':
            print('Raj trapaceou!')
        elif linha[1] == 'lagarto':
            print('Bazinga!')
        elif linha[1] == 'pedra':
            print('De novo!')
        elif linha[1] == 'tesoura':
            print('Bazinga!')
    elif linha[0] == 'papel':
        if linha[1] == 'papel':
            print('De novo!')
        elif linha[1] == 'Spock':
            print('Bazinga!')
        elif linha[1] == 'lagarto':
            print('Raj trapaceou!')
        elif linha[1] == 'pedra':
            print('Bazinga!')
        elif linha[1] == 'tesoura':
            print('Raj trapaceou!')
    elif linha[0] == 'Spock':
        if linha[1] == 'papel':
            print('Raj trapaceou!')
        elif linha[1] == 'Spock':
            print('De novo!')
        elif linha[1] == 'lagarto':
            print('Raj trapaceou!')
        elif linha[1] == 'pedra':
            print('Bazinga!')
        elif linha[1] == 'tesoura':
            print('Bazinga!')
    elif linha[0] == 'lagarto':
        if linha[1] == 'papel':
            print('Bazinga!')
        elif linha[1] == 'Spock':
            print('Bazinga!')
        elif linha[1] == 'lagarto':
            print('De novo!')
        elif linha[1] == 'pedra':
            print('Raj trapaceou!')
        elif linha[1] == 'tesoura':
            print('Raj trapaceou!')