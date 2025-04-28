n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    m = []
    for j in range(a):
        m.append(j + 1)
    j = b-1
    while len(m) > 1:
        j %= len(m)
        m.pop(j)
        j += b - 1
    print('Case ' + str(i+1) + ': ' + str(m[0]))