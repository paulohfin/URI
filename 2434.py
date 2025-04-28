n, s = map(int, input().split(' '))
menor = 0
for i in range(n):
    m = int(input())
    s += m 
    if i == 0:
        menor = s
    elif s < menor:
        menor = s 
print(menor)