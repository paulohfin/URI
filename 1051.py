salario = float(input())
desconto = 0
if salario <= 2000:
    print('Isento')
else:
    salario -= 2000
    if salario <= 1000:
        desconto = salario * 0.08
    else:
        desconto = 80
        salario -= 1000
        if salario <= 1500:
            desconto += salario * 0.18
        else:
            desconto += 1500 * 0.18
            salario -= 1500
            desconto += salario * 0.28
    print('R$ %.2f' %(desconto))