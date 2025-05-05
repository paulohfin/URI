'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''
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
