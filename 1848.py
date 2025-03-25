
for i in range(3):
    caw = input()
    num = 0
    while caw != 'caw caw':
        if caw[0] == '*':
            num += 4
        if caw [1] == '*':
            num += 2
        if caw[2] == '*':
            num += 1
        caw = input()
    print(num)