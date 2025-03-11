import math

def area(n):
    return (8/5) * n * n * math.sqrt(3)/4

while True:
    try:
        n = int(input())
        print('%.2f' %area(n))
    except EOFError:
        break;