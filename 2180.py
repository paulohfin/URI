def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while True:
    try:
        soma = 0
        cont = 0
        n = int(input())
        while cont < 10:
           if primo(n):
               cont += 1
               soma += n
           n+=1
        print(soma, 'km/h')
        print(int(60000000/soma),'h /',int(60000000/(soma * 24)),'d')
    except EOFError:
        break;