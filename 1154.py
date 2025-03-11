n = 0
soma = 0
while True:
    idade = int(input())
    
    if idade < 0:
        break
    
    n += 1
    soma += idade
    
if n == 0:
    print('0')
else:
    print('%0.2f' %float(soma/n))