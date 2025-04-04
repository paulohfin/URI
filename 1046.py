'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
'''
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
