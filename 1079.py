n = int(input())

for i in range(n):
    a, b, c = map(float, input().split(' '))
    
    print(f'%0.1f' %((a * 2 + b * 3 + c * 5) / 10))