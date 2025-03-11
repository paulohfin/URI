a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
pos = 0
neg = 0
par = 0
impar = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        par += 1
    else:
        impar += 1
    if a[i] > 0:
        pos += 1
    if a[i] < 0:
        neg += 1

        
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s)')