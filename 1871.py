while True:
    try:
        num1, num2 = map(int, input().split(' '))
        if num1 == 0 and num2 == 0:
            break
        num = num1 + num2
        soma = str(num)
        soma2 = []
        for i in soma:
            if i != '0':
                soma2.append(i)
        for i in soma2:
            print(i, end='')
        print()
    except EOFError:
        break