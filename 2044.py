while True:
    try:
        n = int(input())
        while n != -1:
            soma = 0
            vez = 0
            a = input().split(' ')
            for i in a:
                if i != '':
                    soma += int(i)
                    if soma % 100 == 0 :
                        soma = 0 
                        vez += 1
            print(vez)
            n = int(input())
        break
    except EOFError:
        break