while True:
    try:
        n = int(input())
        if(n != 0):
            x, y = map(int, input().split(' '))
            for i in range(n):
                
                x2, y2 = map(int, input().split(' '))
                if x2 == x or y2 == y:
                    print('divisa')
                elif y2 > y and x2 > x:
                    print('NE')
                elif y2 > y and x2 < x:
                    print("NO")
                elif y2 < y and x2 > x:
                    print('SE')
                else:
                    print("SO")
        else:
            break
    except EOFError:
        break