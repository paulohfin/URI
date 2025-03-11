a = []
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
pos = 0

for i in range(len(a)):
    if a[i] > 0:
        pos += 1
        
print(pos, 'valores positivos')