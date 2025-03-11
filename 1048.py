salario = float(input())

if salario <= 400:
    print('Novo salario: %.2f' %(salario * 1.15))
    print('Reajuste ganho: %.2f' %(salario * 0.15))
    print('Em percentual: 15 %')
elif salario <= 800:
    print('Novo salario: %.2f' %(salario * 1.12))
    print('Reajuste ganho: %.2f' %(salario * 0.12))
    print('Em percentual: 12 %')
elif salario <= 1200:
    print('Novo salario: %.2f' %(salario * 1.1))
    print('Reajuste ganho: %.2f' %(salario * 0.1))
    print('Em percentual: 10 %')
elif salario <= 2000:
    print('Novo salario: %.2f' %(salario * 1.07))
    print('Reajuste ganho: %.2f' %(salario * 0.07))
    print('Em percentual: 7 %')
elif salario > 2000:
    print('Novo salario: %.2f' %(salario * 1.04))
    print('Reajuste ganho: %.2f' %(salario * 0.04))
    print('Em percentual: 4 %')