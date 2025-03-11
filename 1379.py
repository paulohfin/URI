a, b = map(int, input().split(' '))

while a != 0 and b != 0:
    print(3 * a - (a + b))
    a, b = map(int, input().split(' '))