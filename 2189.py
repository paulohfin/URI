cont = 1

n = int(input())
while n != 0:
    print('Teste', cont)
    linha = input().split(' ')
    cont2 = 1
    for i in linha:
        if i == '' + str(cont2):
            print(i)
        cont2 += 1
    print()
    cont += 1
    n = int(input())