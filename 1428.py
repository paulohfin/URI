import math

n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    
    print(math.ceil((a - 2) / 3) * math.ceil((b - 2) / 3))