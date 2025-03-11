soma = 1
i =  3
j = 2
while i < 40:
    #print(soma, '+' + str(i) + '/' + str(j))
    soma += float(i / j)
    i += 2
    j *= 2
print('%.2f' %soma)