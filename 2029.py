while True:
    try:
        v = float(input())
        d = float(input())
        area = 3.14 * d * d/4
        a = v/area
        print('ALTURA = %.2F'%a)
        print('AREA = %.2F'%area)
    except EOFError:
        break