a, b = map(int, input().split(' '))

hora = 0
while True:
    hora += 1 
    a += 1
    
    if a == 24:
        a = 0
    if a == b:
        break 
    
print("O JOGO DUROU " + str(hora) + ' HORA(S)')