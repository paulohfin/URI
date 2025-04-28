import math

def fibo(n):
    return (math.pow((1 + math.sqrt(5))/2,n) - math.pow((1 - math.sqrt(5))/2,n))/math.sqrt(5)

while True:
    try:
        n = int(input())
        
        print('%.1f'%(fibo(n)))
    except EOFError:
        break