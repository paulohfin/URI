n, m = map(int, input().split(' '))
A = []

def ver(i,j,n, m):
    for k in range(3):
        for l in range(3):
            if (k != 1 or l != 1) and A[i+k][j+l] != '7':
                return False
                
    return True
x = 0
y = 0
for i in range(n):
    k = input().split(' ')
    A.append(k)

for i in range(n-2):
    for j in range(m-2):
        if A[i+1][j+1] == '42' and ver(i,j,n,m) == True:
            x = i + 2 
            y = j + 2 
            
print(x, y)