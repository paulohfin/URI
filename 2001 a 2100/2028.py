'''
Hyam é um menino que adora sequências. Ele anda descobrindo sequências interessantes que nem mesmo Fibonacci imaginaria. Certo dia, Hyam percebeu que dado um número N, ele poderia fazer uma sequência do tipo 0 1 2 2 3 3 3 4 4 4 4 ... N N N ... N. No entanto, Hyam percebeu que cada valor que aumentava no número da sequência, a quantidade total de números da sequência aumentava semelhantemente à um crescimento fatorial, neste caso, ao invés de multiplicar, soma-se o número total de números da sequência com o valor do próximo número da sequência. Por exemplo, se N = 2. A sequência correta seria 0 1 2 2, obtendo-se 4 digitos. Agora, se N = 3, o próximo número da sequência tem valor 3, então a quantidade total de número da sequência seria a quantidade de números com N = 2, que é 4, mais o valor do próximo número da sequência, neste caso 3, obtendo-se 7, já que a sequência correta para N = 3 é 0 1 2 2 3 3 3.

Sua tarefa é fazer um algoritmo que dado um número inteiro N, tenha como resposta a quantidade total de números dessa sequência e logo abaixo a sequência completa.

Entrada
A entrada é composta de vários casos de testes. Cada caso é composto por um inteiro N (0<=N<=200) que indica o valor dos últimos N números da sequência.

A entrada termina com final de arquivo (EOF).

Saída
A saida é no formato Caso X: N numeros onde X é a ordem do número de casos e N é a quantidade de numeros que contém na sequência completa, na próxima linha a sequência de números com um espaço entre eles. É pedido que deixe uma linha em branco após cada caso.
'''
caso = 1
while True:
    try:
        n = int(input())
        if n == 0:
            print('Caso ' + str(caso) + ': 1 numero')
            print('0')
            print()
        
        elif n == 1:
            print('Caso ' + str(caso) + ': 2 numeros')
            print('0 1')
            print()
        
        else:
            print('Caso ' + str(caso) + ': ' + str(1 + int((1 + n) * n/2)) + ' numeros')
            print(0, end='')
            for i in range(n + 1):
                for j in range(i):
                    print(' ' + str(i), end='')
            print()
            print()
        caso += 1
    except EOFError:
        break
