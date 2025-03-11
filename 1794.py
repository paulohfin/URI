n = int(input())

LA, LB = map(int, input().split(' '))
SA, SB = map(int, input().split(' '))
if LA > LB:
    maximo = LA
    LA = LB
    LB = maximo
if SA > SB:
    maximo = SA
    SA = SB
    SB = maximo
    
if LA <= n and n <= LB and SA <= n and n <= SB:
    print('possivel')
else:
    print('impossivel')