while True:
    try:
        t = input().split(':')
        tempo = int(t[0]) * 60 + int(t[1])
        if tempo + 60 > 480:
            print('Atraso maximo:',tempo + 60 - 480)
        else:
            print('Atraso maximo:',0)
    except EOFError:
        break