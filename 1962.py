n = int(input())

for i in range(n):
    ano = int(input())
    
    if ano < 2015:
        print(2015 - ano, 'D.C.')
    else:
        print(ano - 2014, 'A.C.')