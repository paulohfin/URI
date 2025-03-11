import math

while True:
    try:
        d, vf, vg = map(int, input().split(' '))
        
        mf = float(12 / vf)
        mg = float(math.sqrt(144 + d * d)/vg)
        if mg <= mf:
            print("S")
        else:
            print("N")
            
    except EOFError:
        break