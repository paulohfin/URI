'''
Paulinho tem em suas mãos um pequeno problema. A professora lhe pediu que ele construísse um programa para verificar, à partir de dois valores inteiros A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois inteiros A (1 ≤ A < 231 ) e B (1 ≤ B < 231) positivos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.
'''
num = int(input())
for z in range(num):
    n =  input()
    
    p = n.split(' ')
    
    t1 = len(p[0])
    t2 = len(p[1])
    v = True
    if(t2 > t1):
     v = False
    elif t2 == t1 and p[1] not in p[0]:
     v = False
    else:
     for i in range(t2):
      if p[0][t1 - t2 + i] == p[1][i]:
       continue
      else:
       v = False
       break
    
    if(v == True):
     print('encaixa')
    else: print('nao encaixa')
