n = int(input())
l = []
for i in range(n):
    a = input()
    l.append(a)
c = 0
Max = 0
i = 0
while i < n:
    for j in range(n):
        if l[i][j] == 'o':
            c += 1 
        elif l[i][j] == 'A':
            if c > Max:
                Max = c 
            c = 0
    i += 1 
    if i < n:
        for j in range(n):
            if l[i][n - j - 1] == 'o':
                c += 1 
            elif l[i][n - j - 1] == 'A':
                if c > Max:
                    Max = c 
                c = 0
    i += 1
if c > Max:
    Max = c
print(Max) 