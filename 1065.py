a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
pos = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        pos += 1
        
print(pos, 'valores pares')