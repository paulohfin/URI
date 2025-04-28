import math

while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = map(int, input().split(' '))
        
        if math.sqrt((xf - xi) * (xf - xi) + (yf - yi) * (yf - yi)) + 1.5 * vi <= r1 + r2:
            print('Y')
        else:
            print('N')
    except EOFError:
        break