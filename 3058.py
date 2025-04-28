n = int(input())
Min = 0
for i in range(n):
    a, b = map(float, input().split(' '))
    if i == 0:
        Min = 1000 / b * a 
    elif 1000 / b * a < Min:
        Min = 1000 / b * a 
print('%.2f'%Min)