n = int(input())

for i in range(n):
    b = int(input())
    
    a1, d1, l1 = map(int, input().split(' '))
    a2, d2, l2 = map(int, input().split(' '))
    
    vg1 = (a1 + d1)/2
    if l1 % 2 == 0:
        vg1 += b
    vg2 = (a2 + d2)/2
    if l2 % 2 == 0:
        vg2 += b
        
    if vg1 < vg2:
        print('Guarte')
    elif vg2 < vg1:
        print('Dabriel')
    else:
        print('Empate')