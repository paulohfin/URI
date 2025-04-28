import math

while True:
    try:
        n = int(input())
        
        print('%.1f' %(n/math.log(n)),end=' ')
        print('%.1f' %(1.25506* n/math.log(n)))
    except EOFError:
        break