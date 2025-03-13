n = int(input())

for m in range(n):
    dieta = input()
    cafe = input()
    almoco = input()
    vit = ''
    stop = False
    for i in range(ord('A'),ord('Z') + 1):
        
        if cafe.count(chr(i)) + almoco.count(chr(i)) > dieta.count(chr(i)):
            print('CHEATER')
            stop = True
            break
        elif dieta.count(chr(i)) > 0:
            if cafe.count(chr(i)) + almoco.count(chr(i)) > 1:
                print('CHEATER')
                stop = True
                break
            elif cafe.count(chr(i)) + almoco.count(chr(i)) == 0:
                vit += chr(i)
    if stop == False:
        print(vit)