grenais = 0
inte = 0
gremio = 0
empate = 0
i = 0
g = 0
n = 1
while n == 1:
    i, g = map(int, input().split(' '))
    
    grenais += 1
    if i > g:
        inte += 1
    elif i == g:
        empate += 1
    else:
        gremio += 1
    print('Novo grenal (1-sim 2-nao)')
    n = int(input())
    
print(grenais,'grenais')
print('Inter:' + str(inte))
print('Gremio:' + str(gremio))
print('Empates:' + str(empate))
if inte > gremio:
    print('Inter venceu mais')
elif gremio > inte:
    print('Gremio venceu mais')