import math

g = 9.80665
pi = 3.14159
while True:
    try:

        h = float(input())
        p1, p2 = map(int, input().split(' '))
        n = int(input())
        for i in range(n):
            alpha, vel = map(float, input().split(' '))
            
            vy = vel * math.sin(alpha * pi / 180) 
            t = vy/g 
            hmax = h + vy*t - g*t*t/2
            tf = math.sqrt(2*hmax/g)
            vx = vel * math.cos(alpha * pi / 180) 
            acertou = vx * (t + tf)
            if acertou > p1 and acertou < p2:
                print('%.5f'%acertou + str(' -> DUCK'))
            else:
                print('%.5f'%acertou + str(' -> NUCK'))
    except EOFError:
        break