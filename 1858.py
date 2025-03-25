n = int(input())
mi = 1
men = 0
num = input().split(' ')
for i in range(len(num)):
    if i == 0:
        men = int(num[i])
    elif int(num[i]) < int(men):
        men = num[i]
        mi = i + 1 
print(mi)