n = int(input())

while n != 0:
    soma = 0
    if n % 2 == 0:
        for i in range(5):
            soma += n
            n+=2
    else:
        n = n+1
        for i in range(5):
            soma += n
            n+=2
    print(soma)  
    n = int(input())