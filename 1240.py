num = int(input())
for z in range(num):
    n =  input()
    
    p = n.split(' ')
    
    t1 = len(p[0])
    t2 = len(p[1])
    v = True
    if(t2 > t1):
     v = False
    elif t2 == t1 and p[1] not in p[0]:
     v = False
    else:
     for i in range(t2):
      if p[0][t1 - t2 + i] == p[1][i]:
       continue
      else:
       v = False
       break
    
    if(v == True):
     print('encaixa')
    else: print('nao encaixa')