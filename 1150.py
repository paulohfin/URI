x = int(input())
while True:
    z = int(input())
    if z > x:
        break
soma = 0
cont = 0
for i in range(x, z):
    soma += i
    cont += 1
    if soma > z:
        break

print(cont)