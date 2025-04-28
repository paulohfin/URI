n = input()

while n[0] != '-':
    if len(n) > 2 and n[1] == 'x':
        print(int(n[2:],16))
    else:
        print('0x',end='')
        print(hex(int(n)).upper()[2:])
    n = input()