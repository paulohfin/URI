def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fatorial(n):
    if n < 2:
        return 1 
    else:
        return n * fatorial(n - 1)

while True:
    try:
        n = int(input())
        linha = input().split(' ')
        
        for i in linha:
            
            if i != '':
                if primo(int(i)):
                    print(i + '! =',fatorial(int(i)))
    except EOFError:
        break