a, b = map(int, input().split(' '))

while a != 0 and b != 0:
    n0 = 0 
    n1 = 0 
    n2 = 0 
    n3 = 0 
    n4 = 0 
    n5 = 0 
    n6 = 0 
    n7 = 0 
    n8 = 0 
    n9 = 0 
    while a <= b:
        l = str(a)
        n0 += l.count('0')
        n1 += l.count('1')
        n2 += l.count('2')
        n3 += l.count('3')
        n4 += l.count('4')
        n5 += l.count('5')
        n6 += l.count('6')
        n7 += l.count('7')
        n8 += l.count('8')
        n9 += l.count('9')
        a += 1
    print(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)
    a, b = map(int, input().split(' '))