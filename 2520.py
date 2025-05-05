def dif(a, b):
    if b > a:
        return b - a 
    else:
        return a - b

while True:
    try:
        n, m = map(int, input().split(' '))
        x1 = x2 = y1 = y2 = 0
        for i in range(n):
            l = input().split(' ')
            for j in range(len(l)):
                if l[j] == '1':
                    x1 = i + 1  
                    y1 = j + 1
                if l[j] == '2':
                    x2 = i + 1
                    y2 = j + 1
        
        print(dif(x1,x2) + dif(y1,y2))
    except EOFError:
        break