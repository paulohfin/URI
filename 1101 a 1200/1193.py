'''
O professor de matemática de Juliano marcou uma prova cujo conteúdo será apenas conversão entre valores decimais, hexadecimais e binários. Uma das coisas mais complexas para Juliano é fazer estas conversões de base entre números. Por mais que estude, tem muita dificuldade para entender. Portanto, como você entende de computação e é amigo(a) de Juliano, ele solicitou a tua ajuda para que faça um programa que verifique se as conversões feitas por ele estão correta.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N, indicando o número de casos de teste que virão a seguir, um por linha. Cada caso de teste contém um valor X (X > 0) seguido de um texto Y com três caracteres, indicando se o valor X está no formato binário, decimal ou hexadecimal. Independente do formato, qualquer dos números deverá caber em um inteiro de 32 bits.

Saída
Para cada caso de teste, você deve apresentar o número de caso de teste seguido por duas linhas, que contém a conversão do valor fornecido para as outras duas bases. A sequência das bases de saída será sempre: decimal, hexadecimal (em minúsculo) e binário, ou seja deve-se respeitar esta ordem excluindo obviamente o formato de entrada.

Obs: deverá ser impressa uma linha em branco após cada caso de teste, inclusive após o último caso de teste.
'''
n = int(input())

for i in range(n):
    k = input().split(' ')
    
    if k[1] == 'dec':
        print('Case ' + str(i+1) + ':')
        print(hex(int(k[0]))[2:],'hex')
        print(bin(int(k[0]))[2:],'bin')
    elif k[1] == 'hex':
        print('Case ' + str(i+1) + ':')
        print(int(k[0],16), 'dec')
        print(bin(int(k[0],16))[2:],'bin')
    elif k[1] == 'bin':
        print('Case ' + str(i+1) + ':')
        print(int(k[0],2),'dec')
        print(hex(int(k[0],2))[2:],'hex')
    print()
