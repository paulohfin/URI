n = int(input())
d = 0
for i in range(n):
    t, v = map(int, input().split(' '))
    d += t * v
print(d)