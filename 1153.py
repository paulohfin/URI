def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
        
valor = int(input())

print(fatorial(valor))