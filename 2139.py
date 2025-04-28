import datetime

while True:
    try:
        m, d = map(int, input().split(' '))
        
        data = datetime.date(2016, m, d)
        dt = int(data.strftime('%j'))
        if 360 - dt > 1:
            print('Faltam',360-dt,'dias para o natal!')
        elif 360 - dt == 1:
            print('E vespera de natal!')
        elif 360 - dt == 0:
            print('E natal!')
        else:
            print('Ja passou!')
    except EOFError:
        break