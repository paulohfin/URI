a= int(input())
b= int(input())

if a > b:
    maxi = a
    a = b 
    b = maxi
soma = 0
for i in range(a + 1, b):
    if i % 2 != 0:
        soma += i
print(soma)