n = int(input())
k = input().split(' ')
z = 1
if n > 2:
    for i in range(len(k) - 2):
        if (int(k[i+2]) > int(k[i+1]) and int(k[i+1]) < int(k[i])) or (int(k[i+2]) < int(k[i+1]) and int(k[i+1]) > int(k[i])):
            z = 1 
        else:
            z = 0
elif n == 2:
    if k[0] == k[1]:
        z = 0
print(z)