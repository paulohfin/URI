n = int(input())

for i in range(n):
    hame = input().split('k')
    a1 = hame[0].count('a')
    a2 = hame[1].count('a')
    print('k', end='')
    for j in range(a1 * a2):
        print('a', end='')
    print()