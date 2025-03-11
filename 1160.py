n = int(input())

for i in range(n):
    pa, pb, g1, g2 = map(float, input().split(' '))
    
    cont = 0
    while pa <= pb and cont <= 100:
        pa *= (100 + g1) / 100
        pb *= (100 + g2) / 100
        cont += 1
        pa = int(pa)
        pb = int(pb)
    if cont > 100:
        print('Mais de 1 seculo.')
    else:
        print(str(cont) + ' anos.')