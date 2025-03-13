n = int(input())
for i in range(n):
    a = input()
    b = input()
    c = input().split('_')
    c1 = len(c[0])
    c2 = len(c[1])
    if(a[c1] == b[c1+c2+1] or b[c1] == a[c1+c2+1]):
        print('Y')
    else:
        print('N')