n = int(input())
for i in range(n):
    soma = 0
    a, b = input().split(' ')
    for i in range(len(a)):
        soma += (ord(b[i]) - ord(a[i])) % 26
    print(soma)