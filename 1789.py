def maior(a, b):
    if a > b:
        return a 
    else:
        return b

while True:
    try:
        n = int(input())
        lesma = input().split(' ')
        v = 0
        for i in lesma:
            if i != '':
                if int(i) >= 20:
                    v = maior(v, 3)
                elif int(i) >= 10:
                    v = maior(v,2)
                else:
                    v = maior(v,1)
        print(v)
    except EOFError:
        break