n = int(input())
dentro = 0
fora = 0
for i in range(n):
    z = int(input())
    if z >= 10 and z <= 20:
        dentro += 1
    else:
        fora += 1
        
print(dentro, 'in')
print(fora, 'out')