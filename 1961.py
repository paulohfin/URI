def mod(n):
    if n > 0:
        return n 
    else:
        return -n

p, n = map(int, input().split(' '))
pulo = input().split(' ')
i = 0
cnt = 0
while i < len(pulo):
    while i < len(pulo) and pulo[i] == '':
        i += 1
    if i < len(pulo): d1 = pulo[i]
    i+=1
    while i < len(pulo) and pulo[i] == '':
        i += 1
        
    if i < len(pulo):
        d2 = pulo[i]
        if mod(int(d2) - int(d1)) <= p:
            cnt += 1
if cnt == n - 1:
    print('YOU WIN')
else:
    print('GAME OVER')