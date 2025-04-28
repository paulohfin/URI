n = int(input())
l = input().split(' ')

while len(l) > 1:
    t = []
    for i in range(len(l) - 1):
        if l[i + 1] == l[i]:
            t.append(1)
        else:
            t.append(-1)
    l = t   
if l[0] == 1:
    print('preta')
else:
    print('branca')