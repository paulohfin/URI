'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''
leitura1 = input()
leitura2 = input()
leitura3 = input()
leitura4 = input()

a = leitura1.split(' ')
dia1 = int(a[1])
a = leitura2.split(' ')
h1 = int(a[0])
m1 = int(a[2])
s1 = int(a[4])
a = leitura3.split(' ')
dia2 = int(a[1])
a = leitura4.split(' ')
h2 = int(a[0])
m2 = int(a[2])
s2 = int(a[4])

s = s2 - s1
if s < 0:
    m2 -= 1 
    s += 60
m = m2 - m1
if m < 0:
    h2 -= 1 
    m += 60
h = h2 - h1
if h < 0:
    dia2 -= 1 
    h += 24
dia = dia2 - dia1
print(dia,'dia(s)')
print(h,'hora(s)')
print(m,'minuto(s)')
print(s,'segundo(s)')
