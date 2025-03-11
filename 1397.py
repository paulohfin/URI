n = int(input())

while n != 0:
    a = 0
    b = 0
    for i in range(n):
        A, B = map(int, input().split(' '))
        
        if A > B:
            a += 1 
        elif B > A:
            b += 1
        
    print(a,b)
    n = int(input())