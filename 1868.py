def printar(n, posx, posy):
    for i in range(n):
        for j in range(n):
            if i == posy and j == posx:
                print('X', end='')
            else:
                print('O', end='')
        print()
    print('@')

n = int(input())
while n != 0:
    meio = int(n / 2)
    posx = meio
    posy = meio
    printar(n, posx, posy)
    add = 1
    posx += 1
    while posx < n:
        printar(n, posx, posy)
        
        while posy > meio - add:
            posy -= 1
            printar(n, posx, posy)
        
        while posx > meio - add:
            posx -= 1
            printar(n, posx, posy)
            
        while posy < meio + add:
            posy += 1
            printar(n, posx, posy)
            
        while posx < meio + add:
            posx += 1
            printar(n, posx, posy)
        posx += 1
        add += 1
        
    n = int(input())