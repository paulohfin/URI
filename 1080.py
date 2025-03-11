pos = 1
maior = int(input())
for i in range(99):
    n = int(input())
    if n > maior:
        maior = n
        pos = i + 2 
print(maior)
print (pos)