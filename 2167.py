n = int(input())

l = input().split(' ')
m = 0
for i in range(len(l) - 1):
    if int(l[i+1]) < int(l[i]):
        m = i + 2
        break 
print(m)