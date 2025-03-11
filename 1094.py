n = int(input())
nc = 0
nr = 0
ns = 0
total = 0
for i in range(n):
    a, b = input().split(' ')
    if b == 'C':
        nc += int(a)
    if b == 'R':
        nr += int(a)
    if b == 'S':
        ns += int(a)
    total += int(a)
print('Total: ' + str(total) + ' cobaias')
print('Total de coelhos: ' + str(nc))
print('Total de ratos: ' + str(nr))
print('Total de sapos: ' + str(ns))
print('Percentual de coelhos: %.2f' %(nc/total * 100) + ' %')
print('Percentual de ratos: %.2f' %(nr/total * 100) + ' %')
print('Percentual de sapos: %.2f' %(ns/total * 100) + ' %')