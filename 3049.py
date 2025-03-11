while True:
    try:
        a = int(input())
        b = int(input())
        area = (a + b) * 35
        if area > 5600:
            print(1)
        elif area < 5600:
            print(2)
        else:
            print(0)
    except EOFError:
        break