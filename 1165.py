def primo(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

n = int(input())

for i in range(n):
    p = int(input())
    
    if primo(p):
        print(p, 'eh primo')
    else:
        print(p, 'nao eh primo')