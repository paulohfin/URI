n = int(input())
cri = []
comp = 0

for i in range(n):
    k = input().split(' ')
    if k[0] == '+':
        comp += 1
    cri.append(k[1])
cri.sort()
for i in cri:
    print(i)
print('Se comportaram:',comp,'| Nao se comportaram:',n - comp)