def triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

while True:
    try:
        
        a, b, c, d = map(int, input().split(' '))
        if triangulo(a, b, c) or triangulo(a, b, d) or triangulo(a, c, d) or triangulo(b, c, d):
            print("S")
        else:
            print("N")
    except EOFError:
        break