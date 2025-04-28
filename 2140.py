a, b = map(int, input().split(' '))
while a != 0 and b != 0:
    c = [4, 7, 10, 12, 15, 20, 22, 25, 30, 40, 52, 55, 60, 70, 100, 102, 105, 110, 120, 150, 200]
    k = False
    for i in c:
        if a + i == b:
            k = True
    if k == True:
        print('possible')
    else:
        print('impossible')
    a, b = map(int, input().split(' '))