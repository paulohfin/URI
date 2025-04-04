n = int(input())
mat = -1
max1 = -1
for i in range(n):
    mat2, max2 = map(float, input().split(' '))
    if max2 > max1:
        mat = mat2
        max1 = max2 
if max1 < 8:
    print('Minimum note not reached')
else:
    print(int(mat))