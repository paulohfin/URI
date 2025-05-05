'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.
'''
while True:
    try:
        a = 0
        b = 0
        while True:
            a = float(input())
            if a < 0 or a > 10:
                print('nota invalida')
            else:
                break
                
        while True:
            b = float(input())
            if b < 0 or b > 10:
                print('nota invalida')
            else:
                break
            
        print(f'media = %0.2f' %((a + b) / 2))
        break
    
    except EOFError:
        break
