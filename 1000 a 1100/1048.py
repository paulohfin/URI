'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	            Percentual de Reajuste
    0 - 400.00              15%
    400.01 - 800.00         12%
    800.01 - 1200.00        10%
    1200.01 - 2000.00        7%
    Acima de 2000.00         4%







Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.
'''
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
