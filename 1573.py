import math

a, b, c = map(int, input().split(' '))

while a != 0 and b != 0 and c != 0:
    aresta = math.pow(a * b * c, 1/3)
    print(int(aresta))
    a, b, c = map(int, input().split(' '))