'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''
while True:
    try:
        prod, qtd = map(int, input().split(' '))
        
        if prod == 1:
            print(f'Total: R$ %0.2f' %(qtd * 4))
        elif prod == 2:
            print(f'Total: R$ %0.2f' %(qtd * 4.5))
        elif prod == 3:
            print(f'Total: R$ %0.2f' %(qtd * 5))
        elif prod == 4:
            print(f'Total: R$ %0.2f' %(qtd * 2))
        elif prod == 5:
            print(f'Total: R$ %0.2f' %(qtd * 1.5))
    except EOFError:
        break
