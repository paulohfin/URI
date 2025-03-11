import math

while True:
    try:
        A, D, R = map(float,input().split(' '))
        print('%.4f' %(A + D * math.tan((R - 90) * 3.1415926535 / 180)))
    except EOFError:
        break;