def abs(a):
    if a >= 0: return a
    else: return -a

def maior(a, b):
    return (a + b + abs(a - b))/2

a1, a2, a3 = map(int, input().split(' '))

m = maior(a1, maior(a2, a3))

print(int(m), 'eh o maior')