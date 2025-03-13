n = int(input())

for m in range(n):
    sobre = input()
    cont = 0
    for i in sobre:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and  i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U': 
            cont += 1
        else:
            cont = 0
        if cont > 2:
            print(sobre,'nao eh facil')
            break
    if cont <= 2:
        print(sobre,'eh facil')