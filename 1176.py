def fibo(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1 
    else:
        a = []
        a.append(0)
        a.append(1)
        for i in range(2, k+1):
            a.append(a[i - 1] + a[i-2])
        return a[len(a)-1]

n = int(input())

for i in range(n):
    k = int(input())
    
    print('Fib(' + str(k) + ') = ' + str(fibo(k)))