def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primoGemeo(n):
    if primo(n) and primo(n - 2):
        return True
    else:
        return False

while True:
    try:
        n = int(input())
        for i in range(n):
            k = primoGemeo(n - i)
            if k == True:
                print(n - i - 2, n - i)
                break
    except EOFError:
        break