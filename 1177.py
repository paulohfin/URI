n = int(input())
i = 0
j = 0
while i < 1000:
    print('N[' + str(i) + '] = ' + str(j))
    i += 1
    j += 1
    if j == n:
        j = 0