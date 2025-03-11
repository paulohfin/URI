cod1, num1, valor1 = map(float, input().split(' '))

cod2, num2, valor2 = map(float, input().split(' '))

print(f"VALOR A PAGAR: R$ %0.2f" %( num1 * valor1 + num2 * valor2))