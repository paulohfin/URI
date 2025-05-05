'''
Matring é uma mistura de Matriz e String. Ela foi desenvolvida pela UNILA (União dos Nerds para Integração da Lógica e da Aventura) para manter mensagens seguras de escutas.

A primeira e última coluna de uma matring guarda a chave para traduzi-la na mensagem original. As colunas restantes de uma matring representam uma string codificada em ASCII, uma coluna por caractere.

Para uma mensagem com N caracteres, a matring correspondente é uma matriz 4x(N+2) de dígitos. Cada coluna é lida como um número de 4 dígitos; uma sequência de dígitos de cima para baixo é o mesmo que uma sequência de dígitos da esquerda para a direita na horizontal.

Seja o primeiro número F, o último número L e os restantes uma sequência de números Mi, onde 1 ≤ i ≤ N. A primeira coluna de uma matring é indexada por zero.

Para decodificar uma matring para uma string, calculamos: Ci = (F * Mi + L) mod 257, onde Ci é o caractere em ASCII na posição i da mensagem original.

Sua tarefa é desenvolver um algoritmo para decodificar matrings.

Entrada
A entrada é uma matring, ou seja, uma matriz 4x(N+2) de dígitos (de 0 a 9) com 0 < N < 80.

Saída
A saída é dada em uma única linha e corresponde a string decodificada. Inclua o caractere de fim-de-linha após a string.
'''
while True:
    try:
        linha1 = input()
        linha2 = input()
        linha3 = input()
        linha4 = input()
        
        num1 = int(linha1[0]) * 1000 + int(linha2[0]) * 100 + int(linha3[0]) * 10 + int(linha4[0])
        tam = len(linha1)
        num2 = int(linha1[tam - 1]) * 1000 + int(linha2[tam - 1]) * 100 + int(linha3[tam - 1]) * 10 + int(linha4[tam - 1])
        
        for i in range(1, len(linha1) - 1):
            p = int(linha1[i]) * 1000 + int(linha2[i]) * 100 + int(linha3[i]) * 10 + int(linha4[i])
            print(chr((num1 * p + num2)%257), end='')
        print()
    except EOFError:
        break
