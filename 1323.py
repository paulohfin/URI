n = int(input())
while n != 0:
    soma = 0
    for i in range(1, n + 1):
        soma += i * i
    print(soma)
    n = int(input())