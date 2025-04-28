n = int(input())
ant = 0
j = 1
for i in range(n):
    if i == 0:
        ant = int(input())
    else:
        k = int(input())
        if k != ant:
            j += 1 
            ant = k 
print(j)