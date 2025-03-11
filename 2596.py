c = int(input())
for i in range(c):
    n = int(input())
    cel = 0
    for j in range(1, n+1):
        div = 0
        for k in range(1, j + 1):
            if j % k == 0:
                div += 1 
        if div % 2 == 0:
            cel += 1 
    print(cel)