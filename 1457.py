def fatorial(n, k):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - k,k)

n = int(input())
for i in range(n):
    p = input().split('!')
    print(fatorial(int(p[0]), len(p) - 1))