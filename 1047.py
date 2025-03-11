hi, mi, hf, mf = map(int, input().split(' '))

hora = 0
minuto = 0

while True:
    mi += 1
    minuto += 1
    
    if mi == 60:
        mi = 0
        hi += 1
    if minuto == 60:
        minuto = 0
        hora += 1
        
    if hi == 24:
        hi = 0
        
    if hi == hf and mi == mf:
        break 
    
print("O JOGO DUROU " + str(hora) + ' HORA(S) E ' +str(minuto) + ' MINUTO(S)')